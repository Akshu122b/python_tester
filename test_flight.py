from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class TestLogin():
    @pytest.fixture()
    def setup(self):
        self.driver= webdriver.Chrome(ChromeDriverManager)  # type: ignore
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homepageTitle(self, setup):
        self.driver.get("http://127.0.0.1:8000/")
        assert self.driver.title=='flight'

    def test_login(self, setup):
        self.driver.find_element('type','username').send_keys("akshata")
        self.driver.find_element('type',"password").send_keys("1234")
       
        # self.driver.find_element("submit").click()
        assert self.driver.title=='flight'