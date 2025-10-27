from requests import get
import os
import time

# https://cyapi.top/API/beibao.php?msg=
def xibao(text:str)->bool:
    url = f"https://cyapi.top/API/xb.php?msg={text}"
    try:
        res = get(url).content

        with (open(f'./Resource/Images/xibao.png','wb') as p):
            p.write(res)

        time.sleep(0.5)
        return(os.path.exists(f'./Resource/Images/xibao.png'))
    except:
        return(False)

def beibao(text:str)->bool:
    url = f"https://cyapi.top/API/beibao.php?msg={text}"
    try:
        res = get(url).content

        with (open(f'./Resource/Images/beibao.png','wb') as p):
            p.write(res)

        time.sleep(0.5)
        return(os.path.exists(f'./Resource/Images/beibao.png'))
    except:
        return(False)
