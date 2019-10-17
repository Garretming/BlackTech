问题一:修改info.plist

![](/assets/项目import.png)

我想了半天才想起我之前有更改过Info.plist与Prefix.pch的名字及位置，由于工程内有Run Script涉及到自动增加CFBundleVersionNumbel的脚本，但是，由于我之前更改过info.plist文件的名字和位置，所以导致无法正确获取CFBundleVersionNumbel的值。导致问题的info.plilst文件位置设置截图

![](https://upload-images.jianshu.io/upload_images/900142-460c15dffa0d06eb.png?imageMogr2/auto-orient/strip|imageView2/2/w/903/format/webp)

导致问题的info.plilst文件位置设置.png

导致出现问题的主要原因就是在Build Settings 的 info�.plist文件的路径上多添加了一个$\(SRCROOT\)，导致路径错误；

### 正确设置info.plilst的位置方法

直接使用工程主目录和其目录下的info.plist文件的相对路径，也即以上将$\(SRCROOT\)去掉后的路径；  
ps：$\(SRCROOT\)其实就是当前目录的意思

##### 其实，如果在其他位置没有自己直接调用plist文件的内容，就像我在RunScript中调用CFBundleVersionNumbel值这样，在工程名前，加或者不加上"$\(SRCROOT\)/"都可以正常使用，只是建议不要添加$\(SRCROOT\)，因为写的越具体，在其他位置调用起来遇到的麻烦反而有可能越多；.pch文件跟.plist文件基本一致，所以不再重述；



