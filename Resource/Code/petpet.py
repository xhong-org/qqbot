import requests
import os
import time

def petpet(num:str)->bool:
    url = f"https://uapis.cn/api/v1/image/motou?qq={num}"
    try:
        res = (requests.get(url).content)

        with open(f'./Resource/Images/gif-{num}.gif','wb') as f:
            f.write(res)

        time.sleep(0.5)

        return(os.path.exists(f'./Resource/Images/gif-{num}.gif'))
    except:
        return(False)
