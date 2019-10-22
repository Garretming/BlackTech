# use\_frameworks!和\#use\_frameworks!的区别

1

2018.07.24 12:24:58

字数 399

阅读 4247

1、用cocoapods 导入swift 框架到swift项目和OC项目都必须要 use\_frameworks!  
2、用动态库，必须要在Podfile文件中添加 use\_frameworks!

```
静态库
:
（静态链接库）
(
.a
)
在编译时会将库copy一份到目标程序中，编译完成之后，目标程序不依赖外部的库，也可以运行

缺点
:
 会使应用程序变大

动态库：（.dylib）编译时只存储了指向动态库的引用。可以多个程序指向这个库，在运行时才加载，不会使应用体积变大，但是运行时加载会损耗部分性能，并且依赖外部的环境，如果库不存在或者版本不正确则无法运行

Framework：实际上是一种打包方式，将库的二进制文件，头文件和有关的资源文件打包到一起，方便管理和分发。

```

\(1\)如果在Podfile文件里不使用 use\_frameworks! 则是会生成相应的 .a文件（静态链接库），通过 static libraries 这个方式来管理pod的代码。

\(2\)Linked:libPods-xxx.a包含了其它用pod导入的第三方框架的.a文件。

\(3\)如果使用了use\_frameworks! 则cocoapods 会生成相应的 .frameworks文件（动态链接库：实际内容为 Header + 动态链接库 + 资源文件），使用 dynamic frameworks 来取代 static libraries 方式。

\(4\)Linked:Pods\_xxx.framework包含了其它用pod导入的第三方框架的.framework文件。

use\_frameworks! -&gt; dynamic frameworks 方式 -&gt; .framework

# use\_frameworks! -&gt; static libraries 方式 -&gt; .a

```
(1)swift项目cocoapods 默认 use_frameworks!
(2)OC项目cocoapods 默认 #use_frameworks!

```

## 1、用cocoapods导入OC框架到swift项目

（1）\#use\_frameworks! 必须创建头文件，在头文件里面 \#import "xxx.h"  
（2）use\_frameworks! 如果有头文件，在头文件里面 \#import "xxx/xxx.h"，其它swift文件中用到不需要再import；如果没有头文件，则在每个需要用到的swift文件里 import xxx。

## 2、用cocoapods导入swift框架到swift项目

（1）必须use\_frameworks!  
（2）不需要头文件，在需要用到框架的swift文件里 import xxx

## 3、用cocoapods导入OC框架到OC项目

（1）\#use\_frameworks! 在需要用到的文件里 \#import "xxx.h"；也可以通过pch文件，用法类似swift中的头文件。  
（2）use\_frameworks! 与\(1\)类似，用法上没有区别。

总结：

```
（
1
）用swift项目考虑到会使用 OC 和 swift 两种第三方框架，所以Podfile中使用swift项目默认的 use_frameworks
!
 更为妥当，并且frameworks动态链接库具有一定的优势。

（
2
）可以建立一个Bridge头文件，用来
import
那些OC框架的
.
h文件：#
import
"xxx/xxx.h"
。或者不建头文件，像swift框架一样，直接在需要用到的swift文件中
import
 xxx。

```

11人点赞

[日记本](https://www.jianshu.com/nb/13156152)

  


