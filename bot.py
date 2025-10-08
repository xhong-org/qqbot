# 石库水这一块
import websockets
import asyncio
import requests
import json
import psutil
import re
import mcrcon
import msvcrt
import time
import array
import datetime
import random
import atexit
import pyotp
import os
import sys
import re
import platform
import math
import winrm
from mcstatus import JavaServer

# PC
pc_address = "7e526c6c1d80.ofalias.net:51155"

# Minecraft Server Ping

def mc_ping(name):
    mc_url = ""
    match name:
        case '七七服':
            mc_url = "221.236.10.155:39632"
        case 'y某人服':
            mc_url = "mc.yituring.top:18848"
        case '猹猹服':
            mc_url = "103.40.13.124:23242"
        case _:
            #return(False)
            mc_url = name

    server = JavaServer.lookup(mc_url)
    try:
        status = server.ping()
        del server
    except Exception as e:
        del server
        return(None)
    else:
        return({ 'ping' : status , 'url' : mc_url})

def mc_status(nam):
    mc_url = ""
    match nam:
        case '七七服':
            mc_url = "221.236.10.155:39632"
        case 'y某人服':
            mc_url = "mc.yituring.top:18848"
        case '猹猹服':
            mc_url = "103.40.13.124:23242"
        case '蛋壳服':
            mc_url = "mio6868.or-g.net:64432"
        case _:
            #return(False)
            mc_url = nam

    server = JavaServer.lookup(mc_url)
    try:
        status = server.status()
    except Exception as e:
        return(None)
    else:
        del server
        return({'status' : status,'url' : mc_url})
# somethings
user_2fa_data=[]
errOutInput = True
def errI():
     return(errOutInput)

def errS(e):
     errOutInput = e
     return
# 检测一个struct的name是否存在
def struct_exists(var_struct,name):
    return(f'{name}' in var_struct)

# 群功能
sign_data = []

# 签到
def dateToFloat():
    current_datetime = datetime.datetime.now()

    year = int(current_datetime.year)
    month = float(current_datetime.month / 100)
    day = float(current_datetime.day / 10000)
    return(float(year+month+day))

def loadSignData():
    sign_data.clear()
    with open("profile_data.json", 'r', encoding='utf-8') as user_file:
        user_data = json.load(user_file)
        sign_data[0:len(user_data['sign-up'])] = user_data['sign-up']
        global errOutInput
        errOutInput = bool(int(user_data['err-OutPut']))
    return

loadSignData()

def findSignUserData(user_id):
    l = -1
    for ll in range(len(sign_data)):
        if sign_data[ll]['user_id'] == user_id:
            l = ll
            break
    return(l)

def addUserProfile(user_id):
    if(findSignUserData(str(user_id)) == -1):
        j = {
            'user_id' : str(user_id),
            'sign_count' : 0,
            'coin' : 0,
            'time' : 0
        }
        sign_data.append(j)
        print(sign_data)
        saveUserProfile()
        return(True)
    else:
        return(False)

def userProfileSignIn (user_id):

    i = findSignUserData(str(user_id))
    if(i == -1):
        addUserProfile(str(user_id))

    i = findSignUserData(str(user_id))
    
    if(sign_data[i]['time'] == dateToFloat()):
        return(f"({user_id})\n您今天已经签到过了\n使用/bot-info可查看目前拥有的硬币数")
    else:
        #if(user_data[f'{user_id}'].signDataTimes == dateToFloat())
            
        sign_data[i]['time'] = dateToFloat()
        v = random.randint(10,100)
        sign_data[i]['coin'] += int(v)
        sign_data[i]['sign_count'] += 1
        saveUserProfile(False)
        c = sign_data[i]['coin']
        sc = sign_data[i]['sign_count']
        #print(sign_data)
        return(f"({user_id})签到成功\n累计签到次数:{sc}\n获得{v}硬币\n总硬币数:{c}")

def saveUserProfile(ii = True):
    f = {'sign-up' : sign_data,'2fa-code':user_2fa_data , 'err-OutPut' : int(errOutInput)}
    with open("profile_data.json", 'w', encoding='utf-8') as _file:
        json.dump(f,_file,ensure_ascii=False, indent=4)
        if (ii == True):
            return("保存配置成功")
        else:
            return("")

@atexit.register 
def clean(): 
     m = saveUserProfile()
     print(f"[System]{m}")
     return

