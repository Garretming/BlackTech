# iOS.11后的 iOS LaunchImage

开始

两种方法设置：

* LaunchScreen.storyboard

  1. 在LaunchScreen.storyboard中拖拽imageView并设置约束，勾选右侧Use as launch Screen
  2. 工程—General—App Icons and Launch Images选项中设置Launch Screen File为所制作的LaunchScreen.storyboard或者LaunchScreen.xib

* Assets.xcassets

  1. 设置LaunchImage
  2. 准备:  
     640 × 960，640 × 1136，750 × 1334，1242 × 2208，（横平需要2208 ×1242）

     1125x2436,1242x2688,828x1792

```
 iPhone Portrait iOS5,6\(1x:320 × 480 pixels, 2x:640 × 960 pixels, Retina 4:640 × 1136 pixels\)

 iPhone Portrait iOS7,9\(2x:640 × 960 pixels, Retina 4:640 × 1136 pixels\)



 iPhone Portrait iOS8,9\(Retina HD 5.5”:1242 × 2208 pixels, Retina HD 4.7”:750 × 1334 pixels\)

 iPhone Landscape iOS 8,9\(Retina HD 5.5”:2208 × 1242 pixels\)



 iPhone X Portrait iOS 11+ \(3x:1125 x 2436 pixels\)

 iPhone X Landscape iOS 11+\(Retina HD 5.5”:2208 × 1242 pixels\)



 iPhone XR Portrait iOS 12+ \(3x:1242 x 2688 pixels\)

 iPhone XS Max Portrait iOS 12+ \(3x:828x1792 pixels\)
```

1. 配置
   1. 工程—General—App Icons and Launch Images选项中设置Launch Image Source 为LaunchImage
   2. 取消勾选Use as Launch Screen
   3. 置空路径Launch Screen File

更新时间2018年10月07日

ps：最新LaunchImage尺寸图

![](https://img-blog.csdnimg.cn/20190107213242729.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L29aaHVpTWVuZzEyMw==,size_16,color_FFFFFF,t_70)[iOS--LaunchImage启动页设置及问题解决](https://www.cnblogs.com/sundaysgarden/p/9012847.html)

## **在Assets.xcassets中使用LaunchImage来设置启动图:**

#### 一.根据不同屏幕尺寸的需求设置不同的图片，可以参照下图：

```
  1.点击Image.xcassets 进入图片管理,然后右击,弹出"New Launch Image"

  2.右侧的勾选可以让你选择是否要对ipad,横屏,竖屏,以及低版本的ios系统做支持
```

1. 注意: 为适配 iPhone X, 图片尺寸为1125px\*2436px

![](https://upload-images.jianshu.io/upload_images/1376478-c3f5908f0284af94.png)

![](https://upload-images.jianshu.io/upload_images/1376478-aec35c7a420ef8d8.png)

#### 二.取消系统默认使用的LaunchScreen，首先你要取消Use as Launch Screen 的选中

![](https://upload-images.jianshu.io/upload_images/1376478-f1ebea8f62d407d5.png)

![](https://upload-images.jianshu.io/upload_images/1376478-b9318fb3decb0dd0.png)

#### 三.需要设置Launch Screen File

单击你整个项目名称,  选择General,就是这个.

![](https://upload-images.jianshu.io/upload_images/1376478-6d93491896b8b978.png)

在配置好以上之后启动页的图片就会使用LaunchImage中的图片了..

---

### **但是经过上述步骤之后，你觉得完全没有问题了，但是仍然无法显示LaunchImage。**

或者，你在多个模拟器上运行该程序，有的模拟器能够显示，有的模拟器不能显示。

这时候你可能会有3个选择：

1. 菜单－product－Clean－rebuild，也就是重新build程序。

2. 菜单－Xcode－preference－Locations－Derived data－open in Finder，然后删除其中的缓存文件，并重新build程序。

3.把App在模拟器上卸载掉，然后重新build。

4.reset模拟器

正常情况下，LaunchImage 应该会显示了。

---

### 如果真的真的还是不显示的话, 或者遇到5s真机测试时屏幕变小,且有上下两条黑道的话,那就是图片的问题,是否为jpeg转为png的呢?又或者是图片大小不对. 这是我遇到过的情况.



# Mac快速制作LaunchImage（App启动图片）



> 第一步：Keynote画图  
> 第二步：批量剪裁图片

#### 第一步：Keynote画图

![](https://upload-images.jianshu.io/upload_images/3128629-4346910e5827fedf.png?imageMogr2/auto-orient/strip|imageView2/2/w/160/format/webp)

![](https://upload-images.jianshu.io/upload_images/3128629-22771c90cfc4016b.png?imageMogr2/auto-orient/strip|imageView2/2/w/720/format/webp)

打开Keynote，选择“形状”里面的方框功能，画一个322 \* 570的框作为图标的底，然后在右边设计区填充背景颜色等等，可以很容易就做出渐变色等效果。  
然后加上公司logo、几个艺术字就差不多能用了。

为什么底大小要是322 \* 570呢？  
实际上任何大小都可以，只要看起来跟手机屏幕差不多就行，但是一会更改图片像素大小适配手机的时候，会有拉伸和压缩，这是一个中间值，太大按比例缩放电脑屏幕放不下，太小不好做设计。  
设计完启动图后，我们要用截图工具截图，截一个320 \* 568大小的图片保存，这样图片的像素是640 \* 1136的。  
而直接画320 \* 568的底截图时会发现少两个像素。

#### 第二步：批量剪裁图片

我没有发现制作LaunchImage的网站，所以我用的app。  
而好多app，比如Prepo，裁剪AppIcon免费，裁剪LaunchImage要内购收费。  
最终我用的这个：App Icon Gear

![](https://upload-images.jianshu.io/upload_images/3128629-cf4333f3c487b678.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

先选择功能，是AppIcon还是LaunchImage

![](https://upload-images.jianshu.io/upload_images/3128629-e604530643fb1e72.png?imageMogr2/auto-orient/strip|imageView2/2/w/1194/format/webp)

选择好后，把第一步设计好的图拖进左边的方框

![](https://upload-images.jianshu.io/upload_images/3128629-9d8a5ce436cff1ae.png?imageMogr2/auto-orient/strip|imageView2/2/w/960/format/webp)

然后会转到生成完成界面

![](https://upload-images.jianshu.io/upload_images/3128629-417aed52b9f6933b.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

AppIcon

![](https://upload-images.jianshu.io/upload_images/3128629-06e920b0ceb2b89e.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

LaunchImage

点击右上角红箭头指的文件夹按钮保存，会自动打开所在文件夹

![](https://upload-images.jianshu.io/upload_images/3128629-1f1fbadca1ba2b03.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

如果有帮助到你，给个❤️支持一下O\(∩\_∩\)O

