#!/usr/bin/python3

import os
from time import sleep
from selenium import webdriver

# Create output folder if does not exist
dirName = "out"
if not os.path.exists(dirName):
    os.makedirs(dirName)

url = "http://balticmaps.eu/?lang=lv&draw_hash=dteamu&centerx=576912.270312722&centery=6349087.28387397&zoom=5&layer=map&ls=o"
fileName = "out.png"

browser = webdriver.PhantomJS()
browser.set_window_size(2000,2000)
browser.get(url)
sleep(10)
browser.save_screenshot(dirName + "/" + fileName)
browser.quit()
