import requests
import json

# 构造消息结构
class MakeMsgClass:

    # 普通文本
    def makeMsgText(text:str)->dict:
        return({"type": "text","data": {"text": text}})

    # at 某人(默认QQ号不填则at全体成员)
    def makeMsgAt(qq_num:str = 'all')->dict:
        return({'type':'at','data': {'qq': qq_num}})

    # 发送图片结构
    def makeMsgImage(file:str , desc:str = '[Image]')->dict:
        return({'type': 'image','data': {'file': file,'summary': desc}})

    #

url = "http://127.0.0.1:3000/"

# 脚本部分
class group_import_func:
    def setPort(port:int)->bool:
        url = f"http://127.0.0.1:{port}/"
        try:
            # 设置请求头，进行UA伪装
            headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
            }

            # 发送GET请求
            response = requests.get(url=url, params={}, headers=headers)
            return(True)
        except:
            return(False)
        
    def get_group_list()->dict:
        req = f"{url}get_group_list"

        payload = json.dumps({
           "no_cache": False
        })
        headers = {
           'Content-Type': 'application/json'
        }

        response = requests.request("POST", req, headers=headers, data=payload)

        return(response.text)

    def set_group_sp_title(group_id:str,user_id:str,name:str)->dict:
        req = f"{url}set_group_special_title"
        payload = json.dumps({
           "group_id": group_id,
           "user_id": user_id,
           "special_title": name
        })
        headers = {
           'Content-Type': 'application/json'
        }

        response = requests.request("POST", req, headers=headers, data=payload)

        return(response.text)

    def sign_group(group_id:str)->dict:
        req = f"{url}set_group_sign"

        payload = json.dumps({
           "group_id": group_id
        })
        headers = {
           'Content-Type': 'application/json'
        }

        response = requests.request("POST", req, headers=headers, data=payload)

        return(response.text)

    def get_group_user_list(group_id:str)->dict:
        req = f"{url}get_group_member_list"

        payload = json.dumps({
           "group_id": group_id,
           "no_cache": False
        })
        headers = {
           'Content-Type': 'application/json'
        }

        response = requests.request("POST", req, headers=headers, data=payload)

        return(response.text)

    def send_poke(target_id:str , group_id:str = '')->dict:
        req = f"{url}send_poke"

        payload = json.dumps({
           "user_id": '3609822427',
           "group_id": group_id,
           "target_id": target_id
        })
        headers = {
           'Content-Type': 'application/json'
        }

        response = requests.request("POST", req, headers=headers, data=payload)

        return(response.text)

    def get_msg(msg_id:str)->dict:
        req = f"{url}get_msg"

        payload = json.dumps({
           "message_id": msg_id
        })
        headers = {
           'Content-Type': 'application/json'
        }

        response = requests.request("POST", req, headers=headers, data=payload)

        return(response.text)

    def delete_msg(msg_id:str)->dict:
        req = f"{url}delete_msg"

        payload = json.dumps({
           "message_id": msg_id
        })
        headers = {
           'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return(response.text)

    def send_group_msg(group_id:str,msg_list:list)->dict:
        url = "/send_group_msg"

        payload = json.dumps({
           "group_id": group_id,
           "message": msg_list
        })
        headers = {
           'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
    
        return(respone.text)












