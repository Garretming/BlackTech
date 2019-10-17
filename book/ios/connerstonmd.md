# ![](/assets/import111.png)

# 解决Connerstone死锁

0.084

2019.05.24 10:03:10

字数 243

阅读 21

前段时间有小伙伴问我Connerstone无法拉取和上传代码,一直转菊花是怎么回事,经过排查,是因为操作不当导致死锁.恰好之前也遇到过这个问题,帮他解决后在这里记录一下,当做笔记.

**造成死锁的原因是在代码提交过程中退出了Connerstone**\(手贱退出其他应用时按Command + Q按快了🤣\)

---

**解决方案:**

**打开终端,输入命令  
**

**1.cd 项目路径**

**2.ls –al 查看项目下所有文件**

**3.找到.svn文件,输入命令sqlite3 .svn/wc.db "select \* from work\_queue"**

**查找卡住的任务队列**

**4.输入命令sqlite3 .svn/wc.db "delete from work\_queue"**

**清除未完成的队列.**

**5.重新打开connerstone右键项目clean**

**至此,死锁问题已经解决,重新打开Connerstone即可.因为未完成的队列被清除,所以最后一次提交的代码需要重新提交.**

# cornerstone创建分支与合并代码方法整理

**Cornerstone - trunk**、**tags**、**branches**

**trunk**：用于各版本开发提交代码

**tags**：用于记录和保存每个发布版本的代码

**branches**：用于修复特定版本bug而创建的分支

以下为举个栗子：

创建一个**Xcode Project**，工程名为**Winson**，初始版本为**V1.0**；

在**Cornerstone**的**Repositories**指定目录下创建文件夹**WinsonApp**，勾选上**subfolders**选项；

上传工程**Winson**至**WinsonApp**目录下的**trunk**；

check out **WinsonApp**目录下的**trunk**下的工程**Winson**至本地，名为**WinsonTrunk**；

在**WinsonTrunk**下开发，当第一个版本开发完成并发布之后，打个**tag**（在**SVN**服务器下的**WinsonApp**目录下的**trunk**下的工程**Winson**右键**tag**，在弹出窗口中指定**tag**路径为**tags**），名为**Winson\_V1.0**；

主干继续开发新功能；

当新功能未开发完，但是已上线的**V1.0**出现了紧急bug需要立即修复并发布，这个时候，**branchs**就出现了；

首先找到**V1.0**的**tag**，即**tags**文件夹下的名为**Winson\_V1.0**的文件，右键创建**branch**到**branchs**目录下，名为**Winson\_V1.0\_Bug-fix**；

**Winson\_V1.0\_Bug-fix**开发完成并发布后，提交到服务器；

主干开始合并代码；

选中**WinsonTrunk**，先**update**然后**commit**，然后选中，点击**Merge**，**Merg from**选取本地的**Winson\_V1.0\_Bug-fix**，然后点击**Merge Changes**按钮；

合并完以后，提交**WinsonTrunk**的时候会发现有冲突，点击**Confilicts**一个一个修改，然后一个一个**Resolve**;**UserInterfaceState.xcuserstate**这个文件肯定会有冲突，这里先不改它，直接点**Resolve**，然后**update**，然后**commit**。

合并代码就此完成，主干与SVN服务器上的代码是最新的包含V1.0已修复bug的代码。

**UserInterfaceState.xcuserstate**？  
 Xcode中保存的用户操作的GUI状态，如窗口位置，打开的标签页，在项目检查等展开的节点、 简单地调整大小的Xcode窗口将这个文件来改变和修改您的源代码控制系统进行标记。

### （一） 创建分支。 {#一-创建分支}

从云办公主干（Trunk）创建一个分支，放到branches中。  
步骤：

1. 选择主干中文件（JJSMOA）

2. 右击选择Branch

3. 输入分支名称（JJSMOA\_V3.0.1）

4. 并选择需要存放的位置，默认的是错误的位置，需要重新选择（此处选择^/JJSMOA/branches）

5. 点击创建分支即可。

   创建完成后，在branch文件夹下面就可以看到刚刚添加的分支文件了。

   ![](https://img-blog.csdn.net/20160804171915556 "这里写图片描述")

   图1 创建分支步骤截图

### （二） 合并代码。 {#二-合并代码}

当在分支上开发完成后，需要合并到主干代码中。  
步骤：

1. 先要check out一份目标代码到本地，即你要合并到哪个工程文件下，就需要先check out这个工程文件的代码。

2. 选中需要合并的目的文件，如将JJSMOA\_V3.0.1合并到JJSMOA中，此时应该选中JJSMOA

3. 选中主功能区上面的Merge

4. 选择合并的策略，主要有四种方式可以选择：Synchronization Branch、Reintegrate Branch、Cherry Pick Changes、Advanced Merge.  
   ![](https://img-blog.csdn.net/20160804172002501 "这里写图片描述")  
   图2 合并四种方式说明  
   根据自己的需求选择不同的方式，我们一般选择默认的Synchronization Branch。

5. 选择合并代码的来源文件。此处选择我们的分支文件，即JJSMOA\_V3.0.1

6. 选择合并选项。默认是包括所有文件。一般选择默认就可以。

7. 选中合并按钮。  
   ![](https://img-blog.csdn.net/20160804172159248 "这里写图片描述")  
   图3 合并代码步骤截图

### （三） 创建 {#三-创建}

创建tag与上述（一）中创建分支一样，此处就不再描述了。

