import os
from PIL import Image
import random
path = ""

p = os.listdir(r"yzm")
for i in p :
    now_image = Image.open(r"./yzm/" + i)
    now_image.save(r"./now/" + i)
    strr = input().split()
    if strr[0] == 'pass' :
        os.remove(r"./yzm/" + i)
        continue
    for j in range(4) :
        child_image = now_image.crop((6 + 15 * j , 1 , 6 + 15 * (j + 1) , 28))
        child_image.save(r"./divide/" + strr[j] + r'/' + str(random.random()) + '.png')
    os.remove(r"./now/" + i)
    os.remove(r"./yzm/" + i)
