用ccache让Xcode运行、打包飞起来
2
2018.04.23 10:46:09
字数 3730
阅读 4316
你想图省事，硬盘空间有几十G的空余，秒切分支，可以看文章底部，有笨重但极方便的方法

概述
   腰果上岸科技有三个APP分别是腰果公考（支持iPad）、上岸计划、每日一题，最近因为在快速迭代开发新功能，项目规模急速增长，单个端业务代码约20万行，私有库约5万行，第三方库代码约20万行，单个客户端的代码行数约45万行。现在打包一次耗时需要10分钟左右。虽然还远远比不上 Facebook 的40分钟，但是我们在内测的时候，经常一天要发布内测版两到三次。打包时CPU占用基本上是百分百的，因为没有专门的 CI 机器，对负责打包的同事（主要是我自己）的工作时间占用比较多，所以最近一直在寻找加快打包速度的方案。

目前的项目架构
   我们的项目使用 CocoaPods 来管理第三方库和私有库的依赖，对大部分项目来说应该是标配了。目前还是纯 Objective-C 的项目，有少量C++，没有引入 Swift。

调研过的方案
   下面列出研究过的一些主流方案以及最后没有采用的原因，这些方案有各自的局限性，但是也给了我不少启发，思考过程跟最终方案一样有价值。

cocoapods-packager
   cocoapods-packager 可以将任意的 pod 打包成 Static Library，省去重复编译的时间，一定程度上可以加快编译时间，但是也有自身的缺点：

优化不彻底，只能优化第三方和私有 Pod 的编译速度，对于其他改动频繁的业务代码无能为力
私有库和第三方库的后续更新很麻烦，当有源码修改后，需要重新打包上传到内部的 Git 仓库
过多的二进制文件会拖慢 Git 的操作速度（目前还没部署 Git 的 LFS）
难以调试源码
Carthage
   这个方案跟 cocoapods-packager 比较类似，优缺点都差不多，但 Carthage 可以比较方便地调试源码。因为我们目前已经大规模使用 CocoaPods，转用 Carthage 来做包管理需要做大量的转换工作，所以不考虑这个方案了。

Buck
   Buck 是一套通用的构建系统，由 Facebook 开源。最大的特色是智能的增量编译可以极大地提高构建速度。最早听说 Buck 的时候，它还只能用在安卓上，现在已经适配了 iOS。它能增快构建速度的主要原因是缓存了编译结果，通过持续监视项目目录的文件变化，每次编译时只编译有改动的文件。另外一个让我很受启发的功能是 HTTP Cache Server，通过一台缓存文件服务器来保存大家的编译结果，这样只要团队里其中一人编译过的文件，其他人就不用再编译了，直接下载就行。

   Buck 是个相当完备的解决方案，很多国外的大公司例如 Uber 都已经用上。我也花了很多时间来研究，最终还是认为对我们的项目和团队来说，目前并不是很适合，主要原因是：

   Buck 抛弃了 Xcode 的项目文件，需要手工编写配置文件来指定编译规则，这要对现有项目作出大幅度的调整。我们目前还在快速迭代新功能，没有余暇和人手来实施。

   开发和调试的流程都得做出很大的改变。因为 Buck 接管了项目编译的过程，想调试项目不能简单地在 Xcode 里面 ⌘+R 了，得先反过来让 Buck 生成 Xcode 的项目文件。Uber 的工程师甚至推荐使用 Nuclide 来代替 Xcode 作为开发环境。虽然原理上是可行的，但是团队需要花不少时间来适应，短期内效率降低无可避免。

   用 Xcode 调试代码享受不到加快编译速度的好处。虽然可以用 buck 命令启动 App，然后在命令行里启动 lldb 来调试，但那就无法使用 Xcode 的调试工具 例如 View Debugging 和 Memory Graph Debugger。

Bazel
   Bazel 跟 Buck 很相似，是 Google 开源的，优缺点跟 Buck 都差不多，不再详细说了。

