from selenium import webdriver
from selenium.webdriver.common.by import By

class WalletTransferPage:
    textbox_amount_name = "amount"
    btntransfer_xpath = "(//button[@type='submit'])[1]"



    def __init__(self,driver):
        self.driver = driver


    def setAmount(self):
        self.driver.find_element(By.NAME,self.textbox_amount_name).send_keys("0.02")

    def clickonTransfer(self):
        self.driver.find_element(By.XPATH,self.btntransfer_xpath).click()