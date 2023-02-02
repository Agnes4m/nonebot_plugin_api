from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import (
    GroupMessageEvent,
    Message,
    MessageEvent,
    PokeNotifyEvent,
    MessageSegment
)
from nonebot.matcher import Matcher
from nonebot.typing import T_State
from nonebot.permission import SUPERUSER
from nonebot.params import Arg, Command, CommandArg, Depends
from typing import Tuple
from .command import *
from .utils import *
import mimetypes

__version__ = "0.0.1"
__plugin_meta__ = PluginMetadata(
    name="三方api管理",
    description='简易三方api进行调用',
    usage='三方api',
    extra={
        "version": __version__,
        "author": "Umamusume-Agnes-Digital <Z735803792@163.com>",
    },
)

@api_command.handle
async def _(
    commands:Tuple[str,...] = Command(),
    args: Message = CommandArg(),
):
    command = commands[0]
    # msg = args.extract_plain_text()
    # msg = msg.split('-n')
    data_type = API.api_type(command)
    if data_type == 'data':
        data_url = API.api_main_url(command)
        bytes_list = await get_bytes(data_url)
        for i in bytes_list:
            num = await identify_bytes_type(i)
            if num == 1:
                await api_command.send(MessageSegment.record(i))
            elif num == 2:
                await api_command.send(MessageSegment.image(i))
            elif num == 3:
                await api_command.send(MessageSegment.video(i))
            elif num == 4:
                # json之后在做
                pass
# @api_cmd.handle()
# async def _(
#     event:MessageEvent,
#     state:T_State,
#     commands:Tuple[str,...] = Command(),
#     args : Message = CommandArg(),
# )
#     command = commands[0]
#     if command.startswith('添加'):
        