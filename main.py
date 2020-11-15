from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time, random
import json
import undetected_chromedriver as uc
import telegram
from selenium.webdriver.common.action_chains import ActionChains


with open('TelegramBot.json', 'r') as file:
    botinfo = json.load(file)
    file.close()

token = botinfo['TOKEN']
id = botinfo['CHATID']
bot = telegram.Bot(token=token)

counter = 0
global claim


def visit_site_xrp():
    print("Visiting site xrp")
    bot.send_message(chat_id=id, text="Visiting XRP site")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userXRP']
    password = login['passXRP']

    #driver = webdriver.Chrome(PATH)
    opts = uc.ChromeOptions()
    opts.add_argument('--disable-notifications')
    #opts.add_extension("extension_3_9_5_0.crx")
    driver = uc.Chrome(options=opts)
    driver.set_page_load_timeout(120)
    #driver.get('chrome://settings/')
    #driver.execute_script('chrome.settingsPrivate.setDefaultZoom(.7);')


    try:
        driver.get("https://coinfaucet.io/free")

    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    time.sleep(5)

    try:

        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")
        time.sleep(5)
        #send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(2)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)
        time.sleep(5)


        #try login click if fail close the ads iframe
        try:
            #try login click
            driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        except:
            print("login button click fail")
            #close ads since login fail
            driver.find_element_by_xpath("//*[@id='fbf-mobile-close-coinzilla']").click()

            try:
                #try login after ads close
                print("trying login again")
                driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
                print("login successful")
            except:
                #if fail again close
                print("login fail quitting ")
                time.sleep(5)
                driver.quit()

    time.sleep(5)

    #if on login success main page. Print we are on roll page
    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'THIS GAME IS PROVABLY FAIR!')]")))
        print("We are on roll page")

    except:
        print("login fail")


    #now click the roll button
    try:
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll success clicked after login")
        time.sleep(5)
        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)
        claim += 1
        time.sleep(2)
        driver.quit()

    except:
        print("already clicked wait more minutes")
        bot.send_message(chat_id=id, text="Already Claimed")
        time.sleep(2)
        driver.quit()
    print("Visited site XRP successfully")


def visit_site_cardano():
    print("Visiting site cardano")
    bot.send_message(chat_id=id, text="Visiting site Cardano")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userADA']
    password = login['passADA']
    opts = uc.ChromeOptions()
    opts.add_argument('--disable-notifications')
    # opts.add_extension("extension_3_9_5_0.crx")
    driver = uc.Chrome(options=opts)
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://freecardano.com/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(5)
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
        time.sleep(5)

        # try login click if fail close the ads iframe
        try:
            # try login click
            driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        except:
            print("login button click fail")
            # close ads since login fail
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()

            try:
                # try login after ads close
                print("trying login again")
                driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
                print("login successful")
            except:
                # if fail again close
                print("login fail quitting ")
                time.sleep(5)
                driver.quit()

    try:
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'THIS GAME IS PROVABLY FAIR!')]")))
        print("login success")
    except:
        print("login fail")


    #on login success click the roll button now
    try:
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll success clicked after login")

        claim += 1
        time.sleep(2)
        driver.quit()

    except:
        print("already clicked wait more minutes")
        bot.send_message(chat_id=id, text="Already Claimed")
        time.sleep(2)
        driver.quit()

    print("Visited site Cardano successfully")
    driver.quit()


def visit_site_tron():
    print("Visiting site Tron")
    bot.send_message(chat_id=id, text="Visiting site Tron")

    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userTRON']
    password = login['passTRON']
    opts = uc.ChromeOptions()
    opts.add_argument('--disable-notifications')
    # opts.add_extension("extension_3_9_5_0.crx")
    driver = uc.Chrome(options=opts)
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

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(5)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)

        # try login click if fail close the ads iframe
        try:
            # try login click
            driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        except:
            print("login button click fail")
            # close ads since login fail
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()

            try:
                # try login after ads close
                print("trying login again")
                driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
                print("login successful")
            except:
                # if fail again close
                print("login fail quitting ")
                time.sleep(5)
                driver.quit()

    try:
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll success clicked after login")

        time.sleep(5)

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        claim += 1
        time.sleep(5)
        driver.quit()

    except:
        print("already clicked wait more minutes")
        bot.send_message(chat_id=id, text="Already Claimed")
        time.sleep(5)
        driver.quit()

    print("Visited site Tron successfully")
    driver.quit()


