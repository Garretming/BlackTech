# pod search 获取不到最新库的解决方法

在使用CocoaPods中pod search命令搜索第三方框架后，显示框架信息并不会自动退出到可输入命令的状态，而需要按键盘Q键来退出信息显示的状态。

用list命令 dir一样 如果你想学习使用进行后台FTP下载，那么就必须学习FTP指令。 FTP的

[命令行](https://www.baidu.com/s?wd=%E5%91%BD%E4%BB%A4%E8%A1%8C&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)

格式为： ftp -v -d -i -n -g \[主机名\] ， 其中 -v 显示远程服务器的所有响应信息； -n 限制ftp的自动登录，即不使用；.n etrc文件； -d 使用调试方式...

在工作中使用 'pod search GPUImage' 搜索库时，出现了这个错误提示：

```
[
!
]
 Unable to find a pod 
with
 name
,
 author
,
 summary
,
or
 description matching 
'GPUImage'
```

而使用'pod search AFNetworking'时也同样出现了这个问题，但前段时间这个功能是可以正常使用的。

> 为了确定我们搜索的库是不是真的在Cocoapods的Repos中存在，我们可以到[https://cocoapods.org/](https://link.jianshu.com/?t=https%3A%2F%2Fcocoapods.org%2F)中进行搜索查询。如果搜索的类库确实不存在，出现这个提示是正常的，如果存在，却出现这个提示，请往下看解决方法。

在网上查询后发现，获取不到最新库的原因主要有两个：

```
1.cocoapods的版本过低
2.还没有更新本地仓库
```

解决方法：

### 更新pods

```
1、首先查看当前版本
pod --version  //目前最新版是1.3.1

2、查询当前安装的Ruby源
gem source -l
输出为'https://ruby.taobao.org/' 说明当前是淘宝的源

3、移除淘宝的Ruby源，添加新的源（目前淘宝的源不可用了）
 gem sources --remove https://ruby.taobao.org/
 gem sources -a https://gems.ruby-china.org/

4、查看源是否添加成功
gem source -l
输出 'https://gems.ruby-china.org/'说明添加成功

5、开始安装
sudo gem install cocoapods

可能会出现报错'Operation not permitted - /usr/bin/xcodeproj',解决办法如下：
输入命令 'sudo gem install -n /usr/local/bin cocoapods'

6、再次查看pod版本
pod --version
输出 1.3.1表示升级成功
```

### 更新本地仓库

```
执行 'pod repo update'更新本地仓库，执行时间有点长，请耐心等待一会。本地仓库完成后，即可搜索到指定的第三方库。

另一种方法：执行命令'rm ~/Library/Caches/CocoaPods/search_index.json'，删除该文件,然后再执行pod search 命令就可以正常使用了。
```



