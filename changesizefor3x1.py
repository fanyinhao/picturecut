from PIL import Image
import os


def changepngsize(dirname):
    """Change png size"""
    beforcutfilelist = os.listdir(os.path.dirname(__file__)+ '/' + '{}'.format(dirname))
    for filename in beforcutfilelist:
        img = Image.open(os.path.dirname(__file__) + '/' + '{}'.format(dirname) + '/' + filename)
        (x, y) = img.size
        print(x, y)
        # x_s = x
        # y_s = 170
        # print(y_s)
        # out = img.resize((x_s, y_s), Image.ANTIALIAS)
        # out.save(open(os.path.dirname(__file__) + \
        #                 '/afterchangesizefor3x1/{}'.format(filename), 'wb'), 'png')


if __name__ == '__main__':
    path = input('please input the dirname:')
    # os.mkdir('./afterchangesizefor3x1')
    changepngsize(path)