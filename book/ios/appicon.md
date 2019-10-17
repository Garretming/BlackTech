### Python脚本生成iOS全套AppIcon图标_评分:_

python appicon.py ./src.png 第一次运行可能会需要安装Image组件，可能会要权限不足。所以第一次运行最好加一个sudo python3 appicon.py ./src.png 生成的文件夹AppIcon.appiconset直接替换掉项目中Assets.xcassets里面对应的文件夹即可。 XCode9, XCode10 beta6下测试某问题

# Mac快速制作AppIcon（App图标）

App Icon Gear只需要一张1024\*1024的原图即可生成一套图标

由于公司没有美工，所以app的设计、Icon、启动图片、欢迎图、按钮图标等，都要自己制作。  
这篇文章我介绍一种比较快速的方式来做：Keynote（也就是PPT）。

> 第一步：Keynote画图  
> 第二步：批量剪裁图标

#### 第一步：Keynote画图

![](https://upload-images.jianshu.io/upload_images/3128629-4346910e5827fedf.png?imageMogr2/auto-orient/strip|imageView2/2/w/160/format/webp)

![](https://upload-images.jianshu.io/upload_images/3128629-22771c90cfc4016b.png?imageMogr2/auto-orient/strip|imageView2/2/w/720/format/webp)

打开Keynote，选择“形状”里面的方框功能，画一个514 \* 514的方框作为图标的底，然后在右边设计区填充背景颜色等等，可以很容易就做出渐变色等效果。  
然后再加上你自己的设计，利用直线、曲线、填充、渐变、阴影就差不多了。

为什么大小要是514 \* 514呢？  
因为等你设计完你的图标后，我们要用截图工具截图，截一个512 \* 512大小的图片保存，这样图片的像素才能是1024\*1024的，符合App Store上架app的规范。  
而直接画个512 \* 512 的底截图时会发现少两个像素。

值得注意的是，把图标保存到本地后，还要打开图片，再导出一次，取消图片的Alpha通道，符合App Store上架app的规范。

具体操作看这里，我就不重复写了：[iOS 上架（小问题）去除图像中的alpha通道或透明度](https://link.jianshu.com/?t=http://blog.csdn.net/qq_28142539/article/details/51127560)

#### 第二步：批量剪裁图标

批量裁剪图标有两种方法

###### 一种是裁剪图标网站：

[在线批量剪裁各种尺寸iOS、Android APP LOGO图标 - aTool在线工具](https://link.jianshu.com/?t=http://www.atool.org/ios_logo.php)  
[图标工场](https://link.jianshu.com/?t=http://icon.wuruihong.com/)等等一大把...跟着网站里面的说明操作就可以了。

###### 一种是用app：

比如App Icon Gear、Appicon and Launchimage Maker、DevelopersTools、APP Image Resizer、Prepo等等一大把...

![](https://upload-images.jianshu.io/upload_images/3128629-f99f7e47efef292c.png?imageMogr2/auto-orient/strip|imageView2/2/w/160/format/webp)

这个app可以在App Store里面下载，虽然是英文的，但是操作很简单，直接把第一步做好的图标拖进主界面，就会生成各种比例大小的图标了，还可以预览效果，不满意可以重新第一步制作。

![](https://upload-images.jianshu.io/upload_images/3128629-51b4aee7a73516b0.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

然后点击右上角的Export导出到指定文件夹，再根据大小拖到Xcode里面就完成了。

