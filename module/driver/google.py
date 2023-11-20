from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://google.com')
input_google = driver.find_element(By.NAME, 'q')
input_google.send_keys('Iphone')
input_google.send_keys(Keys.RETURN)
# expected_text = 'iphone - Поиск в Google'
# assert expected_text.lower() in driver.title.lower()

html = driver.find_element(By.TAG_NAME, 'html')
for i in range(3):
    html.send_keys(Keys.DOWN)
time.sleep(1)

for i in range(3):
    html.send_keys(Keys.DOWN)
time.sleep(1)

for i in range(3):
    html.send_keys(Keys.DOWN)
time.sleep(1)
    
for i in range(3):
    html.send_keys(Keys.DOWN)    
time.sleep(1)

for i in range(3):
    html.send_keys(Keys.DOWN)    
time.sleep(3)
    
driver.close()
driver.quit()