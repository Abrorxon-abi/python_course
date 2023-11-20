from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


PATH = 'C:\\Users\\User\\Desktop\\python_course\\module\\driver\\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('user-agent=HelloWorld!')

driver = webdriver.Chrome(
    service=Service(PATH),
    options=options)
# url = 'https://www.instagram.com/'
url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'


try:
    driver.get(url=url)
    time.sleep(15)
    # driver.refresh()
    # driver.get_screenshot_as_file('1.png')
    # driver.save_screenshot('2.png')
    # driver.get(url='https://stackoverflow.com/')
    # time.sleep(2)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
