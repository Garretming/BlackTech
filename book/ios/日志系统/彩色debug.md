CocoaLumberjack可以带颜色Log，具体的好处嘛，谁用谁知道，:]

具体步骤如下：

1. 安装XcodeColors插件
下载地址：https://github.com/robbiehanson/XcodeColors

安装方法：
下载并解压缩XcodeColors-master.zip
打开XcodeColors项目，编译项目可以自动将插件安装至~/Library/Application Support/Developer/Shared/Xcode/Plug-ins/XcodeColors.xcplugin
重新启动Xcode
再次打开XcodeColors项目
运行TestXcodeColors测试插件是否安装成功
2. 下载CocoaLumberjack开源框架
下载地址：https://github.com/CocoaLumberjack/CocoaLumberjack

3. 新建项目，将CocoaLumberjack拖入项目中
4. 创建Common.h
#ifdef DEBUG
static const int ddLogLevel = LOG_LEVEL_VERBOSE;
#else
static const int ddLogLevel = LOG_LEVEL_OFF;
#endif
5. 在xxx-Prefix.pch中添加Common.h的引入
#import "Common.h"
6. 实例化DDLog
在- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions

方法中设置DDLog

// 实例化 lumberjack
[DDLog addLogger:[DDTTYLogger sharedInstance]];
// 允许颜色
[[DDTTYLogger sharedInstance] setColorsEnabled:YES];
使用方法
lumberjack提供了四种Log方法

DDLogError(@"错误信息"); // 红色
DDLogWarn(@"警告"); // 橙色
DDLogInfo(@"提示信息"); // 默认是黑色
DDLogVerbose(@"详细信息"); // 默认是黑色
其他
如果要修改Log输出的颜色可以使用如下代码：

[[DDTTYLogger sharedInstance] setForegroundColor:[UIColor blueColor] backgroundColor:nil forFlag:LOG_FLAG_INFO];