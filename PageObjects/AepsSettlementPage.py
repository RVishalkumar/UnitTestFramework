from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class AepsSettlementPage:
    dropdownbankName_xpath = "//select[@id='dbanknamemain']"
    txtamount_xpath = "//input[@id='amount']"
    txttransactionPin_xpath = "//input[@id='txnpin']"
    btnsubmit_xpath = "//*[@id='payoutForm']/div/div[2]/button"
    lnkdirectpayout_xpath = "//*[@id='sidebar-menu']/li[8]"

    def __init__(self, driver):
        self.driver = driver


    def aepsSettlement(self):
        select = Select(self.driver.find_element(By.XPATH,self.dropdownbankName_xpath))
        select.select_by_visible_text("SHUBHAM (AP MAHESH COOPERATIVE URBAN BANK LIMITED -- 837743774747)")
        self.driver.find_element(By.XPATH,self.txtamount_xpath).send_keys("10")
        self.driver.find_element(By.XPATH,self.txttransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH,self.btnsubmit_xpath).click()



    def clickonDirectPayoutMenu(self):
        self.driver.find_element(By.XPATH,self.lnkdirectpayout_xpath).click()



