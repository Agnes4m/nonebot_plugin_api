import asyncio
import httpx
import mimetypes
try:
    import ujson as json
except:
    import json
from .path import DATA_PATH
from .config import *
API_DiCT = json.load(open(DATA_PATH/'api.json'), "r", encoding="utf8")

class API_MANAGE:
    def __init__(self) -> None:
        """加载全部command
         - data_list:响应列表
        """
        self.data_list = []
        self.command_list = []
        self.data_list.append(self.data_bytes('img','command'))
        self.data_list.append(self.data_bytes('text','command'))

    def api_com(self):
        """响应列表变成tuple"""
        a = tuple(self.data_list)
        return a
    
    def api_main_url(self,tag) -> str:
        """tag获取url"""
        for key in API_DiCT:
            for item in API_DiCT[key]:
                if item["command"] == tag:
                    self.value_url = item["main_url"]
        return self.value_url
    
    def api_type(self,tag):
        for key in API_DiCT:
            for item in API_DiCT[key]:
                if item["command"] == tag:
                    self.value_type = key
        return self.value_type
    
    def data_bytes(self,type,tag) -> list:
        """获取data的值列表"""
        data_list = []
        img_list = API_DiCT[type]
        for one in img_list:
            data_list.append(one[tag])
        return data_list    

async def get_bytes(url:str,number:int = 1) -> list[bytes]:
    """url获取直接文件bytes列表"""
    data_list = []
    for i in range(number):
        async with httpx.AsyncClient() as client:
            async with client.get(url) as response:
                data_bytes:bytes = await response.read()
                data_list.append(data_bytes)
    return data_list

async def identify_bytes_type(bytes_object:bytes) -> int:
    """
    识别文件类型
     - 0：未知/文字
     - 1：音频
     - 2：图片
     - 3：视频
     - 4：json
    """
    tag = mimetypes.guess_extension(bytes_object)
    if tag == None:
        try:
            data = json.loads(bytes_object.decode("utf-8"))
            # data is a valid JSON
            return 4
        except ValueError:
            return 0
    else:
        tag = tag[1:]
        if tag in RCD:
            return 1
        elif tag in IMG:
            return 2
        elif tag in VDO:
            return 3
        
        else:
            print(tag)
            return 0