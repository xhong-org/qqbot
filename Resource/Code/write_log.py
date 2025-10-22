import os
import datetime
def writeLog(log:str,_type:str,text:str,debug:bool = False):
    current_datetime = datetime.datetime.now()
    year = int(current_datetime.year)
    month = int(current_datetime.month)
    day = int(current_datetime.day)
    hour = int(current_datetime.hour)
    minute = int(current_datetime.minute)
    second = int(current_datetime.second)
    time_str = f"[{year}-{f'0{mouth}' if len(str(month)) == 1 else month}-{f'0{str(day)}' if len(str(day)) == 1 else day}   {f'0{hour}' if len(str(hour)) == 1 else hour}:{f'0{minute}' if len(str(minute)) == 1 else minute}:{f'0{second}' if len(str(second)) == 1 else second}] [{_type}]  "
    
    if(os.path.exists(log)):
        with(open(log,'a',encoding='utf-8') as f):
            f.write(f"{time_str}{text}\n")

    else:
        with(open(log,'w',encoding='utf-8') as f):
            f.write(f"{time_str}{text}\n")
    if(debug):
        print(text)


