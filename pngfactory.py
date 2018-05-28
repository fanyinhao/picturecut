import os
from PIL import Image
# print(os.path.dirname(__file__))
# print(os.listdir(os.path.dirname(__file__)))


# def getfilenames(path=os.path.dirname(__file__)):
#     """获取路径下的所有文件名"""
#     return os.listdir(path)


def cutimage(dirname, row, column):
    """切图"""
    beforcutfilelist = os.listdir(os.path.dirname(__file__)+ '/' + '{}'.format(dirname))
    # aftercutlist = []
    for filename in beforcutfilelist:
        img = Image.open(os.path.dirname(__file__) + '/' + '{}'.format(dirname) + '/' + filename)
        size = img.size
        newname = filename[0:-4]
        print(size[0])
        width = size[0]
        heigh = size[1]
        num = 0
        for i in range(row):
            for j in range(column):
                region = (j*width/column, i*heigh/row, (j+1)*width/column, (i+1)*heigh/row)
                #裁切图片
                cropImg = img.crop(region)

                #保存裁切后的图片
                cropImg.save(open(os.path.dirname(__file__) + \
                                  '/{}_aftercut/{}_{}.png'.format(dirname, newname, num), 'wb'), 'png')
                num += 1
    return None


if __name__ == '__main__':
    path = input('please input the dirname:')
    row = int(path[0])
    column = int(path[2])
    os.mkdir(os.path.dirname(__file__) + '/' + path + '_aftercut')
    cutimage(path, row, column)

