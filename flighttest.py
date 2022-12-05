from selenium import webdriver
# from selenium import ChromeDriveManager
from selenium.webdriver.common.by import By
import time
import unittest
# from exceldatareader import DataReader
class MyTest(unittest.TestCase):
        def setUp(self):
                self.driver=webdriver.Chrome()
        def test_login(self):
                driver=self.driver
                try:
                   driver.get('http://127.0.0.1:8000/')
                   driver.maximize_window()
                   time.sleep(1)
                except Exception as ex:
                        print(ex)
                driver.find_element(By.XPATH,'//a[@href="Loginpage"]').click()
                time.sleep(5)
                username=driver.find_element("name","username").send_keys('rakesh')   
                password=driver.find_element("name",'password').send_keys('123')
                driver.find_element(By.XPATH,'//input[@value="Login"]').click()
                time.sleep(5)
                # else:
                #         time.sleep(1)
                # username=driver.find_element("id","username").send_keys('rakesh')   
                # password=driver.find_element("id",'password').send_keys('123')
                # time.sleep(3)
                # # url = url.encode('ascii', 'ignore').decode('unicode_escape')
                # # uname,pwd=DataReader.readDataForLogin()
                # # username.clear()
                # # pwd.clear()
                # # username.send_keys(uname)
                # # password.send_keys(pwd)
                # # time.sleep()
                # # xpath
                
                # driver.find_element(By.XPATH,'//button[.="Login"]').click()
                # time.sleep(2)
                # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
                # time.sleep(10)
                # from selenium.webdriver.common.action_chains import ActionChains
                # a = ActionChains(driver)
                # # m= driver.find_element("link","/static/scan.webp").click()
                # driver.find_element(By.XPATH,"//div[contains(@class, 'fe-box')]").click()
                # driver.find_element(By.CLASS_NAME,"fe-box").click()
                # time.sleep(10)
                # # a.move_to_element(m).perform()
                
                # # driver.find_element(By.XPATH,'//img[.="img"]').click()
                # # driver.find_element(By.XPATH,'//img[@src="img"][@src="//static/scan.webp"]').click()
                # time.sleep(10)
        def tearDown(self):
                self.driver.quit()
if __name__=="__main__":
        unittest.main()