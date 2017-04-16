#!/usr/bin/python3
import os
from time import sleep
from selenium import webdriver

# Create output folder if does not exist
dirName = "out"
if not os.path.exists(dirName):
    os.makedirs(dirName)

url = "https://kso.etjanster.lantmateriet.se/?e=535815&n=6459250&z=9&profile=default_background_noauth"
fileName = "out.png"

# browser = webdriver.PhantomJS()
# PhantomJS does not work with Lantmateriet
# Therefore, start Firefox headlessly:
# 1. Install xvfb
# 2. Start it at display 10: `Xvfb :10 -ac &`
# 3. Set display to 10: `export DISPLAY=:10`
# 4. Now run this script from teh same terminal
#
# Source: http://agiletesting.blogspot.se/2016/01/running-selenium-webdriver-tests-using.html

browser = webdriver.Firefox()
browser.set_window_size(2000,2000)
browser.get(url)
sleep(1)
browser.save_screenshot(dirName + "/" + fileName)
browser.quit()
