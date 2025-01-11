from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()
url= "https://web.telegram.org/k"
driver.get(url)
time.sleep(8)
loginClick = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/button[1]")
loginClick.click()
time.sleep(1)
loginPhone = driver.find_element(By.XPATH , "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]")
loginPhone.send_keys("5418640498")
time.sleep(1)
nextButton = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/button[1]/div[1]")
nextButton.click()
time.sleep(1)
code = input("Lütfen Kodu Gir: ")
giris = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[3]/div[1]/input[1]")
giris.send_keys(code)
time.sleep(5)
smsbotlink = "https://web.telegram.org/k/#@sms_recieve_bot"
driver.get(smsbotlink)
time.sleep(2)
chat = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[8]/div[2]/div[1]")
chat.send_keys("/start")
send = driver.find_element(By.XPATH ,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[5]/button[1]/div[1]")
send.click()
chat.send_keys("/get yemeksepeti")
send.click()
time.sleep(1000)
