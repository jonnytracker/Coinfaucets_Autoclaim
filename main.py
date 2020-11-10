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

counter = 0
global claim

def visit_site_xrp():
    print("Visiting site xrp")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userXRP']
    password = login['passXRP']

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
    print("Visited site XRP successfully")


def visit_site_cardano():
    print("Visiting site cardano")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userADA']
    password = login['passADA']
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://freecardano.com/")
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
    print("Visited site Cardano successfully")

def visit_site_tron():
    print("Visiting site Tron")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userTRON']
    password = login['passTRON']
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://free-tron.com/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")
        time.sleep(5)
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
            time.sleep(5)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            time.sleep(5)
            driver.quit()
    print("Visited site Tron successfully")


def visit_site_dash():
    print("Visiting site Dash")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userDASH']
    password = login['passDASH']
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://freedash.io/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")
        time.sleep(5)
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
            time.sleep(5)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            time.sleep(5)
            driver.quit()
    print("Visited site Dash successfully")

def visit_site_eth():
    print("Visiting site ETH")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userETH']
    password = login['passETH']
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://freeethereum.com/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")
        time.sleep(5)
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
            time.sleep(5)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            time.sleep(5)
            driver.quit()
    print("Visited site ETH successfully")


def visit_site_nem():
    print("Visiting site nem")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userNEM']
    password = login['passNEM']
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://freenem.com/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")
        time.sleep(5)
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
            time.sleep(5)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            time.sleep(5)
            driver.quit()
    print("Visited site NEM successfully")


def visit_site_neo():
    print("Visiting site neo")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userNEO']
    password = login['passNEO']
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://freeneo.io/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")
        time.sleep(5)
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
            time.sleep(5)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            time.sleep(5)
            driver.quit()
    print("Visited site NEO successfully")


def visit_site_link():
    print("Visiting site link")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userLINK']
    password = login['passLINK']
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://freechain.link/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")
        time.sleep(5)
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
            time.sleep(5)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            time.sleep(5)
            driver.quit()
    print("Visited site LINK successfully")


while True:
   visit_site_xrp()
   time.sleep(5)
   visit_site_cardano()
   time.sleep(5)
   visit_site_tron()
   time.sleep(5)
   visit_site_dash()
   time.sleep(5)
   visit_site_eth()
   time.sleep(5)
   visit_site_nem()
   time.sleep(5)
   visit_site_neo()
   time.sleep(5)
   visit_site_link()
   time.sleep(5)


   print("waiting about an hour")
   time.sleep(3600) #seconds to hour
   counter += 1
   print("wait finished " + "Run Times: " + str(counter))