def visit_site_dash():
    print("Visiting site Dash")
    bot.send_message(chat_id=id, text="Visiting site Dash")

    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userDASH']
    password = login['passDASH']

    opts = uc.ChromeOptions()
    opts.add_argument('--disable-notifications')
    # opts.add_extension("extension_3_9_5_0.crx")
    driver = uc.Chrome(options=opts)
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

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(5)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)
        # try login click if fail close the ads iframe
        try:
            # try login click
            driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        except:
            print("login button click fail")
            # close ads since login fail
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()

            try:
                # try login after ads close
                print("trying login again")
                driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
                print("login successful")
            except:
                # if fail again close
                print("login fail quitting ")
                time.sleep(5)
                driver.quit()

    try:
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll success clicked after login")

        time.sleep(5)

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        claim += 1
        time.sleep(5)
        driver.quit()

    except:
        print("already clicked wait more minutes")
        bot.send_message(chat_id=id, text="Already Claimed")
        time.sleep(5)
        driver.quit()

    print("Visited site Dash successfully")
    driver.quit()



def visit_site_eth():
    print("Visiting site ETH")
    bot.send_message(chat_id=id, text="Visiting site ETH")

    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userETH']
    password = login['passETH']

    opts = uc.ChromeOptions()
    opts.add_argument('--disable-notifications')
    # opts.add_extension("extension_3_9_5_0.crx")
    driver = uc.Chrome(options=opts)
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

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(5)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)

        # try login click if fail close the ads iframe
        try:
            # try login click
            driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        except:
            print("login button click fail")
            # close ads since login fail
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()

            try:
                # try login after ads close
                print("trying login again")
                driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
                print("login successful")
            except:
                # if fail again close
                print("login fail quitting ")
                time.sleep(5)
                driver.quit()

    try:
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll success clicked after login")

        time.sleep(5)

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        claim += 1
        time.sleep(5)
        driver.quit()

    except:
        print("already clicked wait more minutes")
        bot.send_message(chat_id=id, text="Already Claimed")
        time.sleep(5)
        driver.quit()

    print("Visited site ETH successfully")
    driver.quit()



def visit_site_nem():
    print("Visiting site nem")
    bot.send_message(chat_id=id, text="Visiting site NEM")

    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userNEM']
    password = login['passNEM']

    opts = uc.ChromeOptions()
    opts.add_argument('--disable-notifications')
    # opts.add_extension("extension_3_9_5_0.crx")
    driver = uc.Chrome(options=opts)
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

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(5)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)

        # try login click if fail close the ads iframe
        try:
            # try login click
            driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        except:
            print("login button click fail")
            # close ads since login fail
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()

            try:
                # try login after ads close
                print("trying login again")
                driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
                print("login successful")
            except:
                # if fail again close
                print("login fail quitting ")
                time.sleep(5)
                driver.quit()

    try:
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll success clicked after login")

        time.sleep(5)

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        claim += 1
        time.sleep(5)
        driver.quit()

    except:
        print("already clicked wait more minutes")
        bot.send_message(chat_id=id, text="Already Claimed")
        time.sleep(5)
        driver.quit()

    print("Visited site NEM successfully")
    driver.quit()



def visit_site_neo():
    print("Visiting site neo")
    bot.send_message(chat_id=id, text="Visiting site NEO")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userNEO']
    password = login['passNEO']

    opts = uc.ChromeOptions()
    opts.add_argument('--disable-notifications')
    # opts.add_extension("extension_3_9_5_0.crx")
    driver = uc.Chrome(options=opts)
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

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(5)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)

        # try login click if fail close the ads iframe
        try:
            # try login click
            driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        except:
            print("login button click fail")
            # close ads since login fail
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()

            try:
                # try login after ads close
                print("trying login again")
                driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
                print("login successful")
            except:
                # if fail again close
                print("login fail quitting ")
                time.sleep(5)
                driver.quit()

    try:
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll success clicked after login")

        time.sleep(5)

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        claim += 1
        time.sleep(5)
        driver.quit()

    except:
        print("already clicked wait more minutes")
        bot.send_message(chat_id=id, text="Already Claimed")
        time.sleep(5)
        driver.quit()

    print("Visited site NEO successfully")
    driver.quit()