distcc 分布式编译
   原理是把一部分需要编译的文件发送到服务器上，服务器编译完成后把编译产物传回来。我尝试了一下比较出名的 distcc，搭建过程比较简单，最后也能成功地把编译任务分派到内网的多台服务器上。但是其他编译服务器的 CPU 占用总是很低，只有 20% 左右；也就是说分派任务的速度甚至还赶不上服务器编译的速度，分派任务然后回传编译产物这个过程所耗费的时间超过了本地直接编译。不停调整参数反复试验了很多次，最后发现编译时间完全没有变快，甚至还有点变慢了。可能以我们目前项目的规模并不适合使用分布式编译。

最终方案：CCache
先来看看我对于解决方案的诉求：

能大幅度地提升编译速度，起码要减少掉 50% 的编译时间
不需要对项目作出重大调整
不需要改变开发工具链
   CCache 是一个能够把编译的中间产物缓存起来的工具，在其他领域已经有不少应用，只是在 iOS 界的实践比较少。经过我的实践，它能够满足我前面的三点要求。我最早认识到它是搜到了这篇文章：Using ccache for Fun and Profit | Inside PSPDFKit

   如果你不使用 CocoaPods，参照上面的文章即可。因为针对 CocoaPods 需要作出一些额外的调整，所以还是说明一下。下面就来说说要怎样把 CCache 应用在用 CocoaPods 作为包管理工具的 iOS 项目中。

安装步骤
   注意：项目路径不能有中文，否则会影响 CCache 的正常工作

安装 CCache
   首先你需要在电脑上安装 Homebrew，对使用 macOS 的程序员来说应该是标配，略过。通过 Homebrew 安装 CCache， 在命令行中执行

$ brew install ccache
   命令跑完后即安装成功，中间可能会遇到升级Homebrew，不用做特殊处理，等待终端自动完成即可。

创建 CCache 编译脚本
   为了能让 CCache 介入到整个编译的过程，我们要把 CCache 作为项目的 C 编译器，当 CCache 找不到编译缓存时，它会再把编译指令传递给真正的编译器 clang。

ccache-clang
   cd到项目目录，新建一个文件命名为 ccache-clang 的空白文件即可。

$ touch ccache-clang
   在find 中双击打开，输入下面这段脚本并保存。

#!/bin/sh
if type -p ccache >/dev/null 2>&1; then
  export CCACHE_MAXSIZE=10G
  export CCACHE_CPP2=true
  export CCACHE_HARDLINK=true
  export CCACHE_SLOPPINESS=file_macro,time_macros,include_file_mtime,include_file_ctime,file_stat_matches
  
  # 指定日志文件路径到桌面，等下排查集成问题有用，集成成功后删除，否则很占磁盘空间
  export CCACHE_LOGFILE='~/Desktop/CCache.log'
  exec ccache /usr/bin/clang "$@"
else
  exec clang "$@"
fi
   在命令行中， ccache-clang 文件的目录，把它的权限改成可执行文件

$ chmod 777 ccache-clang
ccache-clang++
   如果你的代码或者是第三方库的代码用到了C++，用同样的方法创建一个ccache-clang++。相应的对clang的调用也要改成clang++，否则 CCache 不会应用在 C++ 的代码上。

#!/bin/sh
if type -p ccache >/dev/null 2>&1; then
  export CCACHE_MAXSIZE=10G
  export CCACHE_CPP2=true
  export CCACHE_HARDLINK=true
  export CCACHE_SLOPPINESS=file_macro,time_macros,include_file_mtime,include_file_ctime,file_stat_matches
  
  # 指定日志文件路径到桌面，等下排查集成问题有用，集成成功后删除，否则很占磁盘空间
  export CCACHE_LOGFILE='~/Desktop/CCache.log'
  exec ccache /usr/bin/clang++ "$@"
else
  exec clang++ "$@"
fi
   完成后项目中应该有这两个文件

创建完成
Xcode 项目的调整
定义CC常量
   在你项目的构建设置(Build Settings)中，添加一个常量CC，这个值会让 Xcode 在编译时把执行路径的可执行文件当做 C 编译器。CC常量的值为 $(SRCROOT)/ccache-clang，如果你的脚本不是放在项目根目录，则自行调整路径。如果一运行项目就报错，检查下路径是不是填错了。
