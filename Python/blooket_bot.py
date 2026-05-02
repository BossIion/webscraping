import os
#from webbrowser import Chrome
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


import pyautogui as pg
import time


beta_chrome_path = "c:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
gameIDXPATH = r"/html/body/main/div/form/div[1]/div/div/input"
gameIDSubmitXPATH = r"/html/body/main/div/form/div[1]/div/div/button"
nicknameSumbitXPATH = r"/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/button"
nicknameXPATH = r"/html/body/div/div/div/div[2]/div/form/div[2]/div[1]/input"
errorXPATH = r"/html/body/section/div/div/div[1]"




def getGameID():
    gameID = ""
    while type(gameID) != int:
        try:
            user_input = str(pg.prompt(text="Input Blooket Game ID", title="Input Game ID", default = '')).strip()
            gameID = int(user_input)
        except:
            pg.alert(text="Invalid Game ID, try again", title="Invalid Game ID", button="OK")


gameID = getGameID()
verifiedGameID = False

#service = Service(executable_path=beta_chrome_path)

#options = uc.ChromeOptions()
driver = uc.Chrome()

wait = WebDriverWait(driver, 10)

driver.get("https://play.blooket.com/play")


ID_SubmitButton = wait.until(EC.element_to_be_clickable((By.XPATH, gameIDSubmitXPATH)))
ID_input_box = driver.find_element(By.XPATH, gameIDXPATH)
ID_input_box.clear()
for char in str(gameID):
    ID_input_box.send_keys(char)
    time.sleep(0.2)
ID_SubmitButton.click()

driver.quit()
