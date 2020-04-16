'''
    此类中的方法用来生成图片验证码，并返回给浏览器
'''


def verifyCode(req):
    print("ddddddddddd")
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random as ra
    # 定义变量，用户画面的背景色、宽、高
    bgcolor = (ra.randrange(20, 100), ra.randrange(20, 100), ra.randrange(20, 100))
    width = 100
    height = 50
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (ra.randrange(0, width), ra.randrange(0, height))
        fill = (ra.randrange(0, 255), 255, ra.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str = '1234567890qwertyuiopasdfghjklzxcvbnmQAZWSXEDCRFVTGBYHNUJMIKOLP'
    # 随机选取4个作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[ra.randrange(0, len(str))]

    # 构造字体对象
    font = ImageFont.truetype(r'C:\Windows\Fonts\consola.ttf', 40)
    # 构造字体颜色
    fontColor = (255, ra.randrange(0, 255), ra.randrange(0, 255))

    # 绘制四个字符
    draw.text((5, 2), rand_str[0], font=font, fill=fontColor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontColor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontColor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontColor)

    # 释放画笔
    del draw

    # 存入session，用于进一步验证
    req.session['verifycode'] = rand_str

    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')

    # 图片保存到本地
    im.save('verifycode', 'png')
    from django.http import HttpResponse
    # 将内存中图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


if __name__ == '__main__':
    verifyCode("")
