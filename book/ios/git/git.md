git回滚到任意版本

先显示提交的log

$ git log -3
commit 4dc08bb8996a6ee02f
Author: Mark <xxx@xx.com>
Date:   Wed Sep 7 08:08:53 2016 +0800

    xxxxx

commit 9cac9ba76574da2167
Author: xxx<xx@qq.com>
Date:   Tue Sep 6 22:18:59 2016 +0800

    improved the requst

commit e377f60e28c8b84158
Author: xxx<xxx@qq.com>
Date:   Tue Sep 6 14:42:44 2016 +0800

    changed the password from empty to max123
回滚到指定的版本

git reset --hard e377f60e28c8b84158
强制提交

git push -f origin master



Git——如何将本地项目提交至远程仓库(第一次)
1.（先进入项目文件夹）通过命令 git init 把这个目录变成git可以管理的仓库。

git init
 
2.把文件添加到版本库中，使用命令 git add .添加到暂存区里面去，不要忘记后面的小数点“.”，意为添加文件夹下的所有文件(夹)。

git add .
 

3.commit到主分支

git commit -m "描述" 
 

4.登录github，把本地仓库提交至远程仓库。

接下来你要做的就是复制那个地址，然后你将本地仓库个远程仓库连接起来。

git remote add origin git@github.com:Garretming/blog.git  
 

5.进行第一次提交

git push -u origin master  
 

ps: windows系统中使用git时报错“warning: LF will be replaced by CRLF”解决方案：

复制代码
复制代码
$ rm -rf .git  // 删除.git  
$ git config --global core.autocrlf false  //禁用自动转换 

//然后重新执行

$ git init    
$ git add . 
复制代码
复制代码
 

rm -rf .git慎用！！！！原因详见：https://www.zhihu.com/question/29438735 不小心敲了rm -rf后反应是怎样的？









#Git 创建分支提交远程分支详解

1.创建本地分支
git branch 分支名，例如：git branch 2.0.1.20120806
注：2.0.1.20120806是分支名称，可以随便定义。

2.切换本地分支
git checkout 分支名，例如从master切换到分支：git checkout 2.0.1.20120806

3.远程分支就是本地分支push到服务器上。比如master就是一个最典型的远程分支（默认）。
git push origin 2.0.1.20120806

4.远程分支和本地分支需要区分好，所以，在从服务器上拉取特定分支的时候，需要指定远程分支的名字。
git checkout --track origin/2.0.1.20120806
注意该命令由于带有--track参数，所以要求git1.6.4以上！这样git会自动切换到分支。

5.提交分支数据到远程服务器

git push origin <local_branch_name>:<remote_branch_name>
例如：
git push origin 2.0.1.20120806:2.0.1.20120806
一般当前如果不在该分支时，使用这种方式提交。如果当前在 2.0.1.20120806 分支下，也可以直接提交
git push

6.删除远程分支
git push origin :develop

1,从已有的分支创建新的分支(如从master分支),创建一个dev分支

?
1
Git checkout -b dev
2,创建完可以查看一下,分支已经切换到dev

?
1
2
3
4
git branch
 
  * dev
  master
3,提交该分支到远程仓库

?
1
git push origin dev
4,测试从远程获取dev

?
1
git pull origin dev
或者：

如果用命令行，运行 git fetch，可以将远程分支信息获取到本地，再运行 git checkout -b local-branchname origin/remote_branchname  就可以将远程分支映射到本地命名为local-branchname  的一分支

5,我觉得现在重要的就是设置git push,pull默认的提交获取分支,这样就很方便的使用git push 提交信息或git pull获取信息

?
1
git branch --set-upstream-to=origin/dev
取消对master的跟踪

?
1
git branch --unset-upstream master
6,现在随便修改一下工程文件的内容,然后git commit ,git push,之后就可以直接提交到远程的dev分支中,而不会是master

#git 创建分支 并 提交到远程分支
git branch（分支命令的使用
http://hbiao68.iteye.com/blog/2055493

 

0.可以通过git branch -r 命令查看远端库的分支情况

 

1,从已有的分支创建新的分支(如从master分支),创建一个dev分支

git checkout -b dev

2,创建完可以查看一下,分支已经切换到dev

git branch

    * dev

    master

3.建立本地到上游（远端）仓的链接 --这样代码才能提交上去

git branch --set-upstream-to=origin/dev 

取消对master的跟踪

git branch --unset-upstream master





git 创建分支提交远程分支 

以下两个应该是同一个意思，=upstream : 上游码流的意思
git branch --set-upstream-to=master
git branch --set-upstream-to=original/master


git help branch
git branch [--set-upstream | --track | --no-track] [-l] [-f] <branchname> [<start-point>]
git branch (--set-upstream-to=<upstream> | -u <upstream>) [<branchname>]
git branch --unset-upstream [<branchname>]

git branch --set-upstream-to=original/master new
git branch --set-upstream debug origin/debug //其中debug为创建的分支

git branch --set-upstream debug origin/debug
 

提交该分支到远程仓库
git push origin dev

git push origin与git push -u origin master的区别
 
$ git push origin

上面命令表示，将当前分支推送到origin主机的对应分支。 

如果当前分支只有一个追踪分支，那么主机名都可以省略。 

$ git push 如果当前分支与多个主机存在追踪关系，那么这个时候-u选项会指定一个默认主机，这样后面就可以不加任何参数使用git push。

$ git push -u origin master 上面命令将本地的master分支推送到origin主机，同时指定origin为默认主机，后面就可以不加任何参数使用git push了。

# 本地分支代码提交到远端库
git push origin master
git push origin HEAD:refs/for/远端分支名

git push origin 本地分支名:refs/for/远端分支名

eg:
git push origin test:refs/for/master #本地test分支代码提交到远端master库

在远端服务器新建分支：

方法1：

git checkout -b dev
#建立本地到上游（远端）仓的链接 --这样代码才能提交上去
git branch --set-upstream-to=origin/dev 
git branch --set-upstream debug origin/debug //其中debug为创建的分支
git push origin dev

#取消对master的跟踪
git branch --unset-upstream master

 

方法2：

git branch -b stage2
git push origin 本地分支名:远端分支名xx  // 在服務器新建新分支名xxx

 

对比：

git branch -b stag2
git push origin stage2:refs/for/stage2 // 代码入庫命令，不会新建新分支在远端



#切换当前分支
git checkout --orphan gh-pages

#上传到远程分支
git push -u origin gh-pages