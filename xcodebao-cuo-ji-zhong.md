运行xcode模拟器时如图所示：

# Command PhaseScriptExecution failed with a nonzero exit code

这是因为Xcode10是默认选中的最新的New Build System\(Default\)，在这个编译系统的环境下，打包的CI脚本一直会报错。



解决方案：







Xcode菜单栏选择File-- Workspace Setting，把new build system\(Defalt\)切换到 Legacy Build System 在模拟器上运行就OK！

————————————————

版权声明：本文为CSDN博主「honey缘木鱼」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。

原文链接：https://blog.csdn.net/dt1991524/article/details/85339816

