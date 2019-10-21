# 解决iOS11以下系统WKWebView崩溃

2019.05.31 15:33:29

字数 220

阅读 301

# 问题1描述：

老版代码WKWebView存在内存泄漏，控制器一直没有dealloc，导致每次访问都内存都在增加

# 问题原因

在WKWebView只有：addScriptMessageHandler 方法，没有添加移除方法，应该添加：removeScriptMessageHandlerForName的方法。问题解决

# 问题2描述

在添加完removeScriptMessageHandlerForName之后，控制器开始走dealloc方法了，但是在iOS11以下系统上crash.

# 问题解决思路：

1:看崩溃日志

  


![](https://upload-images.jianshu.io/upload_images/1839607-7259b5a3742fcdc3.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

日志.jpg

  


这个崩溃日志没有关键信息，需要找到关键信息所以在main函数中添加了这样的代码，查看关键信息：

```
 @try {
            @autoreleasepool
            {
                return UIApplicationMain(argc, argv, nil, NSStringFromClass([AppDelegate class]));
            }
        }
        @catch (NSException* exception)
        {
            NSLog(@"Exception=%@\nStack Trace:%@", exception, [exception callStackSymbols]);
        }
```

可以查看到信息是这样的：

  


![](https://upload-images.jianshu.io/upload_images/1839607-f3b575e6fdb1ef13.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

崩溃日志.jpg

  


根据日志分析可以看出来是因为：有一个observers在控制器dealloc的时间没有释放引起的。完美解决。

