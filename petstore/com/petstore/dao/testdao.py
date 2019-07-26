import os

print('***获取上上级目录***')
print(os.path.join(os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../../..")), 'resources\icon\\dog.jpg')))
print(os.path.join(os.path.abspath(os.path.join(os.getcwd(), '../../..')), 'resources\icon\\image\\' + 'img1.jpg'))
'''


print('***获取上级目录***')
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))


print(os.path.abspath(os.path.join(os.getcwd(), "../../..")))
'''
