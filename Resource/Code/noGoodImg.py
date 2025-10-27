from requests import get
import os
import time

def GetOnlyImg()->bool:
    url = "https://cyapi.top/API/sjmt.php"
    try:
        res = get(url).content

        with (open(f'./Resource/Images/what_img.png','wb') as p):
            p.write(res)

        time.sleep(0.5)
        return(os.path.exists(f'./Resource/Images/what_img.png'))
    except:
        return(False)
