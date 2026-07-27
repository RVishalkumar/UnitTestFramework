from selenium import webdriver
from selenium.webdriver.common.by import By

class CMSPage:
    lnkSwiftXMoneyTransferMenu = "//*[@id='sidebar-menu']/li[13]"

    def __init__(self,driver):
        self.driver = driver

    def clickonSwiftXMoneytransferMenu(self):
        self.driver.find_element(By.XPATH,self.lnkSwiftXMoneyTransferMenu).click()

