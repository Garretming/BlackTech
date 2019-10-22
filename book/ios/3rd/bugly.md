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

关于符号表官网有详细介绍如何使用： [符号表](https://link.jianshu.com/?t=https%3A%2F%2Fbugly.qq.com%2Fdocs%2Fuser-guide%2Fsymbol-configuration-ios%2F)

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

3.2 最后使用JAR包跟dSYM在终端生成符号表文件   在终端执行以下命令:

java -jar jar包路径 -i dSYM文件路径

![](https://upload-images.jianshu.io/upload_images/2427846-75cf6314f0c59166.png?imageMogr2/auto-orient/strip|imageView2/2/w/582/format/webp)

最终符号表文件将生成在dSYM文件所在目录下

![](https://upload-images.jianshu.io/upload_images/2427846-baced30bdb844fb0.png?imageMogr2/auto-orient/strip|imageView2/2/w/372/format/webp)

3.4上传符号表到到我产品。如图:

![](https://upload-images.jianshu.io/upload_images/2427846-b834c087e3f3b432.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

之前用自动符号表生成了一些，所以符号表文件有点多。

最后就可以在项目中愉快的看到bug出现在哪个类哪一行代码上了

![](https://upload-images.jianshu.io/upload_images/2427846-223e10f040a46c03.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

# iOS 集成 Bugly 二三事

[Bugly 官网](https://bugly.qq.com/v2/index)

> 腾讯Bugly，为移动开发者提供专业的异常上报和运营统计，帮助开发者快速发现并解决异常，同时掌握产品运营动态，及时跟进用户反馈。

最近 iOS 项目中集成了 Bugly ，集成该框架的过程中，90%的问题通过仔细阅读[Bugly 官方文档](https://bugly.qq.com/docs/user-guide/instruction-manual-ios/?v=20170912151050)都可以解决。

💡 本文并不会教你如何注册申请 Bugly 帐号，也不会教你如何集成 Bugly SDK，因为官方文档是最权威的，这里只是记录几个注意点（传说中的坑！）。

## 初始化 Bugly 的注意点

### 方式一，最简单

在工程`AppDelegate.m`的`application:didFinishLaunchingWithOptions:`方法中初始化：

```
#import "AppDelegate.h"
#import 
<
Bugly/Bugly.h
>


// Bugly 帐号中创建产品后，产品信息中的 AppId
static NSString *const KBuglyAppId = @"**********"; 

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [Bugly startWithAppId:KBuglyAppId];
    return YES;
}
```

### 方式二，官方文档中的"高级功能"

Bugly支持读取`Info.plist`文件读取SDK初始化参数，可配置的参数如下：

```
-
 Appid

-
 Key
:
 BuglyAppIDString

-
 Value
:
 字符串类型

-
 渠道标识

-
 Key
:
 BuglyAppChannelString

-
 Value
:
 字符串类型

-
 版本信息

-
 Key
:
 BuglyAppVersionString

-
 Value
:
 字符串类型

-
 开启Debug信息显示

-
 Key
:
 BuglyDebugEnable

-
 Value
:
 BOOL类型
```

我们设置`Info.plist`文件如下：

![](https://upload-images.jianshu.io/upload_images/2648731-3887c294e671aa44.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/928/format/webp)

image

如下初始化方式，则会读取`Info.plist`内添加的key-value配置进行SDK初始化：

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // 读取Info.plist中的参数初始化SDK
    [Bugly startWithAppId:nil];
    return YES;
}
```

以上方式初始化 Bugly 确实没问题，可是默认的`BuglyConfig`还有几个监控开关没开，我也想顺便开启一下：

```
// 可能存在问题的代码
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    BuglyConfig *config = [[BuglyConfig alloc] init];
    config.blockMonitorEnable = YES; // 卡顿监控开关，默认关闭
    config.blockMonitorTimeout = 5;
    config.unexpectedTerminatingDetectionEnable = YES; // 非正常退出事件记录开关，默认关闭

    // 读取Info.plist中的参数初始化SDK
    [Bugly startWithAppId:nil config:config];

    return YES;
}
```

⚠️ 注意，这样初始化就会有问题，如果配置了`Info.plist`字段，又在初始化时传入了自定义的`BuglyConfig`实例，那么在`Info.plist`中配置的`BuglyAppChannelString`、`BuglyAppVersionString`、`BuglyDebugEnable`会因为被覆盖而失效。

### 方式三，自定义配置

如果需要自定义配置`BuglyConfig`实例，这里就不建议不同时配置`Info.plist`字段（或者可以只配置`BuglyAppIDString`字段）：

完整代码：

```
#import "AppDelegate.h"
#import 
<
Bugly/Bugly.h
>


static NSString *const KBuglyAppId = @"**********";

@implementation AppDelegate

#pragma mark - UIApplicationDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    [self p_configureForBugly]; 

    return YES;
}

#pragma mark - Private

- (void)p_configureForBugly {
    BuglyConfig *config = [[BuglyConfig alloc] init];
    config.channel = @"App Store";
    config.blockMonitorEnable = YES; // 卡顿监控开关，默认关闭
    config.blockMonitorTimeout = 5;
    config.unexpectedTerminatingDetectionEnable = YES; // 非正常退出事件记录开关，默认关闭
    config.delegate = self;

#ifdef DEBUG
    config.debugMode = YES; // debug 模式下，开启调试模式
    config.reportLogLevel = BuglyLogLevelVerbose; // 设置打印日志级别
#else
    config.debugMode = NO; // release 模式下，关闭调试模式
    config.reportLogLevel = BuglyLogLevelWarn; // 设置自定义日志上报的级别，默认不上报自定义日志
#endif

    [Bugly startWithAppId:KBuglyAppId config:config];
}
```

⚠️ 如果你配置完 Bugly 之后，

```
BLYLogError(fmt, ...)
BLYLogWarn(fmt, ...)
BLYLogInfo(fmt, ...)
BLYLogDebug(fmt, ...)
BLYLogVerbose(fmt, ...)
```

如上的日志不会在控制台输出，或者部分类型日志不会输出，那你应该注意到需要设置这段代码：

```
#ifdef DEBUG
    config.debugMode = YES; // debug 模式下，开启调试模式
    config.reportLogLevel = BuglyLogLevelVerbose; // 设置打印日志级别
#else
    config.debugMode = NO; // release 模式下，关闭调试模式
    config.reportLogLevel = BuglyLogLevelWarn; // 设置自定义日志上报的级别，默认不上报自定义日志
#endif
```

## 关于 SDK 回调问题

`BuglyConfig.h`文件中还有一个可以遵守的协议`BuglyDelegate`用于在系统崩溃时可以同时上传自定义数据。

```
@protocol BuglyDelegate 
<
NSObject
>


@optional
/**
 *  发生异常时回调
 *
 *  @param exception 异常信息
 *
 *  @return 返回需上报记录，随异常上报一起上报
 */
- (NSString * BLY_NULLABLE)attachmentForException:(NSException * BLY_NULLABLE)exception;

@end
```

我遇到的问题是，出于代码清晰的目的，将应用初始化配置、第三方框架初始化配置、推送、分享相关的代码都放在分类中了：

![](https://upload-images.jianshu.io/upload_images/2648731-4453a2d2cb9ad751.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/582/format/webp)

image

并且在分类中遵守了`<BuglyDelegate>`协议，也实现了简单的回调方法：

```
- (NSString * BLY_NULLABLE)attachmentForException:(NSException * BLY_NULLABLE)exception {
    return @"需要上传的数据...";
}
```

正常情况下，应用发生崩溃后，Bugly 会立即上报异常，同时在「崩溃分析」-「跟踪数据」-「附件信息」中显示回调方法中上传的数据文件**crash\_attach.log**：

![](https://upload-images.jianshu.io/upload_images/2648731-a0e1ac5bf7d96730.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/1008/format/webp)

image

实际上把回调代码写在分类中时，应用发生崩溃时，并不会触发协议方法。所以**务必要把所有与 Bugly 初始化及回调代码写在**`AppDelegate.m`**文件中**。

最后，附上 Bugly 集成的完整正确代码示例：

```
#import "AppDelegate.h"
#import 
<
Bugly/Bugly.h
>


static NSString *const KBuglyAppId = @"**********";

@interface AppDelegate () 
<
BuglyDelegate
>


@end

@implementation AppDelegate

#pragma mark - UIApplicationDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    [self p_configureForBugly];

    return YES;
}

#pragma mark - Private

- (void)p_configureForBugly {
    BuglyConfig *config = [[BuglyConfig alloc] init];
    config.channel = @"App Store";
    config.blockMonitorEnable = YES; // 卡顿监控开关，默认关闭
    config.blockMonitorTimeout = 5;
    config.unexpectedTerminatingDetectionEnable = YES; // 非正常退出事件记录开关，默认关闭
    config.delegate = self;

#ifdef DEBUG
    config.debugMode = YES; // debug 模式下，开启调试模式
    config.reportLogLevel = BuglyLogLevelVerbose; // 设置自定义日志上报的级别，默认不上报自定义日志
#else
    config.debugMode = NO; // release 模式下，关闭调试模式
    config.reportLogLevel = BuglyLogLevelWarn;
#endif

    [Bugly startWithAppId:KBuglyAppId config:config];
}

#pragma mark - BuglyDelegate

- (NSString * BLY_NULLABLE)attachmentForException:(NSException * BLY_NULLABLE)exception {
    NSDictionary *dictionary = @{@"Name":exception.name,
                                 @"Reason":exception.reason};
    return [NSString stringWithFormat:@"Exception:%@",dictionary];
}

@end
```

> 过早的优化是万恶之源。——[高德纳](https://en.wikipedia.org/wiki/Donald_Knuth#Computer_Programming_as_art_.281974.29)

## 对依赖进行抽象化和封装

参考对 Flurry 的封装方法

```
#
import
<
Foundation/Foundation.h
>
/**
 封装 Flurry 埋点
 */
@interface
 HPInstrumentation 
:
 NSObject


+
(
void
)
startWithAPIKey
:
(
NSString 
*
)
apiKey
;
+
(
void
)
logEvent
:
(
NSString 
*
)
name
;
+
(
void
)
logEvent
:
(
NSString 
*
)
name withParams
:
(
NSDictionary 
*
)
params
;
+
(
void
)
logPageViewForTabBarController
:
(
UITabBarController 
*
)
vc
;
@end
#
import
 "HPInstrumentation.h"
#
import
 "Flurry.h"
@implementation
 HPInstrumentation


+
(
void
)
startWithAPIKey
:
(
NSString 
*
)
apiKey

{
[
Flurry startSession
:
apiKey
]
;
}
+
(
void
)
logEvent
:
(
NSString 
*
)
name

{
NSLog
(
@"
<
HPInst
>
 %@"
,
 name
)
;
[
Flurry logEvent
:
name
]
;
}
+
(
void
)
logEvent
:
(
NSString 
*
)
name withParams
:
(
NSDictionary 
*
)
params

{
NSLog
(
@"
<
HPInst
>
 %@ -
>
 %@"
,
 name
,
 params
)
;
[
Flurry logEvent
:
name withParameters
:
params
]
;
}
+
(
void
)
logPageViewForTabBarController
:
(
UITabBarController 
*
)
vc 
{
NSLog
(
@"
<
HPInst
>
 PV: %@"
,
[
vc class
]
)
;
[
Flurry logAllPageViewsForTarget
:
vc
]
;
}
@end
```

尝试对 Bugly 进行封装

```
#
import
<
Foundation/Foundation.h
>
/**
 对依赖进行抽象化和封装
 如果直接在项目中使用崩溃报告系统，那么埋点会分散在项目中的各个角落，不利于后期替换或更改。
 低耦合：增加一个中间层之后，可以随时对依赖的第三方框架进行切换，无须再去修改分散在各个类中的代码。
 */
@interface
 HQLInstrumentation 
:
 NSObject


+
(
void
)
logEvent
:
(
NSString 
*
)
name
;
+
(
void
)
logEvent
:
(
NSString 
*
)
name withParamenters
:
(
NSString 
*
)
parameters
;
@end
#
import
 "HQLInstrumentation.h"
#
import
<
Bugly/Bugly.h
>
@implementation
 HQLInstrumentation


+
(
void
)
logEvent
:
(
NSString 
*
)
name 
{
[
BuglyLog log
:
@"%@"
,
 name
]
;
}
+
(
void
)
logEvent
:
(
NSString 
*
)
name withParamenters
:
(
NSString 
*
)
parameters 
{
[
BuglyLog log
:
@"%@:%@"
,
name
,
parametersiOS 集成 Bugly 二三事
1
2017.11.15 00:55:02
字数 888
阅读 2287
Bugly 官网

腾讯Bugly，为移动开发者提供专业的异常上报和运营统计，帮助开发者快速发现并解决异常，同时掌握产品运营动态，及时跟进用户反馈。

最近 iOS 项目中集成了 Bugly ，集成该框架的过程中，90%的问题通过仔细阅读 Bugly 官方文档 都可以解决。

💡 本文并不会教你如何注册申请 Bugly 帐号，也不会教你如何集成 Bugly SDK，因为官方文档是最权威的，这里只是记录几个注意点（传说中的坑！）。

初始化 Bugly 的注意点
方式一，最简单
在工程AppDelegate.m的application:didFinishLaunchingWithOptions:方法中初始化：

#import "AppDelegate.h"
#import <Bugly/Bugly.h>

// Bugly 帐号中创建产品后，产品信息中的 AppId
static NSString *const KBuglyAppId = @"**********"; 

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    [Bugly startWithAppId:KBuglyAppId];
    return YES;
}
方式二，官方文档中的"高级功能"
Bugly支持读取 Info.plist 文件读取SDK初始化参数，可配置的参数如下：

- Appid
    - Key: BuglyAppIDString
    - Value: 字符串类型
- 渠道标识
    - Key: BuglyAppChannelString
    - Value: 字符串类型
- 版本信息
    - Key: BuglyAppVersionString
    - Value: 字符串类型
- 开启Debug信息显示
    - Key: BuglyDebugEnable
    - Value: BOOL类型
我们设置 Info.plist 文件如下：

image
如下初始化方式，则会读取Info.plist内添加的key-value配置进行SDK初始化：

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // 读取Info.plist中的参数初始化SDK
    [Bugly startWithAppId:nil];
    return YES;
}
以上方式初始化 Bugly 确实没问题，可是默认的 BuglyConfig 还有几个监控开关没开，我也想顺便开启一下：

// 可能存在问题的代码
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    BuglyConfig *config = [[BuglyConfig alloc] init];
    config.blockMonitorEnable = YES; // 卡顿监控开关，默认关闭
    config.blockMonitorTimeout = 5;
    config.unexpectedTerminatingDetectionEnable = YES; // 非正常退出事件记录开关，默认关闭

    // 读取Info.plist中的参数初始化SDK
    [Bugly startWithAppId:nil config:config];

    return YES;
}
⚠️ 注意，这样初始化就会有问题，如果配置了Info.plist字段，又在初始化时传入了自定义的 BuglyConfig 实例，那么在 Info.plist 中配置的 BuglyAppChannelString、BuglyAppVersionString、BuglyDebugEnable 会因为被覆盖而失效。

方式三，自定义配置
如果需要自定义配置 BuglyConfig 实例，这里就不建议不同时配置Info.plist字段（或者可以只配置BuglyAppIDString字段）：

完整代码：

#import "AppDelegate.h"
#import <Bugly/Bugly.h>

static NSString *const KBuglyAppId = @"**********";

@implementation AppDelegate

#pragma mark - UIApplicationDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    [self p_configureForBugly]; 

    return YES;
}

#pragma mark - Private

- (void)p_configureForBugly {
    BuglyConfig *config = [[BuglyConfig alloc] init];
    config.channel = @"App Store";
    config.blockMonitorEnable = YES; // 卡顿监控开关，默认关闭
    config.blockMonitorTimeout = 5;
    config.unexpectedTerminatingDetectionEnable = YES; // 非正常退出事件记录开关，默认关闭
    config.delegate = self;

#ifdef DEBUG
    config.debugMode = YES; // debug 模式下，开启调试模式
    config.reportLogLevel = BuglyLogLevelVerbose; // 设置打印日志级别
#else
    config.debugMode = NO; // release 模式下，关闭调试模式
    config.reportLogLevel = BuglyLogLevelWarn; // 设置自定义日志上报的级别，默认不上报自定义日志
#endif

    [Bugly startWithAppId:KBuglyAppId config:config];
}
⚠️ 如果你配置完 Bugly 之后，

BLYLogError(fmt, ...)
BLYLogWarn(fmt, ...)
BLYLogInfo(fmt, ...)
BLYLogDebug(fmt, ...)
BLYLogVerbose(fmt, ...)
如上的日志不会在控制台输出，或者部分类型日志不会输出，那你应该注意到需要设置这段代码：

#ifdef DEBUG
    config.debugMode = YES; // debug 模式下，开启调试模式
    config.reportLogLevel = BuglyLogLevelVerbose; // 设置打印日志级别
#else
    config.debugMode = NO; // release 模式下，关闭调试模式
    config.reportLogLevel = BuglyLogLevelWarn; // 设置自定义日志上报的级别，默认不上报自定义日志
#endif
关于 SDK 回调问题
BuglyConfig.h文件中还有一个可以遵守的协议 BuglyDelegate 用于在系统崩溃时可以同时上传自定义数据。

@protocol BuglyDelegate <NSObject>

@optional
/**
 *  发生异常时回调
 *
 *  @param exception 异常信息
 *
 *  @return 返回需上报记录，随异常上报一起上报
 */
- (NSString * BLY_NULLABLE)attachmentForException:(NSException * BLY_NULLABLE)exception;

@end
我遇到的问题是，出于代码清晰的目的，将应用初始化配置、第三方框架初始化配置、推送、分享相关的代码都放在分类中了：

image
并且在分类中遵守了 <BuglyDelegate> 协议，也实现了简单的回调方法：

- (NSString * BLY_NULLABLE)attachmentForException:(NSException * BLY_NULLABLE)exception {
    return @"需要上传的数据...";
}
正常情况下，应用发生崩溃后，Bugly 会立即上报异常，同时在「崩溃分析」-「跟踪数据」-「附件信息」中显示回调方法中上传的数据文件 crash_attach.log：

image
实际上把回调代码写在分类中时，应用发生崩溃时，并不会触发协议方法。所以务必要把所有与 Bugly 初始化及回调代码写在 AppDelegate.m 文件中。

最后，附上 Bugly 集成的完整正确代码示例：

#import "AppDelegate.h"
#import <Bugly/Bugly.h>

static NSString *const KBuglyAppId = @"**********";

@interface AppDelegate () <BuglyDelegate>

@end

@implementation AppDelegate

#pragma mark - UIApplicationDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    [self p_configureForBugly];

    return YES;
}

#pragma mark - Private

- (void)p_configureForBugly {
    BuglyConfig *config = [[BuglyConfig alloc] init];
    config.channel = @"App Store";
    config.blockMonitorEnable = YES; // 卡顿监控开关，默认关闭
    config.blockMonitorTimeout = 5;
    config.unexpectedTerminatingDetectionEnable = YES; // 非正常退出事件记录开关，默认关闭
    config.delegate = self;

#ifdef DEBUG
    config.debugMode = YES; // debug 模式下，开启调试模式
    config.reportLogLevel = BuglyLogLevelVerbose; // 设置自定义日志上报的级别，默认不上报自定义日志
#else
    config.debugMode = NO; // release 模式下，关闭调试模式
    config.reportLogLevel = BuglyLogLevelWarn;
#endif

    [Bugly startWithAppId:KBuglyAppId config:config];
}

#pragma mark - BuglyDelegate

- (NSString * BLY_NULLABLE)attachmentForException:(NSException * BLY_NULLABLE)exception {
    NSDictionary *dictionary = @{@"Name":exception.name,
                                 @"Reason":exception.reason};
    return [NSString stringWithFormat:@"Exception:%@",dictionary];
}

@end
过早的优化是万恶之源。——高德纳

对依赖进行抽象化和封装
参考对 Flurry 的封装方法

#import <Foundation/Foundation.h>

/**
 封装 Flurry 埋点
 */
@interface HPInstrumentation : NSObject

+(void)startWithAPIKey:(NSString *)apiKey;
+(void)logEvent:(NSString *)name;
+(void)logEvent:(NSString *)name withParams:(NSDictionary *)params;

+(void)logPageViewForTabBarController:(UITabBarController *)vc;

@end

#import "HPInstrumentation.h"
#import "Flurry.h"

@implementation HPInstrumentation

+(void)startWithAPIKey:(NSString *)apiKey
{
    [Flurry startSession:apiKey];
}

+(void)logEvent:(NSString *)name
{
    NSLog(@"<HPInst> %@", name);
    [Flurry logEvent:name];
}

+(void)logEvent:(NSString *)name withParams:(NSDictionary *)params
{
    NSLog(@"<HPInst> %@ -> %@", name, params);
    [Flurry logEvent:name withParameters:params];
}

+(void)logPageViewForTabBarController:(UITabBarController *)vc {
    NSLog(@"<HPInst> PV: %@", [vc class]);
    [Flurry logAllPageViewsForTarget:vc];
}

@end
尝试对 Bugly 进行封装

#import <Foundation/Foundation.h>

/**
 对依赖进行抽象化和封装
 如果直接在项目中使用崩溃报告系统，那么埋点会分散在项目中的各个角落，不利于后期替换或更改。
 低耦合：增加一个中间层之后，可以随时对依赖的第三方框架进行切换，无须再去修改分散在各个类中的代码。
 */
@interface HQLInstrumentation : NSObject

+ (void)logEvent:(NSString *)name;
+ (void)logEvent:(NSString *)name withParamenters:(NSString *)parameters;

@end

#import "HQLInstrumentation.h"
#import <Bugly/Bugly.h>

@implementation HQLInstrumentation

+ (void)logEvent:(NSString *)name {
    [BuglyLog log:@"%@", name];
}

+ (void)logEvent:(NSString *)name withParamenters:(NSString *)parameters {
    [BuglyLog log:@"%@:%@",name,parameters];
}

@end
相关框架
JJException - 保护 Objective-C 应用不闪退的框架。
KSCrash - iOS崩溃报告框架
PLCrashReporter - Reliable, open-source crash reporting for iOS and Mac OS X.
参考
Bugly 官方文档
简书：iOS崩溃异常处理(使用篇) @IUVO
简书：iOS集成Bugly异常上报 @逝水流无痕
简书：iOS-Bugly使用 @Caesar大帝归来
]
;
}
@end
```

### 相关框架

* [JJException](https://github.com/jezzmemo/JJException)
  * 保护 Objective-C 应用不闪退的框架。
* [KSCrash](https://github.com/kstenerud/KSCrash)
  * iOS崩溃报告框架
* [PLCrashReporter](https://www.plcrashreporter.org/)
  * Reliable, open-source crash reporting for iOS and Mac OS X.

### 参考

* [Bugly 官方文档](https://bugly.qq.com/docs/release-notes/release-ios-bugly/?v=20171109131920)
* [简书：iOS崩溃异常处理\(使用篇\) @IUVO](https://www.jianshu.com/p/4d32664dcfdb)
* [简书：iOS集成Bugly异常上报 @逝水流无痕](https://www.jianshu.com/p/846412365179)
* [简书：iOS-Bugly使用 @Caesar大帝归来](https://www.jianshu.com/p/7eecc1a4d2f9)



