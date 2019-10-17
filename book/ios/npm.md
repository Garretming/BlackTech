npm install、npm init、npm update、npm uninstall和package.json
node.js  19k 次阅读  ·  读完需要 6 分钟
npm install
安装本地包
npm install <package_name>:这个命令将在当前目录中创建node_modules目录（如果尚不存在），并将该软件包下载到该目录。该命令默认本地安装。

安装了哪个版本的软件包？
如果本地目录中没有package.json文件，则会安装最新版本的软件包。

如果有package.json文件，则安装满足该package（如果有的话）在package.json中声明的semver规则的最新版本。

安装全局包
npm install -g <package>：全局安装包。

package.json
npm init
npm init：这个命令用于创建一个package.json。

npm init --yes或npm init -y:从当前目录中提取的信息生成默认的package.json。创建过程中不会提问。

如果您的目录中已经有一个package.json文件，并且运行了npm install，那么npm将查看该文件中的dependencies，并下载满足所有这些的最新版本。

package.json文件中的description帮助人们在npm搜索中找到您的包，所以在package.json中进行自定义描述非常有用。

也可以完全自定义package.json文件的内容和在init期间提出的问题。这通过创建自定义.npm-init.js来完成。默认情况下，npm将查找您的主目录。 〜/ .npm-init.js

dependencies与devDependencies
dependencies和devDependencies指定了项目依赖的包。

dependencies：这些包在生产中需要。

devDependencies：这些包用于开发和测试。

npm install <package_name> --save命令会添加条目到package.json的dependencies中。
npm install <package_name> --save-dev命令会添加条目到package.json的devDependencies中。

npm update
更新本地软件包
npm update：用于更新依赖的软件包。需要在package.json文件所在的目录中运行该命令。

更新全局软件包
npm update -g <package>：更新全局软件包。
npm update -g：更新所有的全局软件包。
npm outdated -g --depth=0：找出需要更新的包。

npm uninstall
卸载本地软件包
npm uninstall <package>：从node_modules目录中移除一个包。

npm uninstall --save <package>：从package.json的dependencies中移除一个包。

npm uninstall --save-dev <package>：从package.json的devDependencies中移除一个包。

实际操作时，发现使用npm uninstall <package>不仅会在node_modules目录下删除该包，还会将该包在package.json中dependencies或devDependencies里面的信息删除。

卸载全局软件包
npm uninstall -g <package>：卸载全局软件包。


npm audit ： npm@5.10.0 & npm@6，允许开发人员分析复杂的代码，并查明特定的漏洞和缺陷。

npm audit fix ：npm@6.1.0,  检测项目依赖中的漏洞并自动安装需要更新的有漏洞的依赖，而不必再自己进行跟踪和修复。

同时，官网中还提供了一些其他的命令，整理如下：

1. 运行audit fix，但是只更新pkglock， 不更新node_modules：

$ npm audit fix --package-lock-only
2. 只更新dependencies中安装的包，跳过devDependencies中的包：

$ npm audit fix --only=prod
3.运行命令，得到audit fix将会更新的内容，并且输出json格式的安装信息，但是并不真的安装更新：

$ npm audit fix --dry-run --json
4. 得到json格式的详细检测报告

$ npm audit --json
附：

npm-audit 官网地址：https://docs.npmjs.com/cli/audit
