from requests import get as get
import time as t
import json as js
from mcstatus import JavaServer as je
def mc_get_status(host:str):
    url = f"https://uapis.cn/api/v1/game/minecraft/serverstatus?server={host}"
    r = ''
    try:
        res = js.loads(get(url).content)
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

def mc_get_status_ext(host:str):
    url = f"https://api.mcsrvstat.us/3/{host}"
    image_base = None
    msg = ''
    try:
        res = js.loads(get(url).content)
        #print(res)
        if(res['online']):
            if(res.get('icon') != None):
                image_base = res['icon'][res['icon'].find(',') + 1 : ]
            else:
                image_base = None
            players_text = ''
            msg += f"IP:{res['ip']}\n连接地址:{host}\n是否在线:{res['online']}\n在线人数:{res['players']['online']}/{res['players']['max']}\n"
            msg += f"版本:{res['version']}\n主机名:{res['hostname']}\nmotd:{res['motd']['clean']}\n"
            dns = ''
            if(res['debug'].get('dns') != None):
                if(res['debug']['dns'].get('srv') != None):
                    dns += "SRV类型反解析:\n"
                    for l in range(len(res['debug']['dns']['srv'])):
                        ii = res['debug']['dns']['srv'][l]
                        if(ii['type'] != 'SRV'):
                            continue
                        dns += f"{int(l) + 1}.\n解析子名:{ii['name']}\n优先级:{ii['priority']}\n权重:{ii['weight']}\n目标端口:{ii['port']}\n目标:{ii['target']}\n"
                if(res['debug']['dns'].get('a') != None):
                    dns += "A类型反解析:\n"
                    for ll in range(len(res['debug']['dns']['a'])):
                        ii = res['debug']['dns']['a'][ll]
                        if(ii['type'] != 'A'):
                            continue
                        dns += f"{int(ll) + 1}.\n名字:{ii['name']}\nttl:{ii['ttl']}\nIP:{'无法获取' if ii.get('address') == None else ii['address']}\n"
            msg += f"是否使用了SRV:{res['debug']['srv']}\nDNS:{dns if len(dns) > 0 else '未检测到'}"
        else:
            msg = f"IP:{res['ip']}\n在线状态:{res['online']}\n"
            dns = ''
            if(res['debug'].get('dns') != None):
                if(res['debug']['dns'].get('srv') != None):
                    dns += "SRV类型反解析:\n"
                    for l in range(len(res['debug']['dns']['srv'])):
                        ii = res['debug']['dns']['srv'][l]
                        if(ii['type'] != 'SRV'):
                            continue
                        dns += f"{int(l) + 1}.\n名:{ii['name']}\n优先级:{ii['priority']}\n权重:{ii['weight']}\n目标端口:{ii['port']}\n目标:{ii['target']}\n"
                if(res['debug']['dns'].get('a') != None):
                    dns += "A类型反解析:\n"
                    for ll in range(len(res['debug']['dns']['a'])):
                        ii = res['debug']['dns']['a'][ll]
                        if(ii['type'] != 'A'):
                            continue
                        dns += f"{int(ll) + 1}.\n名字:{ii['name']}\nttl:{ii['ttl']}\nIP:{'无法获取' if ii.get('address') == None else ii['address']}\n"
            msg += f"是否使用了SRV:{res['debug']['srv']}\nDNS:{dns if len(dns) > 0 else '未检测到'}"
    except Exception as e:
        msg = f"Failed:  接口异常或内部错误 \nReason: {e}"
    return({'msg' : str(msg), 'base_img' : image_base})

if (__name__ == '__main__'):
    print(mc_get_status_ext("mc.hypixel.net"))
    
