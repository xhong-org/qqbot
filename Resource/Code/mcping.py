import requests as get
import time as t
import json as js
from mcstatus import JavaServer as je
def mc_get_status(host:str):
    url = f"https://uapis.cn/api/v1/game/minecraft/serverstatus?server={host}"
    r = ''
    try:
        res = js.loads(get.get(url).content)
        print(res)
        if(res.get('error')):
            return({'status' : False, 'msg' : f"Failed: {res['error']}"})
        match(res['code']):
            case 200:
                if (res['online'] == True):
                    if(res.get('players') != None):
                        t = f"当前服务器在线人数:{res['players']}/{res['max_players']}"
                    else:
                        t = f"服务器可进最大人数:{res['max_players']}"

                server = je.lookup(host)
                ping = ''
                try:
                    status = server.ping()
                    del server
                    ping = str(int(status)) + 'ms'
                except:
                    del server
                    ping = '无法获取'
            
                r = {
                    'status' : True,
                    'msg' : '该服务器不在线或不存在' if res['online'] == False else f"原地址:{host}\nSRV解析IP:{res['ip']}\n版本:{res['version']}\n{t}\n端口:{res['port']}\n延迟:{ping}\nmotd:{str(res['motd_clean'])}"
                }
            case 'NOT_FOUND':
                r = {'status' : False, 'msg' : '解析地址失败,可能是连接地址输入错误或服务器处于离线状态'}
            case 'UPSTREAM_ERROR':
                r = {'status' : False, 'msg' : '查询失败。在尝试连接并获取服务器信息时发生网络错误或协议错误。'}

        return(r)
    except Exception as e:
        print(e)
        return({'status' : False, 'msg' : '接口异常或内部错误'})
