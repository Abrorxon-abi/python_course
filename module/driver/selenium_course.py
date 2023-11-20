from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

PATH = 'C:\\Users\\User\\Desktop\\python_course\\module\\driver\\chromedriver.exe'
url = 'https://tutorialsninja.com/demo/'
driver = webdriver.Chrome(service=Service(PATH))

driver.get(url)
search_field = driver.find_element(By.NAME, 'search')
search_field.send_keys('iphone')
search_field.send_keys(Keys.RETURN)

time.sleep(0.2)


add_to_bag_btn = driver.find_element(
    By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
add_to_bag_btn.click()

time.sleep(0.4)


my_bag = driver.find_element(By.ID, 'cart-total')
my_bag.click()

time.sleep(0.4)


view_cart_btn = driver.find_element(
    By.XPATH, '//*[@id="cart"]/ul/li[2]/div/p/a[1]/strong')
view_cart_btn.click()

time.sleep(0.3)


go_shopping_btn = driver.find_element(
    By.XPATH, '//*[@id="content"]/div[3]/div[1]/a')
go_shopping_btn.click()


time.sleep(1)

assert 'Your Store' in driver.page_source
driver.close()
driver.quit()

pass
