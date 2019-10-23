利用NSLogger和CocoaLumberjack打造日志系统（异常捕捉）
2017年06月06日 17:58:00 weixin_33860147 阅读数：0
前言
最近刚接手一个新项目，被分派到一个日志功能的需求，我们的需求是把日志记录到本地，然后让用户上传到服务端，我分别尝试了用NSLogger和CocoaLumberjack完成，下面说下具体过程。

过程
** NSLogger**
github地址
NSLogger的导入十分简单，以下是github上的Installation

Step 1. Download the NSLogger desktop app on your Mac.
Step 2. Add the NSLogger framework to your project.
Step 3. There is no step 3…

NSLogger在mac端有一个专门查看日志的客户端软件，可在github上下载。
而在客户端中保存的日志格式为.rawnsloggerdata。LoggerSetBufferFile这句代码让你设置日志保存的位置。如下：

NSString *cacheDirectory = [NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES) objectAtIndex:0];  
NSString *logPath = [cacheDirectory stringByAppendingPathComponent:@"log.rawnsloggerdata"];  
LoggerSetBufferFile(NULL, (__bridge CFStringRef)logPath); 
导入框架后，为了方便调用，可以按照自己的想法先定义宏定义

#define NSLog(...)  LogMessageF(__FILE__, __LINE__, __FUNCTION__, @"NSLog", 0, __VA_ARGS__)
下面只要在你想打印日志的地方加入NSLog()即可。

需要注意的是：当电脑和测试机处于同一个局域网内，且NSLogger Viewer开启时，NSLogger Viewer会将手机客户端运行时的日志实时显示，而此时这部分日志是不会写入手机客户端本地的，只有NSLogger Viewer没开启监控，日志才会写入本地，这点要注意！！！

另外，NSLogger支持多种数据类型，如文件，图片，文字等等，有需要同学可以深入研究下。

因为NSLogger只能把日志保存.rawnsloggerdata格式，并且只能在mac上用相应客户端查看，不符合我们的需求，于是，我用了另一个框架-CocoaLumberjack。

** CocoaLumberjack**
github地址
导入框架可参考这篇文章,写得不错，下面也根据我自身的需求大概说下：

首先说下CocoaLumberjack的日志级别：

LOG_LEVEL_ERROR：如果设置为LOG_LEVEL_ERROR，仅仅能看到Error相关的日志输出。
LOG_LEVEL_WARN：如果设置为LOG_LEVEL_WARN，能看到Error、Warn相关的日志输出。
LOG_LEVEL_INFO：如果设置为LOG_LEVEL_INFO，能够看到Error、Warn、Info相关的日志输出。
LOG_LEVEL_DEBUG：如果设置为LOG_LEVEL_DEBUG，能够看到Error/Warn/Info/Debug相关的日志输出。
LOG_LEVEL_VERBOSE：如果设置为LOG_FLAG_VERBOSE，能够看到Error/Warn/Info/Debug/Verbose相关日志输出。
LOG_LEVEL_OFF:不输出日志

CocoaLumberjack记录日志有几种方式，可以根据自己的需求选择是否导入
DDASLLogger（发送日志语句到苹果的日志系统，以便它们显示在Console.app上）
DDTTYLoyger（发送日志语句到Xcode控制台，如果可用）
DDFIleLoger（把日志语句发送至文件）
因为我只需要把日志发送控制台和记录在文件，所以我只导入了DDTTYLoyger和DDFIleLoger

在pch头文件设置全局日志等级

static const DDLogLevel ddLogLevel = DDLogLevelVerbose;

DDLogLevel 定义了全局的 log 等级，DDLogFlag 是我们打 log 时设定的 log 等级，CocoaLumberjack 会比较两者，如果 flag 低于 level，则不会打 log：

//在appdelegate中初始化
    //发送日志语句到Xcode控制台
    [DDLog addLogger:[DDTTYLogger sharedInstance]];
    //把日志语句发送至文件
    DDFileLogger *fileLogger = [[DDFileLogger alloc] init];
    fileLogger.rollingFrequency = 60 * 60 * 24; // 24 hour rolling
    fileLogger.logFileManager.maximumNumberOfLogFiles = 7;
    [DDLog addLogger:fileLogger withLevel:DDLogLevelError];

在实际应用中我定义了两个不同日志等级的宏

//INFO级别
#define HZLogInfo(format, ...) DDLogInfo((@"[%@][Line:%d]:" format), [[NSString stringWithUTF8String:__FILE__] lastPathComponent], __LINE__, ## __VA_ARGS__)
//Error级别
#define HZLogError(format, ...) DDLogError((@"[%@][Line:%d]:" format), [[NSString stringWithUTF8String:__FILE__] lastPathComponent], __LINE__, ## __VA_ARGS__)
解释下上面代码：
我设置全局日志等级为DDLogLevelVerbose，可打印Error/Warn/Info/Debug/Verbose相关等级的日志，当然这里还可以根据debug和release设置不同的等级。

另外，导入DDTTYLogger没设置level，这里会默认打印全部等级日志，而DDFileLogger我设置了DDLogLevelError等级，所以只有error等级日志才能写入文件。

所以我定义的两句宏：
HZLogInfo写入的是INFO级别的日志，所以这类日志只能显示在控制台，而不能写入文件。
HZLogError是ERROR级别日志，所以这类日志不仅显示在控制台，还可以写入文件。
当然各位可以根据自己需求而定，CocoaLumberjack记录的本地日志格式为.log格式，上传到服务器时不需特定在mac端观看，满足我们的需求。

另外，我的需求中还需要捕获异常并写入日志，这篇异常捕捉的文章写得十分详细，推荐给大家。要注意的是，使用 NSUncaughtExceptionHandler 捕获 NSException，后注册的NSUncaughtExceptionHandler会把前面注册的handler覆盖，在我们的项目中就有这样的问题。正确的做法是利用NSGetUncaughtExceptionHandler拿到上一个注册的Handler，处理完自己的Handler后再把exception传给上一个Handler。示例如下

static NSUncaughtExceptionHandler *previousUncaughtExceptionHandler;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
   //保存之前的Handler
   previousUncaughtExceptionHandler = NSGetUncaughtExceptionHandler();
   // 将下面C函数的函数地址当做参数
  NSSetUncaughtExceptionHandler(&UncaughtExceptionHandler);
   return YES;
}

void UncaughtExceptionHandler(NSException *exception){
   // 错误reason
    NSString *reason = [exception reason];
    // exception name
    NSString *name = [exception name];
    //异常的堆栈信息
    NSArray *stackArray = [exception callStackSymbols];
    //拼接错误信息
    NSString *exceptionInfo = [NSString stringWithFormat:@" Exception reason: %@\nException name: %@\nException stack:%@", reason , name , stackArray];
   //在此处理我们自己的Handler

    //调用之前注册的Handler
    previousUncaughtExceptionHandler(exception);
}

NSSetUncaughtExceptionHandler()函数指针的恶意覆盖的问题就解决了。参考文章

结束
学习之路，与君共勉。