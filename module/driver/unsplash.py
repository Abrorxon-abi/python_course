from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://unsplash.com')

time.sleep(1)
btn_input = driver.find_element(
    By.XPATH, '//*[@id="popover-visual-search-form-nav"]/button').send_keys(Keys.ENTER)
time.sleep(0.5)

img_input = driver.find_element(By.CLASS_NAME, 'RdTIh').send_keys(
    r'C:\Users\User\Desktop\python_course\module\driver\1.jpg')
time.sleep(10)
