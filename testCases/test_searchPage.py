import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from PageObjects.LoginPage import LoginPage
from PageObjects.AddemployeePage import AddEmployeePage
from PageObjects.SearchEmployee import SearchEmployee
from Utilities.readProperties import ReadConfig

class Test_003_SearchPage(unittest.TestCase):
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()



    @classmethod
    def setUpClass(cls):
        service_obj= Service("C://Users//dell//Desktop//chromedriver.exe")
        global driver
        driver = webdriver.Chrome(service=service_obj)
        driver.get(cls.baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)


    def test_searchEmployee(self):
        self.lp = LoginPage(driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(2)
        self.lp.clickonPIMMenu()
        time.sleep(2)
        self.lp.clickaddCustomer()
        time.sleep(2)
        self.ae = AddEmployeePage(driver)
        self.ae.setFirstName("Vishal")
        self.ae.setLastName("Singh")
        self.ae.setEmpID("0101")
        self.ae.clickonSave()
        time.sleep(3)
        self.lp.clickaddCustomer()
        self.se = SearchEmployee(driver)
        self.se.setEmployeeName("Vishal")
        self.se.clickonSearch()

    @classmethod
    def tearDownClass(cls):
        driver.close()

if __name__ == "__main__":
    unittest.main()