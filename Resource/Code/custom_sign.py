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
            'time' : 0
        }
        sign_data.append(j)
        print(sign_data)
        saveUserProfile([sign_data , []])
        return(True)
    else:
        return(False)

def userProfileSignIn (user_id , data:list):

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
        saveUserProfile([sign_data , []],False)
        c = sign_data[i]['coin']
        sc = sign_data[i]['sign_count']
        #print(sign_data)
        return(f"({user_id})签到成功\n累计签到次数:{sc}\n获得{v}硬币\n总硬币数:{c}")

def saveUserProfile(data:list,ii = True):
    f = {'sign-up' : data[0],'2fa-code':[1] }
    with open("./Resource/Data/profile_data.json", 'w', encoding='utf-8') as _file:
        json.dump(f,_file,ensure_ascii=False, indent=4)
        if (ii == True):
            return("保存配置成功")
        else:
            return("")


