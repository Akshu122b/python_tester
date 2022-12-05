from selenium import webdriver
# from selenium import ChromeDriveManager
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
# from exceldatareader import DataReader
class MyTest(unittest.TestCase):
        def setUp(self):
                self.driver=webdriver.Chrome()
        def test_login(self):
                driver=self.driver
                try:
                   driver.get('http://localhost:3000/')
                   driver.maximize_window()
                   time.sleep(1)
                except Exception as ex:
                        print(ex)
                # driver.find_element(By.XPATH,"//*[@id='Header_navigation__fe29I']/li[2]/a").click()
                a=ActionChains(driver)
                driver.execute_script("window.scrollTo(0,300);")
                time.sleep(2)
                # driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div[1]/div[1]/div[2]/div/a").click()
                # driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div[2]/div[1]/div[2]/div/a").click()
                
                # driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div[1]")
        ###########           python         ########################
                driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div[1]/div[1]").click()
                driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div[1]/div[1]/div[2]/div/a").click()
                time.sleep(1)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                driver.back()
                time.sleep(2)
        #############     Java      ########################
                # driver.get('http://localhost:3000/')
                driver.refresh()
                a=ActionChains(driver)
                driver.execute_script("window.scrollTo(0,300);")
                time.sleep(2)
                driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[2]").click()
                driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div[2]/div[1]/div[2]/div/a").click()
                time.sleep(2)
        ################ Mern stack ###########################################  
                driver.refresh()
                a=ActionChains(driver)
                driver.execute_script("window.scrollTo(0,300);")
                time.sleep(2)
                # driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[3]/div[1]").click()
                driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div[2]/div[1]").click()
                driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div[3]/div[1]/div[2]/div/a").click()
                time.sleep(2)
                
                
                
                driver.close()
                # driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div[2]/form/div[1]/input").send_keys('rakesh')   
                # driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/form/div[2]/input").send_keys('123')
                # driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/form/div[3]/button').click()
                # time.sleep(2)
                
                # a = ActionChains(driver)
                # driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div[1]/div[2]/div/a').click()

if __name__=="__main__":
        unittest.main()