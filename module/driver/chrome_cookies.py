from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
import time

driver = webdriver.Chrome()
driver.get('https://instagram.com')
time.sleep(1)

# email_input = driver.find_element(
#     By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('__abrorxon__')
# password_input = driver.find_element(
#     By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('candy0040')
# enten_btn = driver.find_element(
#     By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.RETURN)
# time.sleep(5)

# pickle.dump(driver.get_cookies(), open(f'instagram_login_cookies', 'wb'))

# ne_seychas = driver.find_element(
#     By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').send_keys(Keys.ENTER)
# time.sleep(0.5)
 
# ne_seychas_2 = driver.find_element(
#     By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
# time.sleep(25)

for cookie in pickle.load(open(f'instagram_login_cookies', 'rb')):
    driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(10)