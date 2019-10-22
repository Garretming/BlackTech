最近接触学习到了RAC\(ReactiveCocoa\)，RAC是函数式+响应式编程结合，首先得去理解何为响应式函数编程（FRP）。

    看了许多介绍，举一个最通俗易懂的例子——在命令式编程环境中， a = b+c表示将表达式的结果赋给 a，而之后改变 b 或 c的值不会影响 a。但在响应式编程中，a的值会随着 b或 c的更新而更新，意味着声明了一种绑定关系，b、c的变化会直接影响到a。

    之前在iOS工作中，类之间的传值，无非就是block、delegate代理、KVO、notification这几种方法。在RAC中，同样具备替代KVO、delegate代理、通知、UI target、计时器timer、数据结构等各种方法。依据响应式函数编程，RAC方法本身更加简洁明了，通过提供信号的方式（RACSignal）可以捕捉当前以及未来的属性值变化，而且无需持续观察和更新代码。可直接在block中将逻辑代码加入其中，使得代码紧凑，更加直观。

    先来介绍ObjC版本，使用cocoaPods在podfile中添加 pod 'ReactiveObjC', '~&gt; 3.1.0' ，然后pod install一下。在项目中\#import &lt;ReactiveObjC.h&gt;，建议放入pch头文件中。

    通过RAC提供的方法与系统提供的方法分别进行对比，先来感受下RAC的强大之处。

1. UIButton

![](https://upload-images.jianshu.io/upload_images/1243805-1ddc42adc855d346.png?imageMogr2/auto-orient/strip|imageView2/2/w/994/format/webp)

通过默认的Target-action创建点击动作

![](https://upload-images.jianshu.io/upload_images/1243805-14871cea4af39f7e.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

RAC创建Button点击事件与添加点击手势动作

  


在RAC的block代码块中，打印x的属性为当前self.testButton的相关信息。

  


![](https://upload-images.jianshu.io/upload_images/1243805-96be2ff0c89d19c5.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

2. KVO

KVO在使用时，必须在- \(void\)observeValueForKeyPath:\(NSString\*\)keyPath ofObject:\(id\)object change:\(NSDictionary \*\)change context:\(void\*\)context中实现针对KVO监听属性值变化的处理，而且对于KeyPath书写容易产生手写错误。在对应类dealloc时，KVO还必须要进行remove操作，否则会程序crash

![](https://upload-images.jianshu.io/upload_images/1243805-e903efbeb48e47e0.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

使用KVO监听UILable的text属性变化

在使用RAC代替KVO时，不仅能大大增加代码可读性，而且RACObserve\(&lt;\#TARGET\#&gt;, &lt;\#KEYPATH\#&gt;\)宏定义中keyPath可以代码提示出target中的属性成员变量，降低手写代码错误的可能性。

![](https://upload-images.jianshu.io/upload_images/1243805-71ea04cac2884982.png?imageMogr2/auto-orient/strip|imageView2/2/w/1170/format/webp)

使用RAC代替KVO监听属性变化

3. delegate代理

以UITextField为例，当需要对UITextField逻辑处理时，往往需要实现其各类代理方法，大大增加了代码量。当使用RAC之后

![](https://upload-images.jianshu.io/upload_images/1243805-fea36f28b944bcdd.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

使用RAC代替delegate实现方法

@selector方法选择器中键入要实现的代理方法，代理名称声明为对应的代理名称。block代码块中，当触发监听的代理方法时返回元组类型数据，与swift中的元组类型有所区别，此处的元组看起来更像是数组。

![](https://upload-images.jianshu.io/upload_images/1243805-f860ae18d48556ba.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

打印结果

4. Notification通知

![](https://upload-images.jianshu.io/upload_images/1243805-13a73de5a0a510e2.png?imageMogr2/auto-orient/strip|imageView2/2/w/1166/format/webp)

RAC通知使用

![](https://upload-images.jianshu.io/upload_images/1243805-939177c09f99de0a.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

RAC会将通知名以及userInfo相关信息返回至block中

5. 定时器timer

![](https://upload-images.jianshu.io/upload_images/1243805-6f32e9887d918369.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

6. 数组与字典

遍历元素

![](https://upload-images.jianshu.io/upload_images/1243805-6dab7655145d6512.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

RAC遍历字典、数组中的元素

![](https://upload-images.jianshu.io/upload_images/1243805-d9c155e4dc3b2991.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

RAC基本使用方法与流程

![](https://upload-images.jianshu.io/upload_images/1243805-141d598008e7f242.png?imageMogr2/auto-orient/strip|imageView2/2/w/1192/format/webp)

RAC基本使用方法与流程

    以上代码中，subscribeNext作用为订阅信号，可在该block中输入逻辑相关代码块。但当多个对象的逻辑存在于block中需要修改时，仅仅subscribeNext已不能满足需求。

RAC中信号的其它动作：

信号映射：map、flattenMap

信号过滤：filter、ignore、distinctUntilChanged

信号合并：combineLatest、reduce、merge、zipWith

信号连接：concat、then

信号操作时间：timeout、interval、dely

信号跳过：skip

信号取值：take、takeLast、takeUntil

信号发送顺序：donext、cocompleted

获取信号中的信号：switchToLatest

信号错误重试：retry

    在实际开发过程中，需要在RAC代码块中添加逻辑代码，避免不了引用当前类中的成员变量，那么需要在RAC方法外部写入以下代码：

@weakify\(self\)

    在RAC的block代码块内部写入：

@strongify\(self\)

![](https://upload-images.jianshu.io/upload_images/1243805-c9e04640fdd03384.png?imageMogr2/auto-orient/strip|imageView2/2/w/1166/format/webp)

以此来避免出现block的循环引用，至于为何要如此声明，稍后会在后续文章中一一说明。

  


    稍后会在后续的文章里继续介绍如何使用，以及RAC信号流程原理。demo代码放到GitHub上[demo链接](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FRoganZheng%2FReactiveObjC)

作者：我只不过是出来写写代码

  




  




  


著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

