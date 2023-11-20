import time
import unittest


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
HALF_SECOND = 0.5
PATH = 'C:\\Users\\User\\Desktop\\python_course\\module\\driver\\chromedriver.exe'


class Fullstack(unittest.TestCase):
    def setUp(self) -> None:
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(PATH), options=options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print(f"Ending test for {self.driver}")

    def test_wikipedia(self):
        self.driver.get("https://www.wikipedia.org/")
        print("Getting url...")
        slogan = self.driver.find_element(By.CLASS_NAME, "localized-slogan")
        print(slogan)
        print("ID: -> ", slogan.get_property("id"))
        print("link.text: -> ", slogan.text)

        text_to_write = "FullStack programming"
        search_input = self.driver.find_element(By.ID, "searchInput")
        search_input.send_keys(text_to_write)
        time.sleep(HALF_SECOND)
        btn = self.driver.find_element(By.CLASS_NAME, "svg-search-icon")
        btn.click()
        time.sleep(HALF_SECOND*2)
        expected_heading = self.driver.find_element(By.ID, "firstHeading")
        assert expected_heading.text == "Результаты поиска"
        assert "Результаты поиска" in self.driver.page_source

    # def test_facebook(self):
    #     self.driver.get(
    #         'https://www.facebook.com/r.php?locale=ru_RU&display=page')
    #     slogan = self.driver.find_element(
    #         By.CLASS_NAME, "_52lr _9bq0 fsm fwn fcg")
    #     print(slogan)
    #     search_input = self.driver.find_element(
    #         By.ID, "u_0_b_MG")
    #     search_input.send_keys('Abrorxon')
    #     search_input_2 = self.driver.find_element(
    #         By.ID, "u_0_d_em")
    #     search_input_2.send_keys('Abrorov')
    #     search_input_3 = self.driver.find_element(
    #         By.ID, "u_0_g_Ua")
    #     search_input_3.send_keys('ppvbuyppv@gmail.com')
    #     search_input_4 = self.driver.find_element(
    #         By.ID, "password_step_input")
    #     search_input_4.send_keys('Candy00$')
    #     search_input_5 = self.driver.find_element(By.CLASS_NAME, "_58mt")
    #     search_input_5.click()
    #     # search_input_6 = self.driver.find_element(By.ID, "day")
    #     # search_input_6.
    #     # search_input_7 = self.driver.find_element(By.ID, "month")
    #     # search_input_7.
    #     # search_input_8 = self.driver.find_element(By.ID, "year")
    #     # search_input_8.
    #     btn = self.driver.find_element(
    #         By.CLASS_NAME, "_6j mvm _6wk _6wl _58mi _6o _6v")
    #     btn.click()

    #     assert search_input not in self.driver.page_source


# to run this test from command line:
# python -m unittest -v functional_tests.py
# -v  =>  verbose mode  (means that we will see all the output from the test)
# -m  =>  module  (means that we will run the test from the module)
