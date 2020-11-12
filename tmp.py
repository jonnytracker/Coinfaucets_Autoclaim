import selenium
import undetected_chromedriver as uc
import time

driver = uc.Chrome()
driver.get('https://coinfaucet.io/')
time.sleep(5)


iframes = driver.find_elements_by_tag_name("iframe")

time.sleep(5)

for e in iframes:
    try:
        e.find_element_by_xpath("//*[@id='fbf-mobile-close-coinzilla']").click()
        print("found iframe and closed")

    except:
        print("not found iframe")


time.sleep(10)
driver.quit()