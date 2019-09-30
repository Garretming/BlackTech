运行xcode模拟器时如图所示：

# Command PhaseScriptExecution failed with a nonzero exit code

这是因为Xcode10是默认选中的最新的New Build System\(Default\)，在这个编译系统的环境下，打包的CI脚本一直会报错。

解决方案：

Xcode菜单栏选择File-- Workspace Setting，把new build system\(Defalt\)切换到 Legacy Build System 在模拟器上运行就OK！



