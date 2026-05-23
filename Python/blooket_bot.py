import os
#from webbrowser import Chrome
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pyautogui as pg
import time
import random as r

numberBots = 15
if __name__ == "__main__":

    firstWordList = ["Awesome", "Happy", "Golden", "Rose", "Red", "Blue", "Green", "Yellow", "Purple", "Silver", "Diamond", "Wooden", "Steel", "Bronze", "Copper", "Iron", "Crystal", "Glass", "Plastic", "Paper", "Cardboard", "Cotton", "Wool", "Silk", "Leather", "Rubber", "Stone", "Clay", "Sand", "Snow", "Ice", "Fire", "Water", "Air", "Light", "Dark", "Shadow", "Thunder", "Lightning", "Wind", "Storm", "Cloud", "Sky", "Star", "Moon", "Sun",("Galaxy"), ("Universe"), ("Planet"), ("Comet"), ("Meteor"), ("Asteroid"), ("Rocket"), ("Spaceship"), ("Alien"), ("Robot"), ("Zombie"), ("Vampire"), ("Werewolf"), ("Ghost"), ("Witch"), ("Wizard"), ("Fairy"), ("Giant"), ("Dwarf"), ("Troll"), ("Ogre"), ("Dragon"), ("Phoenix"), ("Unicorn"), ("Mermaid"), ("Centaur"), ("Minotaur")]
    secondWordList = ['Cat', 'Dog', 'Fish', 'Mouse', 'Hamster', 'Rabbit', 'Turtle', 'Snake', 'Lizard', 'Frog', 'Bird', 'Cow', 'Pig', 'Horse', 'Sheep', 'Goat', 'Chicken', 'Duck', 'Bee', 'Ant', 'Spider', 'Butterfly', 'Ladybug', 'Dragonfly', 'Grasshopper', 'Snail',
                       'Worm', 'Octopus', 'Crab', 'Lobster', 'Starfish', 'Jellyfish', 'Coral', 'Seaweed', 'Shark', 
                       'Whale', 'Dolphin', 'Seal', 'Penguin', 'Polar Bear', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Monkey', 'Gorilla', 'Zebra', 'Giraffe', 'Kangaroo']

    beta_chrome_path = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
    gameIDXPATH = r"/html/body/main/div/form/div[1]/div/div/input"
    gameIDSubmitXPATH = r"/html/body/main/div/form/div[1]/div/button"
    nicknameSumbitXPATH = r"/html/body/div/div/div/div[2]/div/form/div[2]/div[2]"
    nicknameXPATH = r"/html/body/div/div/div/div[2]/div/form/div[2]/div[1]/input"
    errorXPATH = r"/html/body/section/div/div/div[1]"

    usedNames = []

    def generateNickname():
        nickname = r.choice(firstWordList) + r.choice(secondWordList)
        while nickname in usedNames:
            nickname = r.choice(firstWordList) + r.choice(secondWordList)
        usedNames.append(nickname)
        return str(nickname)


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
        time.sleep(0.05)
    ID_SubmitButton.click()

    # Verify Game ID

    try:
        
        error = driver.find_element(By.XPATH, errorXPATH)
        if error.is_displayed():
            verifiedGameID = False
            pg.alert(text="Invalid Game ID, try again", title="Invalid Game ID", button="OK")
        else:
            verifiedGameID = True
    except:
        verifiedGameID = True

    if verifiedGameID:
        nickname_input_box = wait.until(EC.element_to_be_clickable((By.XPATH, nicknameXPATH)))
        nickname_submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, nicknameSumbitXPATH)))

        nickname = generateNickname()
        nickname_input_box.clear()
        for char in str(nickname):
            nickname_input_box.send_keys(char)
            time.sleep(0.01)
        nickname_submit_button.click()

    #repeat
    for i in range(numberBots):
        driver.switch_to.new_window('tab')
        driver.get("https://play.blooket.com/play")

        ID_SubmitButton = wait.until(EC.element_to_be_clickable((By.XPATH, gameIDSubmitXPATH)))
        ID_input_box = wait.until(EC.element_to_be_clickable((By.XPATH, gameIDXPATH)))
        ID_input_box.clear()
        for char in str(gameID):
            ID_input_box.send_keys(char)
            time.sleep(0.01)
        ID_SubmitButton.click()

        nickname_input_box = wait.until(EC.element_to_be_clickable((By.XPATH, nicknameXPATH)))
        nickname_submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, nicknameSumbitXPATH)))

        nickname = generateNickname()
        nickname_input_box.clear()
        for char in str(nickname):
            nickname_input_box.send_keys(char)
            time.sleep(0.01)
        nickname_submit_button.click()


input("Press ENTER to close all bots...")