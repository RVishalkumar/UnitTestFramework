import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig

class Test_001_Login(unittest.TestCase):


    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()



    @classmethod
    def setUpClass(cls):
        service_obj = Service("C://Users//dell//Desktop//chromedriver.exe")
        global driver
        driver = webdriver.Chrome(service=service_obj)
        driver.get(cls.baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_homePageTitle(self):
        act_title = driver.title
        if act_title == "OrangeHRM":
            #self.driver.close()
            assert True

        else:
            driver.save_screenshot(".\\screenshot\\test_homePageTitle.png")
            #self.driver.close()
            assert False

    def test_loginPage(self):
        self.lp = LoginPage(driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass passed")
        driver.quit()

if __name__ == "__main__":
    unittest.main()
