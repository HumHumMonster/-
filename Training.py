from selenium import webdriver
import os
from PIL import Image
import random
from pykeyboard import PyKeyboard
import time

import Identification

browser = webdriver.Chrome()
yonghumin = "1717000110"
mima = "zhx980906"

cnt_yes = 0
cnt_no = 0

browser.get("http://210.40.2.253:8888/default2.aspx")

for i in os.listdir(r"./yzm") :
    os.remove(r'./yzm/' + i)


while True :
    print ("成功次数" , cnt_yes)
    print("失败次数" , cnt_no)
    new_vector = []
    name = './yzm/' + str(random.random()) + '.png'
    browser.get_screenshot_as_file(name)
    img = Image.open(name)
    img = img.crop((917, 346, 1006, 379))
    img.save(name)

    os.system(r'python ./Image_Processing.py')

    yanzhenma = ""
    image_save = []
    for i in os.listdir(r"./yzm"):
        now_image = Image.open(r"./yzm/" + i)
        # now_image.show()
        for j in range(4):
            child_image = now_image.crop((6 + 15 * j, 1, 6 + 15 * (j + 1), 28))
            image_save.append(child_image)
            new_vector.append(Identification.identify(child_image))
            yanzhenma += new_vector[-1][0]
        print(yanzhenma)

    os.remove(name)

    browser.find_element_by_xpath("/html/body/form/div/div[3]/dl[1]/dd/input").send_keys(' ')
    k = PyKeyboard()
    k.press_key(k.control_key)
    k.press_key('a')
    k.tap_key(k.delete_key)
    k.release_key('a')
    k.release_key(k.control_key)
    for i in yonghumin :
        k.tap_key(i)
    k.tap_key(k.tab_key)
    k.tap_key(k.tab_key)
    for i in mima:
        k.tap_key(i)
    k.tap_key(k.tab_key)
    for i in yanzhenma:
        k.tap_key(i)
    k.tap_key(k.enter_key)
    time.sleep(1)
    try:
        if len(browser.page_source) > 5:
            print("成功！")
            cnt_yes += 1
            browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/form/div/ul/li[2]/a').click()
            for i in range(4):
                image_save[i].save(r'./divide/' + new_vector[i] + r'/' + str(random.random()) + '.png')
        else:
            print("失败！")
            cnt_no += 1
            k.tap_key(k.enter_key)
    except:
        print("失败！")
        cnt_no += 1
        k.tap_key(k.enter_key)

