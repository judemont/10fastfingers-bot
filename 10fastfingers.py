from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()



driver.get("https://10fastfingers.com/typing-test/english")

while(driver.title != "Typing Test English - 10FastFingers.com"):
    pass

time.sleep(0.5)
cookieButon  = driver.find_element(By.ID, "CybotCookiebotDialogBodyButtonDecline")

cookieButon.click()

print("Cookie popup passed")




input = driver.find_element(By.ID, "inputfield")

startTime = time.time()



time.sleep(5)

while(time.time() - startTime < 60):
    try:
        time.sleep(0.1)
        word = driver.find_element(By.CLASS_NAME, "highlight").text

        input.send_keys(word)
        input.send_keys(Keys.SPACE)
    except:
        pass


