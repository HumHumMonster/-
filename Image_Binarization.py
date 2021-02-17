from PIL import Image

# 二值化，tresold是阈值，灰度值小于阈值像素值为0.否则为1
def get_bin_table(thresold = 170):
    table = []
    for i in range(256):
        if i < thresold:
            table.append(0)
        else:
            table.append(1)
    return table # 得到的一个list，其0~thresold-1项为0，thresold~255项为1

def image_bin(now_image) :
    # 灰度化
    now_image = now_image.convert("L")
    # 二值化
    table = get_bin_table()
    now_image = now_image.point(table , '1')
    return now_image