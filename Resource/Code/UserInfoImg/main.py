from Resource.Code.UserInfoImg.XImg import MakeCustomImage as img
#from XImg import MakeCustomImage as img
import time
import requests as get
import json as js
import random
from io import BytesIO
#   1069413063
def BuildUserImgInfo(qq:str , coin:int , lv:int , exp:int):
    # 计算延迟
    t = time.time()
    # 获取基本信息
    qq_url = f"https://uapis.cn/api/v1/social/qq/userinfo?qq={qq}"
    rr = js.loads(get.get(qq_url).content)
    print(rr)
    # 基本信息
    name = (f"{rr['nickname'][:8]}..." if len(rr['nickname']) >=8 else rr['nickname'])
    sign = f"{rr['long_nick'][:15]}..." if len(rr['long_nick']) >= 15 else rr['long_nick']
    sex = rr['sex']
    age = rr['age']
    qid = rr['qid']
    qq_level = rr['qq_level']
    email = rr['email']
    is_vip = '有' if rr['is_vip'] else '没有'
    vip_level = rr['vip_level']
    reg_time = rr['reg_time'][ : 4] + rr['reg_time'][10 : ]
    last_updated_time = rr['last_updated']
    # 棍木
    empty_str = '                       '
    need_xp = (lv * 30 + 30) - exp
    text = f" id: {qq}\n名字: {name}\n性别: {sex}\n年龄: {age}\n硬币: {coin}\n等级: Lv.{lv}\n经验值: {exp}\n(还需{need_xp}经验升至{lv+1}级)\n\n邮箱: {email}\nqid: {qid}\nQQ等级: {qq_level}\n有无QQ会员: {is_vip}\n注册时间:\n{reg_time}\n\n名片:\n{sign}"
    
    # 获取头像
    url = f"http://q.qlogo.cn/headimg_dl?dst_uin={qq}&spec=640&img_type=jpg"
    res = (get.get(url).content)
    temp_img = BytesIO(res)
    #读取头像
    path = "./Resource/Code/UserInfoImg/"
    im = img(path + 'font.otf' , 10 , temp_img)
    #im.OutputImg('get.png') # 测试导出
    # 获取头像长和宽
    im_width = im.ImgInfo()['width']
    im_height = im.ImgInfo()['height']
    # 调试
    print(f"图片长和宽: {im_width}*{im_height}")

    # 加载背景图
    bg_list = [
        path + '6.jpeg',
        path + '1.jpg',
        path + '2.jpg',
        path + '3.jpg',
        path + '4.jpg',
        path + '5.jpg',
        path + '7.jpg'
    ]
    image = img(path + 'font.otf' , 70 , bg_list[random.randint(0,len(bg_list) - 1)])
    # 获取背景图长和宽 
    info = image.ImgInfo()
    # 调试
    print(image.ImgInfo())
    # 绘制半透明图
    image.DrawRect( ( 100 , 100 , info['width'] - 100 , info['height'] - 100 ) , fill = ( 64 , 64 , 64 , 150 ) )
    # 请输入文本
    #ai_text = '只有无畏前进,胜利才属于你的'
    
    # 编辑图片
    image.EditImg(
        [
            {
                'text' : text,
                'grid' : (120 , 830 - (640 - im_height)),
                'color' : (255,255,255)
            }
        ],
        [
            {
                'img' : temp_img,
                'size' : 'default',
                'grid' : (120 , 150)
            }
        ]
        
    )
    # 输出
    image.OutputImg(f'./Resource/Images/qqimg-{qq}.png')
    print(f'Done,Generated {100 * (time.time()-t)}ms')
    time.sleep(0.5)

if(__name__ == '__main__'):
    BuildUserImgInfo('1069413063' , 0 , 0 , 0 )
    pass
'''
import requests
from PIL import Image
from io import BytesIO
yzmdata = requests.get(图片url)
tempIm = BytesIO(yzmdata.content)
im = Image.open(tempIm)

'''
