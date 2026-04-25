import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
import time

def resetDir():
    fileName = __file__
    if type(fileName.split("\\")) == list and len(fileName.split("\\")) > 1:
        fileName = fileName.split("\\")[-1]
        filePath = __file__.replace(fileName,"")
    else:
        fileName = fileName.split("/")[-1]
        filePath = __file__.replace(fileName,"")
    os.chdir(filePath)
    return os.path.abspath(filePath)

resetDir()


opts = FirefoxOptions()

opts.add_argument("--headless")

driver = webdriver.Firefox(options=opts)

driver.get("https://apod.nasa.gov/apod/astropix.html")
time.sleep(2)

text = driver.find_element(By.XPATH, "/html/body/center[2]/b[1]").text.strip()
print(text)
image = driver.find_element(By.XPATH, "/html/body/center[1]/p[2]/a").click()

img = driver.find_element(By.TAG_NAME, "img")

with open(f"Images/SELENIUM_{text}.png","wb") as f:
    f.write(img.screenshot_as_png )

driver.close()

