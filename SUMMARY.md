# Gitbook根据目录生成Summary.md

2017.11.16 11:31:43

字数 326

阅读 4935

## 使用插件生成SUMMARY.md

插件地址:[**gitbook-plugin-summary**](https://link.jianshu.com/?t=https://github.com/julianxhokaxhiu/gitbook-plugin-summary)

### book.json加入以下

```
{
"title"
:
"公共服务组文档库"
,
"theme-default"
:
{
"showLevel"
:
true
}
,
"plugins"
:
[
"summary"
,
"toggle-chapters"
,
"theme-comscore"
]
}
```

插件说明:  
summary: 自动生成SUMMARY.md文件

toggle-chapters: 菜单可以折叠

theme-comscore: 主题插件, 修改标题和表格颜色

###### 根目录下新增0-README.md文件, 该文件对应gitbook中introduction菜单

###### gitbook新增菜单

在根目录下新增目录, 如取名 "菜单1", 在菜单1目录中新增0-README.md文件, 并在该文件中加入标题

```
        # 菜单1
        ......

```

该标题对应gitbook中该菜单名称.

子菜单添加规则一致, 需要在目录中加入README.md文件, 并指定文件中的标题为菜单名称

###### 在菜单中加入文件

在菜单中加入 用户指南 MARKDOWN文件, 并修改该文件的标题为

```
        # 用户指南
        ......

```

### 注意事项

1. 每个新增的目录中加入README.md否则菜单则为不可折叠

2. 同个目录下的文件采用自然排序来决定菜单生成的前后顺序, 故在文件或目录前加入 "数字-" 如 "0-" 或 "1-" 来排序菜单的前后顺序.

3. 菜单由目录自动生成, 菜单名称依赖md文件中的标题, 故每个md文件中必须添加标题, 否则无法生成目录.



