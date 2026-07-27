from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class FundRequest:

    btnCreateFundRequest_xpath = "//button[@data-bs-target='#payoutBankModal']"
    dropdownTransactionMode_name = "transactionmode"
    dropdownBankName_xpath = "//select[@id='bankid']"
    txtDepositeAmount_xpath = "//input[@id='amount']"
    txtUTR_xpath = "//input[@id='bankutr']"
    selectDepositeDate_xpath = "//input[@id='depositdate']"
    uploadclip_xpath = "//input[@id='bankslip']"
    textareaRemark_xpath = "//textarea[@id='remarks']"
    btnSubmit_xpath = "//div[@class='d-flex align-items-center justify-content-center gap-3 mt-24']/button"
    lnkBiometricSupport_xpath = "//*[@id='sidebar-menu']/li[18]"


    def __init__(self,driver):
        self.driver = driver

    def cliconCreateFundRequest(self):
        self.driver.find_element(By.XPATH,self.btnCreateFundRequest_xpath).click()
        mode = Select(self.driver.find_element(By.NAME,self.dropdownTransactionMode_name))
        mode.select_by_visible_text("IMPS")
        bank = Select(self.driver.find_element(By.XPATH,self.dropdownBankName_xpath))
        bank.select_by_visible_text("ADMIN BANK || STATE BANK OF INDIA || 877373773733 || SBIN0000567  [Demo admin (admin)]")
        self.driver.find_element(By.XPATH,self.txtDepositeAmount_xpath).send_keys("10000")
        self.driver.find_element(By.XPATH,self.txtUTR_xpath).send_keys("987654321098")
        self.driver.find_element(By.XPATH,self.selectDepositeDate_xpath).send_keys("27-07-2026")
        self.driver.find_element(By.XPATH,self.uploadclip_xpath).send_keys("C://Users//dell//Pictures//Screenshots//pic.png")
        self.driver.find_element(By.XPATH,self.textareaRemark_xpath).send_keys("I want to be a Developer")
        self.driver.find_element(By.XPATH,self.btnSubmit_xpath).click()


    def clickonBiometricSupportMenu(self):
        self.driver.find_element(By.XPATH,self.lnkBiometricSupport_xpath).click()



