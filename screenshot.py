#!/usr/bin/python3
import os
import time
from selenium import webdriver

# Create output folder if does not exist
dirName = "out"
if not os.path.exists(dirName):
    os.makedirs(dirName)

url = "https://kso.etjanster.lantmateriet.se/?e=535815&n=6459250&z=9&profile=default_background_noauth"
fileName = "out.png"

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.set_window_size(2000,2000)
driver.get(url)
time.sleep(1)
driver.save_screenshot(dirName + "/" + fileName)
driver.quit()