# 管理员op列表
opList = []
admin_user = ""
def vfOpUser(user_id):
    if(str(user_id) == str(admin_user)):
        return(True)

    vf = False
    for i in range(len(opList)):
        if opList[i] == user_id:
            vf = True
            break

    return(vf)

def loadOpList(_id,vi = True):
    if vi == True:
        g = vfOpUser(_id)

        if g == False:
            return("无权")

    opList.clear()
    global admin_user
    admin_user = ""
    with open("ops.json", 'r', encoding='utf-8') as ops_file:
        ops_data = json.load(ops_file)
        opList[0:len(ops_data['oplist'])] = ops_data['oplist']
        admin_user = str(ops_data['admin'])
        print(opList)
        return(f"重载配置成功\n管理员:{opList}\nAdmin:{admin_user}")

def addOpList(add_user_id,user_id):
    if(str(add_user_id) == "3609822427"):
        return("不允许以bot的身份授予管理员权限")
    g = vfOpUser(add_user_id)
    if(str(user_id) == str(admin_user)):
        return("不能对最高权限用户进行操作")
    if g == False:
        return("无权")

    for l in range(len(opList)):
        if opList[l] == user_id:
            return(f"不能完成此操作\n因为({user_id})已经成为bot管理员了")

    opList.append(user_id)
    ii = {'oplist' : opList,'admin':admin_user}
    
    with open("ops.json", 'w', encoding='utf-8') as ops_file:   
        json.dump(ii,ops_file,ensure_ascii=False, indent=4)
        return(f"已将({user_id})设为bot管理员")

def removeOpList(add_user_id,user_id):
    if(str(add_user_id) == "3609822427"):
        return("不允许以bot的身份授予管理员权限")
    g = vfOpUser(add_user_id)
    if(str(user_id) == str(admin_user)):
        return("不能对最高权限用户进行操作")

    if g == False:
        return("无权")

    rr = vfOpUser(user_id)

    if rr == False:
        return(f"未能找到({user_id})")

    if user_id == add_user_id:
        return(f"不能对自己({add_user_id})进行撤销权限操作")
    opList.remove(user_id)
    ii = {'oplist' : opList,'admin':admin_user}
        
    with open("ops.json", 'w', encoding='utf-8') as ops_file:
        json.dump(ii,ops_file,ensure_ascii=False, indent=4)
        return(f"成功将({user_id})移除")

print(loadOpList(0,False))
#2FA 验证功能
def load2FAData():
    user_2fa_data.clear()
    with open("profile_data.json", 'r', encoding='utf-8') as user_file:
        user_data = json.load(user_file)
        user_2fa_data[0:len(user_data['2fa-code'])] = user_data['2fa-code']    
    return


load2FAData()

def bind2FAId(user_id,bind_id):
    f = False
    ii = -1
    bind_c = 0
    for i in range(len(user_2fa_data)):
        if (user_2fa_data[i]['user_id'] == str(user_id) and len(user_2fa_data[i]['bind_id']) >= 10):
            return("你已经超过绑定上限了n如需解绑不需要用的密钥,请输入/2fa-unbind <id>进行解绑，再输入/2fa-bind <2fa秘钥>绑定一个新的\n查看id可以使用/2fa-info查看")
        elif (user_2fa_data[i]['user_id'] == str(user_id)):
            f = True
            ii = i

    if (f == False):
        l = {'user_id' : str(user_id),'bind_id' : []}
        l['bind_id'].append(str(bind_id))
        user_2fa_data.append(l)
    else:
        user_2fa_data[ii]['bind_id'].append(str(bind_id))

    saveUserProfile()
    return(f"绑定成功\n剩余绑定个数:{10 - len(user_2fa_data[ii]['bind_id'])}")


def unbind2FAId(user_id , ID : int):
    msg = "该ID不存在或未绑定过一个秘钥"
    if(int(ID) < 0):
        return("输入的id为非法值")

    for i in range(len(user_2fa_data)):
        if (user_2fa_data[i]['user_id'] == str(user_id) and len(user_2fa_data[i]['bind_id']) > 0 and len(user_2fa_data[i]['bind_id']) > int(ID)):
            #user_2fa_data[i]['bind_id'] = ""
            del user_2fa_data[i]['bind_id'][int(ID)]
            saveUserProfile()
            msg = "解绑成功"

    return(msg)

