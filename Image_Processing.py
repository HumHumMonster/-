import Image_Binarization
import Image_Denoising
import os
from PIL import Image

p = os.listdir(r"yzm/")
for i in p :
    now_image = Image.open(r"./yzm/" + i)
    now_image = Image_Binarization.image_bin(now_image)
    # now_image.show()
    now_image = Image_Denoising.clear_noise(now_image) #去噪
    # now_image.show()
    now_image = Image_Denoising.clear_noise(now_image) #去噪
    # now_image.show()
    now_image.save(r"./yzm/" + i)