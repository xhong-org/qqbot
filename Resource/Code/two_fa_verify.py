import json

user_2fa_data = []
#2FA 验证功能
def load2FAData():
    user_2fa_data.clear()
    with open("./Resource/Data/profile_data.json", 'r', encoding='utf-8') as user_file:
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
