from PIL import Image
import os


def getcolor(dirname):
    """切图"""
    beforcutfilelist = os.listdir(os.path.dirname(__file__)+ '/' + '{}'.format(dirname))
    # aftercutlist = []
    for filename in beforcutfilelist:
        img = Image.open(os.path.dirname(__file__) + '/' + '{}'.format(dirname) + '/' + filename)
        src_strlist = img.load()
        # 获取背景颜色
        data = src_strlist[0, 0]
        # img.save(open(os.path.dirname(__file__) + \
        #               '/{}_aftercut/{}_{}.png'.format(dirname), 'wb'), 'png')

        print(filename, data)
        x, y = img.size
        print(x,y)
        p = Image.new('RGBA', (x, 256), data)
        p.paste(img, (0, 43))
        p.save(open(os.path.dirname(__file__) + \
                       '/3x1_afterupdate/{}'.format(filename), 'wb'), 'png')
if __name__ == '__main__':
    dirname = '11'
    newdirname = '3x1_afterupdate'
    # os.mkdir('./{}'.format(newdirname))
    # os.mkdir(os.path.dirname(__file__) + '/{}_afterupdate'.format(dirname))
    getcolor(dirname)

