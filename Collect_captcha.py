from selenium import webdriver
from PIL import Image
import random
import urllib.request

browser = webdriver.Chrome()

browser.get("http://210.40.2.253:8888/default2.aspx")
for i in range(200) :
    name = './yzm/' + str(random.random()) + '.png'
    print(name)
    browser.get_screenshot_as_file(name)

    img = Image.open(name)
    img = img.crop((917 , 346 , 1006 , 379))
    img.save(name)

    element = browser.find_element_by_id("icode")
    element.click()