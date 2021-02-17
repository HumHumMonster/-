import os
from PIL import Image
# 根据选取规则得到图像特征值
def get_all_eigen_b(image):
    res = [0 for i in range(17)]
    sum_pixel = 0
    for i in range(4):
        for j in range(4):
            now_image = image.crop((j*4,i*6,(j+1)*4,(i+1)*6)) # 分割图像
            now_pixel = 0
            for x in range(now_image.size[0]):
                for y in range(now_image.size[1]):
                    if now_image.getpixel((x,y))==0:
                        now_pixel += 1 # 计算黑色点数量
            res[i*4+j] = now_pixel/24 # 计算黑色点比例
            sum_pixel += now_pixel
    res[16] = sum_pixel/384
    return res

char_vectors = {}
divide_path = r"divide/"

def save_vectors():
    for i in os.listdir(divide_path) :
        char_vectors[i] = []
    for key in char_vectors:
        for x in os.listdir(divide_path + key):
            now_png = str(x)
            if now_png[-4:]==".png":
                image = Image.open(divide_path + key + "/" + now_png, "r") # 打开一张图片
                char_vectors[key].append(get_all_eigen_b(image)) # 黑点比例作为特征值
        fp = open(divide_path + key + "/vectors.txt", "w") # 保存
        for i in range(len(char_vectors[key])):
            for j in range(len(char_vectors[key][i])):
                fp.write(str(char_vectors[key][i][j]))
                fp.write(" ")
            fp.write("\n")
        fp.close()

save_vectors()