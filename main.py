# 依旧石库水()
# 别看下面一堆import 全是叠buff

import datetime
from Resource.Code.MCRcon import mc_send_cmd
from Resource.Code.bot_func import group_import_func as gp_scr
from Resource.Code.bot_func import MakeMsgClass as m_msg

print('初始化完成')
rst = False
gp_list = [
    '747059275',
    '581638376',
    '976841360',
    '1035500695',
    '570757868',
    '908558802',
    '1017923548',
    '721215474',
    '703318027',
    '1043997911',
    '958732188',
    '739570219'
]
# 自动群签到
while True:
    current_datetime = datetime.datetime.now()    
    hour = int(current_datetime.hour)
    minute = int(current_datetime.minute)
    second = int(current_datetime.second)
    year = int(current_datetime.year)
    month = int(current_datetime.month)
    day = int(current_datetime.day)
    if(hour == 0 and minute == 0 and second == 0):
        if(rst == False):
            l = 0
            gp_scr.send_group_msg('747059275',[m_msg.makeMsgText('签到')])
            for l in range(len(gp_list)):            
                gp_scr.send_group_msg(gp_list[l],[m_msg.makeMsgText('打卡')])
                gp_scr.sign_group(gp_list[l])

            print(f'[{year}.{month}.{day} - {hour}:{minute}:{second}] 全部执行成功')    
            rst = True
    else:
        rst = False
