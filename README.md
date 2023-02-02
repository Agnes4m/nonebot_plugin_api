<div align="center">
  <img src="https://s2.loli.net/2022/06/16/opBDE8Swad5rU3n.png" width="180" height="180" alt="NoneBotPluginLogo">
  <br>
  <p><img src="https://s2.loli.net/2022/06/16/xsVUGRrkbn1ljTD.png" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot_plugin_api
_✨Nonebot2下非常简单的三方api接口操作✨_

<a href="https://github.com/Umamusume-Agnes-Digital/nonebot_plugin_api/stargazers">
        <img alt="GitHub stars" src="https://img.shields.io/github/stars/Umamusume-Agnes-Digital/nonebot_plugin_api" alt="stars">
</a>
<a href="https://github.com/Umamusume-Agnes-Digital/nonebot_plugin_api/issues">
        <img alt="GitHub issues" src="https://img.shields.io/github/issues/Umamusume-Agnes-Digital/nonebot_plugin_api" alt="issues">
</a>
<a href="https://jq.qq.com/?_wv=1027&k=HdjoCcAe">
        <img src="https://img.shields.io/badge/QQ%E7%BE%A4-399365126-orange?style=flat-square" alt="QQ Chat Group">
</a>
    <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="python">
    <img src="https://img.shields.io/badge/nonebot-2.0.0rc1+-red.svg" alt="NoneBot">
</div>

## 使用说明

    在json中只需要输入url和响应指令就可以，这个项目可以自动识别音频、图片、视频并进行输出

## 操作方法

启动一次，在bot目录下data/api/api.json，填入url和其他信息格式如下(可能需要重启)

        {
                "data":[
                        {
                        "detail":"这里是注释",
                        "command":"涩图",
                        "main_url":"http://114514:514?key=114&value=514"
                        }
                ]
        }

## 配置项
暂无

## to do

 -[ ] 支持上传文件
 -[ ] 支持json解析