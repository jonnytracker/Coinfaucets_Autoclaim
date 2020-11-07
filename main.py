from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import json
import schedule
import undetected_chromedriver as uc


PATH = "C:\Program Files (x86)\chromedriver.exe"
counter = 0
global claim

login = json.load(open('Login.json'))
username = login['user']
password = login['pass']




def visit_site():
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://coinfaucet.io/free")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")
        time.sleep(2)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)
        time.sleep(10)
        driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        time.sleep(5)
        try:
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
            print("roll success clicked after login")
            claim += 1
            time.sleep(2)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            time.sleep(2)
            driver.quit()

while True:
   visit_site()
   print("waiting about an hour")
   time.sleep(1800) #wait 30 minutes
   counter += 1
   print("wait finished " + "Run Times: " + str(counter))





