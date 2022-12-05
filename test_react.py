from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
class TestLogin():
    @pytest.fixture()
    def setup(self):
        self.driver= webdriver.Chrome()  # type: ignore
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homepageTitle(self, setup):
        self.driver.get("http://localhost:3000/")
        time.sleep(2)
        a=ActionChains(self.driver)
        self.driver.find_element(By.XPATH,"//*[@id='Header_navigation__FIn3u']/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div[2]/form/div[1]/input").send_keys("akshata")
        self.driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div[2]/form/div[2]/input").send_keys("1234")
        self.driver.find_element("submit").click()
        time.sleep(2)