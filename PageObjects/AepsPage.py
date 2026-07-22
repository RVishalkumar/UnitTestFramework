from selenium import webdriver
from selenium.webdriver.common.by import By

class AepsPage:

    lnkAepsSettlement = "//*[@id='sidebar-menu']/li[7]"

    def __init__(self,driver):
        self.driver = driver







    def clickonAepsSettlement(self):
        self.driver.find_element(By.XPATH,self.lnkAepsSettlement).click()