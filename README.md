

# github上创建项目，拉到本地，再gitbook init
# gitbook
## 1、安装
    1、npm install gitbook -g
    //安装命令
    npm install -g gitbook-cli

    //卸载命令
    npm uninstall -g gitbook
    
    cd x到项目文件夹下，执行 gitbook init 
    
    gitbook ls
    
    
    gitbook ls-remote 列出远程可用的gitbook版本
    
    gitbook update 更新到gitbook的最新版本
    
## 写文件
    如果想要新增章节，可以在 SUMMARY.md 里面新增，然后执行 gitbook init 就会新增对应的 md 文件，原有文件不会变化；如果想要删除章节，在 SUMMARY.md 里面删除，然后执行 gitbook init 想要删除的 md 文件并不会删除，需要手动删除。
## 样式设置
1、配置book.json

## 安装插件
安装依赖
gitbook install
$ gitbook install ./

## 预览
    1、执行下面的命令
    $ gitbook serve
    然后浏览器中输入 http://localhost:4000 就可以预览生成的以网页形式组织的书籍。

## debug
    指定log的级别

    gitbook build --log=debug
    1
    输出错误信息

    gitbook builid --debug

## 编译
    执行命令：

    gitbook build
    1
    运行该命令后会在根文件夹生成一个 _book 文件夹，包含了书籍的所有 html 文件. 可以使用该命令来生成网页而不开启服务器，也可以将_book文件夹部署到服务器上。
    
    2、
    生成静态网页时指定gitbook的版本，如果本地没有将先下载
    gitbook build --gitbook=3.2.3
    
    3、
    $ mkdir /tmp/gitbook
    $ gitbook build --output=/tmp/gitbook
