import os
#from webbrowser import Chrome
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pyautogui as pg
import time

if __name__ == "__main__":
    beta_chrome_path = r"C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
    gameIDXPATH = r"/html/body/main/div/form/div[1]/div/div/input"
    gameIDSubmitXPATH = r"/html/body/main/div/form/div[1]/div/button"
    nicknameSumbitXPATH = r"/html/body/div/div/div/div[2]/div/form/div[2]/div[2]"
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
        return gameID


    gameID = getGameID()
    verifiedGameID = False

    options = uc.ChromeOptions()
    driver = uc.Chrome(browser_executable_path=beta_chrome_path, options=options)

    wait = WebDriverWait(driver, 10)

    driver.get("https://play.blooket.com/play")


    ID_SubmitButton = wait.until(EC.element_to_be_clickable((By.XPATH, gameIDSubmitXPATH)))
    ID_input_box = wait.until(EC.element_to_be_clickable((By.XPATH, gameIDXPATH)))
    ID_input_box.clear()
    for char in str(gameID):
        ID_input_box.send_keys(char)
        time.sleep(0.2)
    ID_SubmitButton.click()

    # Verify Game ID

    try:
        error = driver.find_element(By.XPATH, errorXPATH)
        if error.is_displayed():
            verifiedGameID = False
            pg.alert(text="Invalid Game ID, try again", title="Invalid Game ID", button="OK")
    except:
        verifiedGameID = True

    if verifiedGameID:
        nickname_input_box = wait.until(EC.element_to_be_clickable((By.XPATH, nicknameXPATH)))
        nickname_submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, nicknameSumbitXPATH)))

        nickname = "TESTESTESTEST"

        nickname_input_box.clear()
        for char in nickname:
            nickname_input_box.send_keys(char)
            time.sleep(0.2)
        nickname_submit_button.click()

    driver.quit()
