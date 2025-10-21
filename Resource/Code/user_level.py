import json

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
    with open("./Resource/Data/ops.json", 'r', encoding='utf-8') as ops_file:
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
        
    with open("./Resource/Data/ops.json", 'w', encoding='utf-8') as ops_file:
        json.dump(ii,ops_file,ensure_ascii=False, indent=4)
        return(f"成功将({user_id})移除")