定义CC常量
关闭 Clang Modules
   因为 CCache 不支持 Clang Modules，所以需要把 Enable Modules 的选项关掉。这个问题在 CocoaPods 上如何处理，后面会讲。
   关闭了 Enable Modules 后需要作出的调整因为关闭了 Enable Modules，所以必须删除所有的 @import语句，替换为#import的语法例如将 @import UIKit 替换为 #import <UIKit/UIKit.h>。之后，如果你用到了其他的系统框架例如 AVFoundation、CoreLocation等，现在 Xcode 不会再帮你自动引入了，你得要在项目 Target 的 Build Phrase -> Link Binary With Libraries 里面自己手动引入。

可能需要重新引入的库
可能需要重新导入的系统库
测试效果
   尝试编译一遍，然后在命令行里输入 ccache -s 就能看见类似下面的 ccache 运行情况统计：

cache directory                     /Users/mac/.ccache
primary config                      /Users/mac/.ccache/ccache.conf
secondary config      (readonly)    /usr/local/Cellar/ccache/3.3.4_1/etc/ccache.conf
cache hit (direct)                 14378
cache hit (preprocessed)            1029
cache miss                          7875
cache hit rate                     66.18 %
called for link                       61
called for preprocessing              48
compile failed                         2
preprocessor error                     4
can't use precompiled header          70
unsupported compiler option         2332
no input file                         11
cleanups performed                     0
files in cache                     35495
cache size                           1.3 GB
max cache size                       10.0 GB
   如果成功接入，就能看见 cache miss 不为0。因为第一次编译没有缓存，肯定是全 miss 的。接着编译第二遍，如果能看见 cache hit 的数字开始飙升，恭喜你，接入成功了。

CocoaPods 的处理
   如果你的项目不用 CocoaPods 来做包管理，那你已经完全接入成功了，不用执行下面的操作。

   因为 CocoaPods 会单独把第三方库打包成一个 Static Library（或者是Dynamic Framework，如果用了 use_frameworks!选项），所以 CocoaPods 生成的 Static Library 也需要把 Enable Modules 选项给关掉。但是因为 CocoaPods 每次执行 pod update 的时候都会把 Pods 项目重新生成一遍，如果直接在 Xcode 里面修改 Pods 项目里面的 Enable Modules 选项，下次执行pod update的时候又会被改回来。我们需要在 Podfile 里面加入下面的代码，让生成的项目关闭 Enable Modules 选项，同时加入 CC 参数，否则 pod 在编译的时候就无法使用 CCache 加速：

post_install do |installer_representation|
  installer_representation.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      #关闭 Enable Modules
      config.build_settings['CLANG_ENABLE_MODULES'] = 'NO'
      
      # 在生成的 Pods 项目文件中加入 CC 参数，路径的值根据你自己的项目来修改
      config.build_settings['CC'] = '$(PODS_ROOT)/../ccache-clang' 
    end
  end
end
   需要注意的是，如果你使用的某个 Pod 引用了系统框架，例如AFNetworking引用了System Configuration，你需要在你自己项目的Build Phrase -> Link Binary With Libraries里面代为引入，否则你编译时可能会收到 Undefined symbols xxx for architecture yyy一类的错误。有点回到了原始时代的感觉，但考虑到编译速度的极大提升，这一点代价可以接受。
可能需要重新引入的库
可能需要重新导入的系统库
集成问题排查
   重点关注日志文件的输出和ccache -s 命令的统计，如果在日志中看到了 unsupported compiler option -fmodules 这样的字眼，就是你的 Enable Modules 没有关掉了，根据前面的步骤仔细检查。其他问题，参考官方文档的 Troubleshooting。

进一步的优化
移除 Precompiled Header File
   PCH 的内容会被附加在每个文件前面，而 CCache 是根据文件内容的 MD4 摘要来查找缓存的，因此当你修改了 PCH 或者 PCH 引用到的头文件的内容时，会造成全部缓存失效，只能全体重新编译。CCache 在首次编译的时候因为需要更新缓存，会造成编译时间变长差不多一倍。因此如果 PCH 或者 PCH 引入的文件被频繁修改的话，缓存就会频繁地 miss，这种情况下还不如不用 CCache。

   为了避免以上这种情况，我建议在 PCH 里面尽量少引入头文件，只保留比较少更改的系统框架和第三方类库的头文件。最好是把 PCH 彻底删除，反正苹果现在也不建议使用 PCH 了，Xcode 新建的项目默认都是不带 PCH 的。

