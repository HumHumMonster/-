import os
divide_path =  "./div/" # 分割后的验证码路径
# 在路径下新建文件夹，名字为a-z,0-9,用于存储分割后的验证码
for i in range(26):
    if not os.path.exists(divide_path + chr(i+97) + 'l'):
        os.mkdir(divide_path + chr(i+97) + 'l')
    if not os.path.exists(divide_path + chr(i+97) + 'm'):
        os.mkdir(divide_path + chr(i+97) + 'm')
    if not os.path.exists(divide_path + chr(i+97) + 'r'):
        os.mkdir(divide_path + chr(i+97) + 'r')
for j in range(10):
    if not os.path.exists(divide_path + str(j) + 'l'):
        os.mkdir(divide_path + str(j) + 'l')
    if not os.path.exists(divide_path + str(j) + 'm'):
        os.mkdir(divide_path + str(j) + 'm')
    if not os.path.exists(divide_path + str(j) + 'r'):
        os.mkdir(divide_path + str(j) + 'r')


