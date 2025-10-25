from PIL import Image, ImageDraw, ImageFont
#from PIL.ExifTags import GPSTAGS, MAKE

class MakeCustomImage:
    def __init__(self , fnt:str , size:int , img:str):
        self.font = ImageFont.truetype(fnt, size)
        self.image = (Image.open(img).convert('RGBA'))

    # 文字字典: 'text'要插入的文字 , 'grid'插入文字的坐标 , 'color'插入文字的颜色
    # 图片字典: 'img'要插入的图片 , 'size'图片大小 , 'grid'插入图片的坐标
    def EditImg(self , project_list:list , insert_img:list = []):
        drawer = ImageDraw.Draw(self.image)
        # 镶进文字
        for l in range(len(project_list)):
            data = project_list[l]
            drawer.text(data['grid'], data['text'], fill=data['color'], font=self.font)
        # 镶进头像
        for i in range(len(insert_img)):
            data = insert_img[i]
            i_image = Image.open(data['img'])
            if(data['size'] == 'default'):
                data['size'] = (i_image.width , i_image.height)
            i_image = (i_image.resize(data['size']).convert('RGBA'))
            
            self.image.paste(i_image , data['grid'])
    
    def OutputImg(self , name:str):
        # 输出
        self.image.save(name)
    def DrawRect( self , pos, **kwargs):
        transp = Image.new('RGBA', self.image.size, (0,0,0,0))
        draw = ImageDraw.Draw(transp, "RGBA")
        draw.rectangle(pos, **kwargs)
        self.image.paste(Image.alpha_composite(self.image, transp))
    def ImgInfo(self):
        return( { 'width' : self.image.width , 'height' : self.image.height } )
    def Destroy(self):
        del self.image

if (__name__ == '__main__'):
    img = MakeCustomImage('./得意黑.otf' , 70 , './background.jpg')
    info = img.ImgInfo()
    img.DrawRect( ( 10 , 10 , 50 , 50 ) , fill=( 64 , 64 , 64 , 100 ) )
    img.EditImg( [ { 'grid' : (320 , 320) , 'text' : '写入测试1' , 'color' : (255,255,255,255) } ,{ 'grid' : (320 , 380) , 'text' : '写入测试2' , 'color' : (0,0,0,255) } ] )
    
    img.OutputImg('./output.png')
    img.Destroy()