def view2FAIdList(user_id):
    ii = ""
    d = False
    co = 0
    for i in range(len(user_2fa_data)):
        if (user_2fa_data[i]['user_id'] == str(user_id)):
            if(len(user_2fa_data[i]['bind_id']) == 0):
                return("No Code")
            else:
                for l in range(len(user_2fa_data[i]['bind_id'])):
                    ii += f"(id={l})Code: {user_2fa_data[i]['bind_id'][l]}\n"
                    co += 1
                d = True

    _m = ii if d == True else '您现在还未绑定过一个秘钥呢'             
    return(f"绑定个数:{f'{co}/10'}\n{_m}")

def find2FAId(user_id , ID : int):
    for i in range(len(user_2fa_data)):
        if (user_2fa_data[i]['user_id'] == str(user_id) and len(user_2fa_data[i]['bind_id']) != 0):
            if(ID > len(user_2fa_data[i]['bind_id']) - 1):
                return(None)
            else:
                return(user_2fa_data[i]['bind_id'][int(ID)])

    return(None)

# Phigros API
phi_data = []
def load2FAData():
    phi_data.clear()
    with open("profile_data.json", 'r', encoding='utf-8') as user_file:
        user_data = json.load(user_file)
        phidata[0:len(user_data['phi-data'])] = user_data['phi-data']    
    return



run_bot = True
# 发送群消息
async def send_group_message(websocket,group_id,message,bot_auto=True):
        json_message = {
            "action": "send_group_msg", 
            "params":{
                "group_id": group_id,
                "message": [
                    {
                        "type": "text",
                        "data": {
                            "text": f"{'[XTHX_BOT] \n' if bot_auto == True else ''}{message}"
                        }
                     }
                ]
                }
        }
        await websocket.send(json.dumps(json_message))
        await asyncio.sleep(1.5)


# Minecraft rcon连接&发送指令

# 服务器IP、端口、RCON密码
host = "cn-qz-plc-1.ofalias.net"  # 地址
port = 53467  # 端口
password = "2118181145141414"  # 密码
async def mc_send_cmd(cmd):
    if(mc_ping('y某人服') == None):
        return("与服务器失去连接")

    try:
        # 连接到RCON
        with mcrcon.MCRcon(host, password, port) as mcr:
            # 指令
            print(f"已发送指令\n{cmd}")
            res = mcr.command(cmd)
            return(res)
    except ConnectionRefusedError as e:
        return(f"连接被拒绝\n错误信息：{e}")
    except TimeoutError:
        return("连接超时")
    except mcrcon.MCRconException as e:
        return(f"RCON连接错误:{e}")
    except Exception as e:
        return(f"发生未知错误:{e}")
    except:
        return(f"发送指令出现异常报错")



