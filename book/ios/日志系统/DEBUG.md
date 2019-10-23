iOS: 如何在工程中设置 DEBUG 模式？
在APP 开发中，有时需要做一些模拟数据， 这时候，就得设置一个 Debug 开关， 当发布时，再把这个 Debug 关掉。

具体应用如下：..


打开DEBUG 模式： DEBUG = 1   

关掉DEBUG 模式：  DEBUG =0 

#if DEBUG

    

      ......  模拟数据     



#else

   

      ... 真实数据  



#endif

