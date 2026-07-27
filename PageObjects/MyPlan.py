from selenium import webdriver
from selenium.webdriver.common.by import By

class MyPlan:

    btnRenewNow_xpath = "(//button[@class='plan-action-btn primary'])[1]"
    btnPopupRenewNow_xpath = "//button[@class='swal2-confirm swal2-styled']"
    lnkCompairPlanMenu_xpath = "//*[@id='sidebar-menu']/li[16]"


    def __init__(self,driver):
        self.driver = driver

    def clickonRenewNow(self):
        self.driver.find_element(By.XPATH,self.btnRenewNow_xpath).click()

    def clickonPopupRenewNow(self):
        self.driver.find_element(By.XPATH,self.btnPopupRenewNow_xpath).click()

    def clickonCompairPlanMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCompairPlanMenu_xpath).click()

    
