# 文本文件读写  文本文件读写的单位是字符

f_name = 'test.txt'

with open(f_name, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    line = f.read()
    copy_f_name = 'copy.txt'
    with open(copy_f_name, 'w', encoding='utf-8') as copy_f:
        copy_f.writelines(lines)
        print('文件复制成功')

#二进制文件读写

img_name = '1.jpg'
with open(img_name,'rb') as f:
    b = f.read()
    copy_img_name = 'copy1.jpg'
    with open(copy_img_name,'wb') as copy_img:
        copy_img.write(b)
        print('文件复制成功')