在团队内部共享缓存文件夹
   这个优化方式我尝试过，最终效果不是很好，因此没有采用。CCache 的官方文档中有一段关于共享缓存文件夹的说明，描述了如何修改 CCache 的配置，让编译缓存能够在多台电脑之间公用，理论上只要其中一个人编译过的文件其他人就能直接下载到了，节约了整个团队的时间。因为 Buck 也有类似的机制，我觉得值得尝试一下，便在公司局域网内搭建了一个 OwnCloud 网盘，让大家把自己电脑上的 CCache 缓存目录放上去共享。虽然试验是成功了，但是实际效果并不好。因为同步在多台电脑上大小达到几个G的缓存目录，需要在后台进行很多文件的对比和传输的工作，在编译的同时进行这些操作会耗费不少计算资源，反而会拖慢编译速度。加上移除掉 PCH 后，其实缓存的命中率已经相当可观了，不太需要通过共享缓存来进一步提高缓存命中率，所以我最后放弃了共享缓存这个想法。如果你对缓存命中率还是不满意的话，可以考虑往这个方向尝试一下。

总结
   通过集成 CCache，我们的项目在 Xcode 里面的打包（在菜单里面选择 Product -> Archive）时间从10分钟减少到了3分钟左右，大概有3倍的提升，成果喜人。集成的过程其实很简单，我从开始尝试到集成成功总共就花了两个小时。如果你也被过长的编译时间困扰，建议尝试一下。

补充：比较笨重但方便高效的实施方法（硬盘空间够多）
将项目拷贝几份分别以分支名或功能命名，将几个项目文件夹都导入到Tower或sourcetree中，在每个文件下切换分支，一个文件夹下固定只有1个分支，每次切换分支，只切换文件夹即可，完全不受其他分支的影响。在实际开发中这个方法，虽然笨拙，但是也是相对来说，高效的方法。

ccache - 让Xcode编译速度飞起来
今天来介绍一个小工具ccache，其可以提高xcode的编译速度。说起缘由，是因为我的苹果电脑配置比较低，而每次开发调试或测试打包都需要编译工程，虽然项目工程代码量不算大，但是编译的时间还是很长，尤其是修改了头文件或者Archive打包时，看着进度条像蜗牛在爬一样，心里都有小动物在奔腾......

好在遇到了ccache，其原理是通过把项目的源文件用ccache编译器编译，然后缓存编译生成的信息，从而在下一次编译时，利用这个缓存加快编译的速度，目前支持的语言有：C、C++、Objective-C、Objective-C++，但是如果找不到ccache编译器，那么还是会选择clang编译器来编译源文件。下面介绍一下具体的应用过程：

添加ccache脚本
下面是ccache的编译脚本，命名为：ccache-clang，需要添加到工程根目录，ccache就是通过这个脚本来选择编译器的，该脚本的详细介绍如下：

第1行：指定这是一个bash脚本

第2行：type -p ccache判断是否存在ccache命令，/dev/null是空设备文件，2>&1是把标准错误流重定向到标准输出流，所以整行的作用是先判断命令是否存在，如果不存在就把标准错误流重定向成标准输出流后，再重定向到空文件，这样错误就不会在控制台上打印出来了

第3行：设置最大的缓存

第4行：设置源文件的编译模式，默认是true，ccache会先处理源文件，如果缓存没有命中，就编译源文件；而如果是false，就会在缓存没有命中时，不是直接编译源文件，而是编译处理后的文件，但是这可能会有问题，因为不同的编译器，预处理后的文件内容不完全相同

第5行：设置为true，表明ccache直接利用缓存目录下的文件，而不是拷贝后的文件，这样可以加快编译速度，默认是false

第6行：设置提高缓存命中率，忽略__FILE__、DATE、__TIME__等宏，也不检查文件的修改和创建时间是否是最新的等等

第9行：指定日志文件的路径

第10行：执行/usr/bin/clang命令，"$@"是指所有参数

