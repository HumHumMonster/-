from PIL import Image
from PIL import ImageDraw



# 判断某个点是否超出了图的边界
def isvalid(image, x, y):
    if x < 0 or x >= image.size[0] or y < 0 or y >= image.size[1]:
        return False
    return True

after_table = [[0 for x in range(89)] for x in range(33)]

# 判断某个点是否为噪点，after_table_b用于描点画图，可以改变level以调节去噪深度
def clear_noise_pixel_binary(image, x, y, level):
    # 检索指定坐标点的像素的RGB颜色值
    now = image.getpixel((x,y))
    flag = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0:
                continue
            if isvalid(image, x+i, y+j):
                if image.getpixel((x+i,y+j))==0:
                    flag+=1 # 计算该点周围黑色点的数量
    if now == 0 and flag<level:
        after_table[y][x] = 1 # 去除操作，若该点为黑点，且周围黑点的数量小于level，则将该点变为白点
    # elif now==1 and flag>=4:
    #     after_table[y][x] = 0 # 补充操作，若该点为白点，且周围黑点的数量大于等于4，则将该点变为黑点
    else:
        after_table[y][x] = now

# 总的去噪函数
def clear_noise(image):
    draw = ImageDraw.Draw(image)
    for k in range(1):
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                    clear_noise_pixel_binary(image,i,j,2)
    try:
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                draw.point((i,j) , after_table[j][i])
    except Exception as e:
        print(e)
    return image