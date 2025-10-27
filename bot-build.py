# 依旧石库水
import asyncio
import requests
import json
import websockets
import time
import platform
import psutil
import datetime
import os
import wget
import Resource.Code.user_level as user_level
from Resource.Code.petpet import petpet
#from Resource.Code.moutou import petpet
import Resource.Code.custom_sign as sign
from Resource.Code.mc_status import mc_get_status_ext as mc_get_status
#import Resource.Code.two_fa_verify as fa_v
from Resource.Code.bot_func import group_import_func as gp_f
from Resource.Code.bot_func import MakeMsgClass as m_f
from Resource.Code.write_log import writeLog as writeLog
import Resource.Code.xibao as bao
from Resource.Code.noGoodImg import GetOnlyImg
from Resource.Code.UserInfoImg.main import BuildUserImgInfo

import atexit


readme = ''
with open('README.md', 'r') as rm:
    readme = rm.read()
start = time.time()
bot_version = 'v.1.1.5 - Beta'
gp_f.setPort(3000)
send_time = 0
send_clamp = False
log_file = ''
def logChange():
    #print('test')
    global log_file
    current_datetime = datetime.datetime.now()
    year = int(current_datetime.year)
    month = int(current_datetime.month)
    day = int(current_datetime.day)
    log = log_file
    log_file = f'./Resource/Logs/log-{year}-{month}-{day}.log'
    if(log_file != log and len(log) != 0):
        gp_f.send_group_msg(
            '747059275',
            [
                m_f.makeMsgText('[XTHX_BOT - Beta Build]\n'),
                m_f.makeMsgText(f"\n日志上报中")
            ]
        )
        gp_f.send_group_msg(
            '747059275',
            [
                m_f.makeMsgFile(os.path.abspath(log))
            ]
        )

logChange()
@atexit.register
def clean():
    writeLog(log_file,'Debug',"Stopping service")

writeLog(log_file,'Debug','Starting service')