第12行：执行系统默认的clang命令，"$@"是指所有参数

#!/bin/sh
if type -p ccache >/dev/null 2>&1; then
    export CCACHE_MAXSIZE=10G
    export CCACHE_CPP2=true
    export CCACHE_HARDLINK=true
    export CCACHE_SLOPPINESS=file_macro,time_macros,include_file_mtime,include_file_ctime,file_stat_matches
  
    # 指定日志文件路径到桌面，等下排查集成问题有用，集成成功后删除，否则很占磁盘空间
    export CCACHE_LOGFILE='~/Desktop/CCache.log'
    exec ccache /usr/bin/clang "$@"
else
    exec clang "$@"
fi
如果你的代码或者三方库里的代码中有C++文件，则需要把脚本命名为：ccache-clang++，同时，脚本中的clang也需要修改为clang++，如下：

#!/bin/sh
if type -p ccache >/dev/null 2>&1; then
  export CCACHE_MAXSIZE=10G
  export CCACHE_CPP2=true
  export CCACHE_HARDLINK=true
  export CCACHE_SLOPPINESS=file_macro,time_macros,include_file_mtime,include_file_ctime,file_stat_matches
  
  # 指定日志文件路径到桌面，等下排查集成问题有用，集成成功后删除，否则很占磁盘空间
  export CCACHE_LOGFILE='~/Desktop/CCache.log'
  exec ccache /usr/bin/clang++ "$@"
else
  exec clang++ "$@"
fi
配置Xcode项目
1.添加一个CC常量

在项目的Build Settings里，添加一个常量：CC，值为脚本的完整路径：$(SRCROOT)/ccache-clang(脚本在根目录下)

图1

添加CC常量

图2

因为ccache不支持Clang Modules，所以需要关闭项目的Modules选项，如果你的工程里有用的@import UIKit等，那么现在需要替换为#import <UIKit/UIKit>，这是因为关闭Moduels后，Xcode不会再自动导入模块了，对于其他的模块，你还需要在Linked Frameworks and Libraries里手动导入所需模块。

配置Pod项目
如果项目中用到了CocoaPods，还需要设置Pod工程，因为Pod工程也需要关闭Modules选项，我们可以按照修改Xcode项目的方法来修改Pod工程的modules配置，但是每次pod update会把Pod工程重新生成，Modules选项又被改回去了，所以我们直接在Podfile里加入下面的代码，让Pod工程在生成的时候就关闭Modules选项，同时加入CC常量，就可以在编译时用缓存加速了。

但是，由于我们关闭了modules选项，如果某个Pod工程用到了系统的框架，则需要按照Xcode工程的方法添加到对应的Pod工程里，否则会提示Undefined symbols xxx for architecture arm7等等，尽管每次更新Pod后，都需要重新添加所需的框架，但是考虑到编译速度的提升，而Pod不会经常更新，所以也不是很麻烦。

post_install do |installer_representation|
  installer_representation.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      #关闭 Enable Modules
      config.build_settings['CLANG_ENABLE_MODULES'] = 'NO'
      
      # 在生成的 Pods 项目文件中加入 CC 参数，路径的值根据你自己的项目来修改
      config.build_settings['CC'] = '$(PODS_ROOT)/ccache-clang' 
    end
  end
end
应用ccache
设置完成后，就可以利用ccache了，首次因为还没有缓存，要添加缓存，所以编译的时间会比没有用ccache要多一会儿，但是从第二次之后，会有缓存命中，就可以加快编译速度了，多次之后，可以明显感觉到，编译的速度快了许多，一般至少了加快一倍以上，我们也可以用命令来查看ccache -s的缓存的命中情况：

图3

可以看到，现在的缓存命中率是53.01%，以前打包需要10分钟，现在3分钟搞定，喝茶的时间又多了，是不是很开森，^_^。

通过添加ccache，项目的编译速度得到了极大的提升，对于需要花费很长时间进行编译的项目，是十分值得的。
如何将 iOS 项目的编译速度提高5倍

ccache — a fast C/C++ compiler cache

ccache 让你的编译时间飞起来

linux中shell变量#,@,0,1,$2的含义解释

