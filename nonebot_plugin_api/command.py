from nonebot import on_notice,on_command,on_regex,on_fullmatch,CommandGroup
from .utils import API_MANAGE



# {
#     "img":[
#         {
#             "detail":"a60的涩图库",
#             "command":"涩图",
#             "main_url":"http://a60.one:404/?bytes=true&san=6&only=true"
#         }
#     ],
 
API = API_MANAGE()

api_word=CommandGroup('api')
api_command = on_command('这里是api响应的对象',aliases=API.api_com(),block=True,priority=20)
api_cmd = api_word.command(
    "api",
    aliases={
        "添加api",
        "删除api",
        "修改api",
    },
)