def visit_site_link():
    print("Visiting site link")
    bot.send_message(chat_id=id, text="Visiting site LINK")

    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userLINK']
    password = login['passLINK']

    opts = uc.ChromeOptions()
    opts.add_argument('--disable-notifications')
    # opts.add_extension("extension_3_9_5_0.crx")
    driver = uc.Chrome(options=opts)
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

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(5)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)

        # try login click if fail close the ads iframe
        try:
            # try login click
            driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        except:
            print("login button click fail")
            # close ads since login fail
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()

            try:
                # try login after ads close
                print("trying login again")
                driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
                print("login successful")
            except:
                # if fail again close
                print("login fail quitting ")
                time.sleep(5)
                driver.quit()

    try:
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll success clicked after login")

        time.sleep(5)

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        claim += 1
        time.sleep(5)
        driver.quit()

    except:
        print("already clicked wait more minutes")
        bot.send_message(chat_id=id, text="Already Claimed")
        time.sleep(5)
        driver.quit()

    print("Visited site LINK successfully")
    driver.quit()


def visit_site_binanceCoin():
    print("Visiting site BinanceCoin")
    bot.send_message(chat_id=id, text="Visiting site BinanceCoin")

    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userBNB']
    password = login['passBNB']

    opts = uc.ChromeOptions()
    opts.add_argument('--disable-notifications')
    # opts.add_extension("extension_3_9_5_0.crx")
    driver = uc.Chrome(options=opts)
    driver.set_page_load_timeout(120)

    try:
        driver.get("https://freebinancecoin.com/")
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

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(5)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)

        # try login click if fail close the ads iframe
        try:
            # try login click
            driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        except:
            print("login button click fail")
            # close ads since login fail
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()

            try:
                # try login after ads close
                print("trying login again")
                driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
                print("login successful")
            except:
                # if fail again close
                print("login fail quitting ")
                time.sleep(5)
                driver.quit()

    try:
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll success clicked after login")

        time.sleep(5)

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        claim += 1
        time.sleep(5)
        driver.quit()

    except:
        print("already clicked wait more minutes")
        bot.send_message(chat_id=id, text="Already Claimed")
        time.sleep(5)
        driver.quit()

    print("Visited site BinanceCoin successfully")
    driver.quit()




while True:
    rand = random.randrange(1,10)   
    time.sleep(rand)

    visit_site_xrp()

    rand = random.randrange(1,10)   
    time.sleep(rand)

    visit_site_cardano()

    rand = random.randrange(1,10)   
    time.sleep(rand)

    visit_site_tron()

    rand = random.randrange(1,10)   
    time.sleep(rand)

    rand = random.randrange(1,10)   
    time.sleep(rand)

    visit_site_dash()

    rand = random.randrange(1,10)   
    time.sleep(rand)

    visit_site_eth()

    rand = random.randrange(1,10)   
    time.sleep(rand)

    visit_site_nem()

    rand = random.randrange(1,10)   
    time.sleep(rand)

    visit_site_neo()

    rand = random.randrange(1,10)   
    time.sleep(rand)

    visit_site_link()

    rand = random.randrange(1,10)   
    time.sleep(rand)

    visit_site_binanceCoin()

    rand = random.randrange(1,10)   
    time.sleep(rand)

    bot.send_message(chat_id=id, text="Waiting About an Hour...")
    print("waiting about an hour")

    rand = random.randrange(3600,9000)
    
    time.sleep(rand) #seconds to hour

    counter += 1
    bot.send_message(chat_id=id, text="wait finished " + "Run Times: " + str(counter))
    print("Wait Finished " + "Run Times: " + str(counter))