async def hello_world(msg:dict,websocket):
    if msg.get("message_type") != "group":
        return
    # other
    global group_id
    group_id = msg.get("group_id")
    m = msg.get("user_id")
    mmsg = msg.get("raw_message")
    global mc_address
    current_datetime = datetime.datetime.now()
    year = int(current_datetime.year)
    month = int(current_datetime.month)
    day = int(current_datetime.day)
    hour = int(current_datetime.hour)
    minute = int(current_datetime.minute)
    second = int(current_datetime.second)
    print(f"[{year}.{month}.{day} - {hour}:{minute}:{second}] [INFO]-> 接收群消息:{mmsg}")
    
    
    
    s_p = mmsg[1:]
    # bot-cmd 
    mc_c_msg1 = s_p[:6]
    mc_c_msg2 = (s_p[7:])
    # bot-op
    op_msg1 = s_p[:6]
    op_msg2 = s_p[7:]
    # bot-deop
    deop_msg1 = s_p[:8]
    deop_msg2 = s_p[9:]
    # 2FA
    code_msg1 = s_p[:8]
    code_msg2 = s_p[9:]

    del_code_msg1 = s_p[:10]
    del_code_msg2 = s_p[11:]

    get_code_msg1 = s_p[:11]
    get_code_msg2 = s_p[12:]
    # say message mc
    s_msg1 = s_p[:1]
    s_msg2 = s_p[2:]
    # say message bot
    b_msg1 = s_p[:7]
    b_msg2 = s_p[8:]
    # recall-bot
    re_call_id = -1
    try:
        re_msg = re.search('[CQ:reply,id=(.+?)]').group(1)
        re_call_id = int(re_msg)
        re_msg2 = mmsg[15+len(msg):]
    except:
        re_msg = ""

   
    
    if (mmsg == "/bot-test" or mmsg == "测试"):
        msg = f"({m})\n已接收响应,完成!"
        await send_group_message(websocket,group_id,msg)
        pass
    elif mmsg == "/xthx-stop" or mmsg == "bot自爆":
        if(str(m) == "3609822427"):
            return
        vf = vfOpUser(m)
        if vf == True:
            msg = "自爆中"
            await send_group_message(websocket,group_id,msg)
            exit()
        else:
            msg = "无权"
            await send_group_message(websocket,group_id,msg)
        
        pass
    elif (mmsg == "/mc-start" or mmsg == "/mc-run"):
        ff = vfOpUser(m)
        if(ff == False):
            msg = "无权"
        else:
            if(mc_ping('y某人服') == None):
                ses = winrm.Session(f'http://{pc_address}/wsman', auth=('Administrator', 'Qwe123456'))
                r = ses.run_cmd('exit')# E:\\MC-Server-1.20.1\\minecraft\\run.bat
                msg = f"发送命令成功\n等待mc服务器启动中"
                del ses
            else:
                msg = "您需要将服务器关闭之后才能使用这条命令"

        await send_group_message(websocket,group_id,msg)
        pass
    elif mmsg == "/tps":
         a = vfOpUser(m)
         i = await mc_send_cmd("forge tps")
         msg = f"发送成功\n输出:{i}"

         await send_group_message(websocket,group_id,msg)
         pass
    elif mmsg == "/滚木":
         await send_group_message(websocket,group_id,"余额不足\n需要10000000个硬币你才可以买到")
         pass
    elif mmsg == "/list":
         i = await mc_send_cmd("list")
         msg = f"发送成功\n输出:{i}"
         await send_group_message(websocket,group_id,msg)
         pass
    elif s_msg1 == "s" and mmsg[0:1] == "/" and mmsg[2:3] == " ":
         if len(s_msg2) == 0:
             msg = "No Text"
         else:
             i = await mc_send_cmd(f"say {s_msg2}")
             msg = f"发送成功\n输出:{i}"
         
         await send_group_message(websocket,group_id,msg)
         pass
    elif((b_msg1 == "bot-say" and mmsg[0:1] == "/" and mmsg[8:9] == " ") or (mmsg[:8] == "踏马的快给爹地说" and mmsg[8:9] == ":")): # or 
        if(len(b_msg2) == 0):
            return
        if(str(m) == "3609822427"):
            return
        await send_group_message(websocket,group_id,b_msg2,False)
        pass
    elif(mmsg[0:5] == "/info" and mmsg[5:6] == " " and len(mmsg[6:]) > 0):
        ii = mc_status(mmsg[6:])
        if(ii == None):
            msg = "错误:与服务器失去连接"
        else:
            msg = f"Minecraft服务器版本:{ii['status'].version.name}\n服务器地址:{ii['url']}\n协议:{ii['status'].version.protocol}\n介绍:{ii['status'].description}\nPing延迟:{math.floor(ii['status'].latency)}ms"

        await send_group_message(websocket,group_id,msg)
        pass
    elif(mmsg[:5] == "/ping"):
        mmm = "/ping指令已不再支持,请使用/info <ip地址>以查看"
        await send_group_message(websocket,group_id,mmm)
        pass
    elif mmsg == "/bot-update" or mmsg == "执行更新脚本":
        if(str(m) == "3609822427"):
            return
        vf = vfOpUser(m)
        if vf == True:
            msg = "正在启动热更新服务"
            await send_group_message(websocket,group_id,msg)
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            msg = "无权"
            await send_group_message(websocket,group_id,msg)
        return
    elif mmsg == "/ok":        
        msg = "ojbk"
        await send_group_message(websocket,group_id,msg)
        pass
    elif del_code_msg1 == "2fa-unbind" and mmsg[0:1] == "/" and mmsg[11:12] == " ":
        c = unbind2FAId(str(m) , del_code_msg2)
        await send_group_message(websocket,group_id,c)
        
        return
    elif mmsg == "/bot-status" or mmsg == "运行状态": #bot状态
        cpu_status = f"CPU 占用: {psutil.cpu_percent(interval=1)}%"

        # 获取系统总计内存
        mem = psutil.virtual_memory()
        total_memory = float(mem.total) / 1024 / 1024 / 1024
        # 系统已经使用内存
        used_memory = float(mem.used) / 1024 / 1024 / 1024
        
        mem_status = f"内存: {str(used_memory)[0:4]}GB / {str(total_memory)[0:4]}GB({str(used_memory/total_memory *100)[0:4]}%)"
        msg = f"操作系统: {platform.system()}\n版本: {platform.version()}\n处理器: {platform.processor()}\n{cpu_status}\n{mem_status}"
        await send_group_message(websocket,group_id,msg)
        pass
    elif mmsg == "/bot-reload" or mmsg == "重载配置":
        if(str(m) == "3609822427"):
            return
        mm = loadOpList(m)
        loadSignData()
        await send_group_message(websocket,group_id,mm)
        pass
    elif mmsg == "/bot-help" or mmsg == "查看帮助":
        mg = [
            "指令帮助:",
            "\n",
            "#非OP指令",
            "\n",
            "> 日常用的",
            "1./bot-status   查看bot主机状态",
            "2./bot-sign   每日签到,能获得硬币.硬币可以用来购买奇奇怪怪的物品",
            "3./bot-info   查看个人信息",
            "4./bot-say <message>   令bot发送消息",
            "\n",
            ">2FA 工具",
            "1./2fa-bind <秘钥>   绑定一个2FA秘钥,谨慎被泄露",
            "2./2fa-unbind <ID>  解绑秘钥",
            "3./2fa-getcode <ID>  生成验证码",
            "4./2fa-info   查看秘钥",
            "\n",
            ">Phigros 乱七八糟的功能(暂未开放)",
            "1./phi-bind <SessionToken>   绑定SessionToken,建议在私人群聊使用",
            "2./phi-unbind   解绑SessionToken",
            "3./phi-update   查看更新内容",
            "3./phi-best <10～60>   查看b10～60",
            "4./phi-p <10～60>   查看p10～60",
            "5./phi-info   查看Phigros个人信息",
            "\n",
            ">mc查询便捷指令",
            "1./list   查看玩家列表",
            "2./tps   查看服务器当前tps",
            "3./s   向mc服务器发送游戏消息",
            "4./ping <忘了啥来着>   仅查看mc服务器延迟(注意:使用这条命令无效)",
            "5./info <IP>   查看mc服务器基本信息和Ping检测结果",
            "\n",
            ">不太常用的",
            "1./tab-errCmdInput   用于打开或者关闭输出错误的bot命令提醒",
            "2./bot-test   bot测试",
            "\n",
            "#OP指令",
            "\n",
            ">bot管理命令",
            "1./bot-op <QQ号>   给予某人OP权限",
            "2./bot-deop <QQ号>   取消某人OP权限",
            "3./bot-stop   终止bot服务进程",
            "4./bot-update   更新BOT",
            "5./bot-reload    重新加载配置文件",
            "6./mc-cmd <Minecraft指令>   执行一个mc指令",
            "7./mc-start   运行mc服务器(暂时不能用)"
            "\n",
            "(更多待开发中)",
        ]
        msg = "\n".join(mg)
        await send_group_message(websocket,group_id,msg)
        pass
    elif mmsg == "/bot-sign" or mmsg == "签到":
        mm = userProfileSignIn(str(m)) #"暂未开放"
        await send_group_message(websocket,group_id,mm)
        pass
    elif mmsg == "/bot-info" or mmsg == "个人信息":
        mm = ""
        o = findSignUserData(str(m))
        oo = ["",""]
        ss = ""
        s = vfOpUser(m)

        if(s == True):
            ss = "管理员"
        else:
            ss = "普通成员"

        if (o == -1):
            oo[0] = "0"
            oo[1] = "0"
        else:
            oo[0] = sign_data[o]['coin']
            oo[1] = sign_data[o]['sign_count']

        mm += f"({m}的个人信息)\n"
        mm += f"身份:{'开发者' if str(m) == str(admin_user) else ss}\n"
        mm += f"总硬币数:{oo[0]}\n"
        mm += f"累计签到次数:{oo[1]}\n"
        mm += f"2FA秘钥绑定个数:N/A"
        await send_group_message(websocket,group_id,mm)
        pass
    elif mmsg == "/bot-save" or mmsg == "保存配置":
        mm = saveUserProfile()
        await send_group_message(websocket,group_id,mm)
        pass
    elif get_code_msg1 == "2fa-getcode" and mmsg[0:1] == "/" and mmsg[12:13] == " ":
        v = find2FAId(str(m) , int(get_code_msg2))
        if(v == None):
            mm = "未绑定秘钥或填入的ID超过最大值,无法获取验证码"
        else:
            try:
                t = pyotp.TOTP(v)
                code = t.now()
                mm = f"成功获取验证码,30秒内有效\n验证码: {code}\nID: {get_code_msg2}\n预览密钥: {v[0:4 if len(v) >= 4 else len(v)]}(Test Module)"
            except:
                mm = "获取失败,疑似绑定了一个无效的2FA秘钥"


        await send_group_message(websocket,group_id,mm)
        pass
    elif code_msg1 == "2fa-bind" and mmsg[0:1] == "/" and mmsg[9:10] == " ":
        c = bind2FAId(str(m),str(code_msg2))
        await send_group_message(websocket,group_id,c)
        pass
    elif mmsg == "/2fa-info":
        mm = view2FAIdList(str(m))

        await send_group_message(websocket,group_id,mm)
        pass
     
    elif deop_msg1 == "bot-deop" and mmsg[0:1] == "/":
        t = deop_msg2.find("=")
        if (t != -1):
            if (len(deop_msg2[t+1:len(deop_msg2)-1]) >= 5):
                mm = removeOpList(m,int(deop_msg2[t+1:len(deop_msg2)-1]))
                await send_group_message(websocket,group_id,mm)
                return
        else:
            try:
                if len(deop_msg2) >= 5:
                    mm = removeOpList(m,int(deop_msg2))
                else:
                    mm = "请输入正确的QQ号或at某人"
            except ValueError as o:
                mm = f"输入值错误\n请输入正确的QQ号或at某人\nReason:{o}"

            await send_group_message(websocket,group_id,mm)

        pass
    elif op_msg1 == "bot-op" and mmsg[0:1] == "/":
        t = op_msg2.find("=")
        print(t)
        if (t != -1):
            if (len(op_msg2[t+1:len(op_msg2)-1]) >= 5):
                mm = addOpList(m,int(op_msg2[t+1:len(op_msg2)-1]))
                await send_group_message(websocket,group_id,mm)
                return
        else:
            try:
                if len(op_msg2) >= 5:
                    mm = addOpList(m,int(op_msg2))
                else:
                    mm = "请输入正确的QQ号或at某人"
            except ValueError as o:
                mm = f"输入值错误\n请输入正确的QQ号或at某人\nReason:{o}"

            await send_group_message(websocket,group_id,mm)

        pass
    elif mc_c_msg1 == "mc-cmd" and mmsg[0:1] == "/" and mmsg[7:8] == " ":
        p = vfOpUser(m)
        if p == True:
            i = await mc_send_cmd(mc_c_msg2)
            msg = f"发送成功\n输出:{i}"
        else:
            msg = "无权或被停用"

        await send_group_message(websocket,group_id,msg)
        pass
    elif mmsg == "/tab-errCmdOutput" or mmsg == "切换错误指令输出开关":
        global errOutInput
        if errOutInput == True:
            errOutInput = False
        else:
            errOutInput = True

        await send_group_message(websocket,group_id,f"Checked: {int(errOutInput)}")
        pass
    elif s_p[0:8] == "bot-kick" and mmsg[0:1] == "/":
        mm = "(有严重bug暂时不能开放)"
        await send_group_message(websocket,group_id,mm)
        pass
    elif (mmsg[0:1] == "/" and errI() == True) :
        await send_group_message(websocket,group_id,"未知指令\n请输入/bot-help查看帮助")
        pass

# 获取群列表
async def get_group_list(web):
    json_message = {
        "action": "get_profile_like"
    }
    await web.send(json.dumps(json_message))
    response = await web.recv()
    await asyncio.sleep(1.5)
    return(response)

err_count = 0
async def main():
    async with websockets.connect("ws://127.0.0.1:3001") as websocket:
        print("已连接至服务器")
        lll = await get_group_list(websocket)
        print(lll)
        #await send_group_message(websocket,1017923548,"服务已启动")
        async for message in websocket:
            
            #print(f"接收->{message}")
            msg = json.loads(message)
            try:
                await hello_world(msg,websocket)
            except Exception as e:
                global group_id
                global err_count
                err_count += 1
                await send_group_message(websocket,group_id,f"X某人的bot爆炸了,如果X某人的不在的话，似掉算了\n持续报错次数:{err_count}(超过五次自动关闭)\n报错信息:{e}{'' if err_count < 5 else '\n正在关闭服务中'}")
                if err_count >= 5:
                    exit()


count = 0     
while run_bot:
    asyncio.run(main())
    if count >= 500000:
        saveUserProfile()
        count = 0
        continue

    count += 1
