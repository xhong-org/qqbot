import json
import datetime
import random
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
    with open("./Resource/Data/profile_data.json", 'r', encoding='utf-8') as user_file:
        user_data = json.load(user_file)
        sign_data[0:len(user_data['sign-up'])] = user_data['sign-up']
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
            'time' : 0,
            'xp' : 0,
            'lv' : 0         
        }
        sign_data.append(j)
        print(sign_data)
        saveUserProfile([sign_data , []])
        return(True)
    else:
        return(False)
def exp_to_level(lv:int,xp:int):
    ins_lv = False
    text = ''
    while xp >= 30 + lv * 30:
        xp -= lv * 30
        lv += 1
        ins_lv = True
        text += f"恭喜等级升级至{lv}级\n"
    return({'ins_lv':ins_lv,'text':text,'lv':lv,'xp':xp})
def convertProfile(data:dict):
    level = 0 if(('lv' in data) == False) else data['lv']
    exp = 0 if(('xp' in data) == False) else data['xp']
    msg = ''
    t = []
    for l in range(data['sign_count']):
        r = random.randint(1 + 10 * level,10 + 15 * level)
        exp += r
        t = exp_to_level(level,exp)
        msg += t['text']
        level = t['lv']
        exp = t['xp']
    
    p = '检测到有过签到次数但是从来没有获取过任何经验值或等级,将为你的档案进行转换\n\n'
    
    data.update({'xp':exp,'lv':level})
    return([data,p + msg + f'总共获得经验值{exp}'])

def userProfileSignIn (user_id , data:list):

    i = findSignUserData(str(user_id))
    if(i == -1):
        addUserProfile(str(user_id))

    i = findSignUserData(str(user_id))
    mm = ''
    if(('xp' in sign_data[i]) == False or ('lv' in sign_data[i]) == False):
        c = convertProfile(sign_data[i])
        sign_data[i] = c[0]
        mm = c[1]

    if(sign_data[i]['time'] == dateToFloat()):
        saveUserProfile([sign_data , []])
        return(f"({user_id})\n{mm}\n----------\n您今天已经签到过了\n使用/bot-info可查看目前拥有的硬币数")
    else:
        #if(user_data[f'{user_id}'].signDataTimes == dateToFloat())
            
        sign_data[i]['time'] = dateToFloat()
        v = random.randint(10,100)
        sign_data[i]['coin'] += int(v)
        sign_data[i]['sign_count'] += 1
        saveUserProfile([sign_data , []],False)
        c = sign_data[i]['coin']
        sc = sign_data[i]['sign_count']
        r = random.randint(1 + 10 * sign_data[i]['lv'],10 + 15 * sign_data[i]['lv'])
        ll = exp_to_level(sign_data[i]['lv'],sign_data[i]['xp']+r)
        sign_data[i]['lv'] = ll['lv']
        sign_data[i]['xp'] = ll['xp']
        #print(sign_data)
        saveUserProfile([sign_data , []])
        return(f"({user_id})\n签到成功\n{mm}\n{ll['text']}----------\n获得经验+{r}\n累计签到次数:{sc}\n获得{v}硬币\n总硬币数:{c}")

def saveUserProfile(data:list,ii = True):
    f = {'sign-up' : data[0],'2fa-code':[1] }
    with open("./Resource/Data/profile_data.json", 'w', encoding='utf-8') as _file:
        json.dump(f,_file,ensure_ascii=False, indent=4)
        if (ii == True):
            return("保存配置成功")
        else:
            return("")