async def idk_script(dict_msg:dict):
    global send_time
    global send_clamp
    global readme
    if(dict_msg['msg_structor'][0]['type'] == 'reply'):
        if(dict_msg['msg_structor'][1]['type'] == 'text' and dict_msg['msg_structor'][1]['data']['text'] == '撤回'):
            gp_f.del_msg(dict_msg['msg_structor'][0]['data']['id'])
            #print('114514')
            return(True)
        else:
            return(False)
    elif(dict_msg['msg_structor'][0]['type'] != 'text'):
        return(False)
        
    text = ((dict_msg['msg_structor'][0]['data']['text']).split(" ",1))
    if(dict_msg['self_id'] != dict_msg['sender']['id']):
        writeLog(log_file,'Info',f"群名: {dict_msg['group_info']['name']}({dict_msg['group_info']['id']})->[{dict_msg['sender']['name']}]({dict_msg['sender']['id']}): {dict_msg['sender']['message']}")
    #asyncio.sleep(0.5)
    match text[0]:
        case '/bot-test' | '测试':
            gp_f.send_group_msg(
                dict_msg['group_info']['id'],
                [
                    m_f.makeMsgText('[XTHX_BOT - Beta Build]\n'),
                    m_f.makeMsgAt(dict_msg['sender']['id']),
                    m_f.makeMsgText(f"\n({dict_msg['sender']['id']})\n测试接收响应完成")
                ]
            )
            return(True)
        case '/bot-sign' | '签到':
            s = sign.userProfileSignIn(dict_msg['sender']['id'] )
            gp_f.send_group_msg(
                dict_msg['group_info']['id'],
                [
                    m_f.makeMsgText('[XTHX_BOT - Beta Build]\n'),
                    m_f.makeMsgAt(dict_msg['sender']['id']),
                    m_f.makeMsgText(f"\n{s}")
                ]
            )
            return(True)
        case '/bot-say':
            del text[0]
            if(len(text) == 0 or dict_msg['sender']['id'] == dict_msg['self_id']):
                return(False)
            else:
                text[0] = text[0].strip()
                str1 = ''.join(text)
            if(not bool(len(str1))):
                return(False)

            gp_f.send_group_msg(
                dict_msg['group_info']['id'],
                [
                    m_f.makeMsgText(str1)
                ]
            )
            return(True)
        case '/bot-stop':
            
            return(True)
        case '/bot-op':
            return(True)
        case '/bot-deop':
            return(True)
        case '/mc-cmd':
            return(True)
        case '/list':
            return(True)
        case '/tps':
            return(True)
        case '/say':
            return(True)
        case '/bot-status' | '运行状态':
            cpu_status = f"CPU 占用: {psutil.cpu_percent(interval=1)}%"

            # 获取系统总计内存
            mem = psutil.virtual_memory()
            total_memory = float(mem.total) / 1024 / 1024 / 1024
            # 系统已经使用内存
            used_memory = float(mem.used) / 1024 / 1024 / 1024
            
            mem_status = f"内存: {str(used_memory)[0:4]}GB / {str(total_memory)[0:4]}GB({str(used_memory/total_memory *100)[0:4]}%)"
            msg = f"操作系统: {platform.system()}\n版本: {platform.version()}\n处理器: {platform.processor()}\n{cpu_status}\n{mem_status}"
            
            current_datetime = datetime.datetime.now()    
            hour = int(current_datetime.hour)
            minute = int(current_datetime.minute)
            second = int(current_datetime.second)
            year = int(current_datetime.year)
            month = int(current_datetime.month)
            day = int(current_datetime.day)
            str1 = str(time.time() - start)
            res = str1[:str1.index('.')]
            gp_f.send_group_msg(
                dict_msg['group_info']['id'],
                [
                    m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n机器人版本: {bot_version}\n{msg}\n运行时间: {res}秒\n服务器本地时间: {year}年{month}月{day}日-{hour}点{minute}分{second}秒"),
                    m_f.makeMsgText("\n\nGithub Updated to 2025.10.27\nCode by XTHX_FORM")
                ]
            )
            return(True)
        case '随机来张神秘小图片' | '/x-image':
            gp_f.send_group_msg(
                dict_msg['group_info']['id'],
                [
                    m_f.makeMsgText('[XTHX_BOT - Beta Build]\n对不起,该服务已下线')
                ]
            )
        case '我要亿张神秘小图片':
            
            # 
            if(time.time() - send_time < 5):
                if(send_clamp == False):
                    gp_f.send_group_msg(
                        dict_msg['group_info']['id'],
                        [
                            m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n"),
                            m_f.makeMsgAt(dict_msg['sender']['id']),
                            m_f.makeMsgText('\n获取期间请勿连续发送,请耐心等待结果出来再发送')
                        ]
                    )
                    send_clamp = True

                return(False)
            else :
                send_clamp = False
            ai = False
            r18 = False
            writeLog(log_file,'Debug',text)
            if(len(text) == 2):
                sp = text[1].split(' ')
                #print(sp)
                match len(sp):
                    case 1:
                        if(sp[0][:5] == '-R18-'):
                            if(sp[0][5:] == 'yes'):
                                r18 = True
                    case 2:
                        if(sp[0][:5] == '-R18-'):
                            if(sp[0][5:] == 'yes'):
                                r18 = True
                        if(sp[1][:4] == '-AI-'):
                            if(sp[1][4:] == 'yes'):
                                ai = True
            try:        
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    [
                        m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n好的,请耐心等待")
                    ]
                )
                header = {
                    'Content-Type' : 'application/json'
                }
                payload = json.dumps({
                    'num' : 1,
                    'r18Type' : int(r18),
                    'aiType' : 1 if(ai == False) else 2,
                    'sizeList' : ['regular' for ll in range(20)]
                })
                writeLog(log_file,'Debug',payload)
                url = "https://api.mossia.top/duckMo"
                res = json.loads(requests.request("POST" , url , headers=header , data=payload).text)
                writeLog(log_file,'Debug',res)
                if(res['success']):
                    tags = ''
                    for ii in range(len(res['data'][0]['tagsList'])):
                        tags += f"#{res['data'][0]['tagsList'][ii]['tagName']} "
                    arr = [
                        m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n"),
                        m_f.makeMsgAt(dict_msg['sender']['id']),
                        m_f.makeMsgText(f"\n标题: {res['data'][0]['title']}\npid: {res['data'][0]['pid']}\nuid: {res['data'][0]['uid']}\n作者: {res['data'][0]['author']}"),
                        m_f.makeMsgText(f"\n标签: {tags}")
                    ]
                    for i in range(len(res['data'][0]['urlsList'])):
                        arr.append(m_f.makeMsgImage(res['data'][0]['urlsList'][i]['url']))
                    send_status = (gp_f.send_group_msg(dict_msg['group_info']['id'] , arr)['status'])
                    if(send_status != 'ok'):
                        gp_f.send_group_msg(
                            dict_msg['group_info']['id'],
                            [
                                m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n"),
                                m_f.makeMsgAt(dict_msg['sender']['id']),
                                m_f.makeMsgText('\n图片发送失败')
                            ]
                        )
                    send_time = time.time()
            except Exception as e:
                writeLog(log_file,'Error',e,True)
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    [
                        m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n图床获取失败")
                    ]
                )
                send_time = time.time()
            
            return(True)
        case '摸头':
            num = dict_msg['sender']['id']
            if(len(dict_msg['msg_structor']) >= 2):
                if(dict_msg['msg_structor'][1]['type'] == 'at'):
                    writeLog(log_file,'Debug','Num')
                    num = str(dict_msg['msg_structor'][1]['data']['qq'])
                
            i = petpet(num)
            #print(i)
            if(i == True):
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    [
                        m_f.makeMsgImage(os.path.abspath(f"./Resource/Images/gif-{num}.gif"))
                    ]
                )
            else:
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    [
                        m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n发送失败")
                    ]
                )
            return(True)
        case '赞我':
            s = json.loads(gp_f.send_like(dict_msg['sender']['id'] , 10))
            if(s['status'] == 'ok'):
                msg = '已经为你点了10个赞,记得给我回赞(◦˙▽˙◦)'
            else:
                msg = f"{s['message']}( ๑ŏ ﹏ ŏ๑ )"
            gp_f.send_group_msg(
                dict_msg['group_info']['id'],
                [
                    m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n{msg}")
                ]
            )
            return(True)
        case '查询mc服务器信息' | '/mc-info':
            if(len(text) == 2 and len((text[1].replace(' ','')).replace('\n','')) > 0):
                text[1] = (text[1].replace(' ','')).replace('\n','')
                mc = mc_get_status(text[1])
                lists = [
                    m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n"),
                    m_f.makeMsgAt(dict_msg['sender']['id']),                 
                ]
                if(mc['base_img'] != None):
                    lists.append(m_f.makeMsgImage(f"base64://{mc['base_img']}"))
                lists.append(m_f.makeMsgText('\n'+mc['msg']))
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    lists
                )
            else:
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    [
                        m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n"),
                        m_f.makeMsgAt(dict_msg['sender']['id']),
                        m_f.makeMsgText('\n地址去哪了?')
                    ]
                )
            return(True)
        case '个人信息' | '/bot-info':
            num = dict_msg['sender']['id']
            sign.userProfileSignIn(num , True)
            _id = sign.findSignUserData(num)
            data = sign.sign_data[_id]
            
            BuildUserImgInfo(num , data['coin'] , data['lv'] , data['xp'])
            time.sleep(0.5)
            gp_f.send_group_msg(
                dict_msg['group_info']['id'],
                [
                    m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n"),
                    m_f.makeMsgAt(num),
                    m_f.makeMsgImage(os.path.abspath(f"./Resource/Images/qqimg-{dict_msg['sender']['id']}.png")),
                    m_f.makeMsgText(f"(测试阶段,不代表最终成品)")
                ]
            )
            return(True)
        case '喜报':
            if(len(text) == 1):
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    [
                        m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n你这啥也没写"),
                    ]
                )
                return(True)
            i = bao.xibao(text[1])
            if(i):
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    [
                        m_f.makeMsgImage(os.path.abspath('./Resource/Images/xibao.png')),
                    ]
                )
            else:
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    [
                        m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n悲报: 图片生成失败"),
                    ]
                )
            return(True)
        case '悲报':
            if(len(text) == 1):
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    [
                        m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n你这啥也没写"),
                    ]
                )
                return(True)
            i = bao.beibao(text[1])
            if(i):
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    [
                        m_f.makeMsgImage(os.path.abspath('./Resource/Images/beibao.png')),
                    ]
                )
            else:
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    [
                        m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n喜报: 图片生成失败"),
                    ]
                )
            return(True)
        case '我要一张正经图':
            gp_f.send_group_msg(
                dict_msg['group_info']['id'],
                [
                    m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n好的,请耐心等待")
                ]
            )
            i = GetOnlyImg()
            if(i):
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    [
                        m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n"),
                        m_f.makeMsgAt(dict_msg['sender']['id']),
                        m_f.makeMsgImage(os.path.abspath('./Resource/Images/what_img.png')),
                        m_f.makeMsgText(f"\n\n并非正经"),
                    ]
                )
            else:
                gp_f.send_group_msg(
                    dict_msg['group_info']['id'],
                    [
                        m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n图片生成失败"),
                    ]
                )
            return(True)
        case 'readmd':
            gp_f.send_group_msg(
                dict_msg['group_info']['id'],
                [
                    m_f.makeMsgText(f"[XTHX_BOT - Beta Build]\n{readme}"),
                ]
            )
            return(True)
        case _:
            return(False)
        
async def judgeMsg(const_msg:dict):
    #   and const_msg['group_info']['id'] == '1036696409'
    if(const_msg['status'] and const_msg['type'] == 'group'):
        await idk_script(const_msg)
        return(True)
    else:
        return(False)
        


    
async def main():
    #logChange()
    async with websockets.connect("ws://127.0.0.1:3001") as websocket:
        writeLog(log_file,'Debug',"已连接至服务器",True)
        async for message in websocket:
            logChange()
            msg = json.loads(message)
            p = gp_f.parseWebMsg(msg)
            try:
                await judgeMsg(p)
            except Exception as e:
                gp_f.send_group_msg(
                    p['group_info']['id'],
                    [
                        m_f.makeMsgText(f"发生了一个错误\n错误信息: {e}\n请联系开发者并将错误信息发给他\n\n非常感谢"),
                    ]
                )
            #print(gp_f.parseWebMsg(msg))
            #print(message) 
    
while True:
    asyncio.run(main())
