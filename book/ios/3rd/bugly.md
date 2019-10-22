# iOS腾讯Bugly使用



项目上线后总结了一下Bugly分享给大家

首先进入Bugly官网：[https://bugly.qq.com/v2/](https://link.jianshu.com/?t=https://bugly.qq.com/v2/)

点击立即接入，用qq登陆后点击我的产品，新建一个产品，然后填写产品信息，保存

然后将Bugly集成到项目中，这里我用的是cocoapods 集成的Bugly

pod 'Bugly'

然后在工程中初始化Bugly，一句代码搞定

![](https://upload-images.jianshu.io/upload_images/2427846-0bc3eea36894e270.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

APPID是必填的，在我的产品中点击设置获取

  


![](https://upload-images.jianshu.io/upload_images/2427846-849aee3ab48f1641.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

![](https://upload-images.jianshu.io/upload_images/2427846-a5c42b3c63ba23d4.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

![](https://upload-images.jianshu.io/upload_images/2427846-cce02e10b65d44c3.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

配置完成之后运行出现bug后就可以捕获异常了，在崩溃分析中查看，但是我们只看到了在哪个方法里里报错，并不知道崩溃具体在哪一行，所以我们还要配置符号表

关于符号表官网有详细介绍如何使用： [符号表](https://link.jianshu.com/?t=https%3A%2F%2Fbugly.qq.com%2Fdocs%2Fuser-guide%2Fsymbol-configuration-ios%2F)

下面我再总结一下：

上传符号表有两种方式，分别是自动跟手动：

**自动配置**：不需要java运行环境，在脚本里面填写相关信息， 直接在Xcode编译执行脚本即可，官网上有写，非常方便简单，但在编译的时候比较慢

  


**重点讲下手动配置：**

官方的符号表工具iOS文档版­使用指南不是很通俗易懂，下面我再写一个更直观的教程，方便大家阅读。

**1 配置环境**

 点击[Java运行环境](https://link.jianshu.com/?t=http://www.oracle.com/technetwork/cn/java/javase/downloads/jre7-downloads-1880261.html)下载\(JRE或JDK版本需要&gt;=1.6，我下的是9.0.4\) 。

安装过后,查看是否安装成功，打开终端,在终端输入"java -version"\(这是查看运行环境的版本号\),运行结果如图所示:

![](https://upload-images.jianshu.io/upload_images/2427846-5d085ec0e524a1a8.png?imageMogr2/auto-orient/strip|imageView2/2/w/1094/format/webp)

**2 获取dSYM文件**

dSYM文件是指具有调试信息的目标文件,在Products里面右击 Show in Finder

![](https://upload-images.jianshu.io/upload_images/2427846-9cda2b62b3ff439d.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

  


如图所示，如果编译后没有dSYM文件说明是Dug编译的，如果要在Debug环境也能成dSYM文件，所以要做如下设置:

![](https://upload-images.jianshu.io/upload_images/2427846-931996e2f206c41b.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

  


![](https://upload-images.jianshu.io/upload_images/2427846-a424be6bf149f8e3.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

实际项目中我没有设置，因为我是通过打包后获取的dSYM文件

**3 生成符号表文件**

**3.1下载最新版**[**Bugly iOS符号表工具**](https://link.jianshu.com/?t=https%3A%2F%2Fbugly.qq.com%2Fv2%2Fsdk%3Fid%3D37f16cf0-2020-4e30-9e8d-0f7de59cfe94)**  
**

**  
**

![](https://upload-images.jianshu.io/upload_images/2427846-b4ba58074f9dff24.png?imageMogr2/auto-orient/strip|imageView2/2/w/410/format/webp)

3.2 选一个位置创建一个文件夹，将"buglySymboliOS.jar"放入文件夹里面 ，我自己是在桌面创建了"testBugly",然后将"buglySymboliOS.jar"放入进去了

3.2 最后使用JAR包跟dSYM在终端生成符号表文件   在终端执行以下命令:

java -jar jar包路径 -i dSYM文件路径

![](https://upload-images.jianshu.io/upload_images/2427846-75cf6314f0c59166.png?imageMogr2/auto-orient/strip|imageView2/2/w/582/format/webp)

最终符号表文件将生成在dSYM文件所在目录下

![](https://upload-images.jianshu.io/upload_images/2427846-baced30bdb844fb0.png?imageMogr2/auto-orient/strip|imageView2/2/w/372/format/webp)

3.4上传符号表到到我产品。如图:

![](https://upload-images.jianshu.io/upload_images/2427846-b834c087e3f3b432.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

之前用自动符号表生成了一些，所以符号表文件有点多。

最后就可以在项目中愉快的看到bug出现在哪个类哪一行代码上了

![](https://upload-images.jianshu.io/upload_images/2427846-223e10f040a46c03.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

26人点赞

[日记本](https://www.jianshu.com/nb/5014389)

  


