from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from Utilities.wait import Wait


class DirectPayoutPage:

    btnAddBank_xpath = "/html/body/main/div[2]/div[2]/div/div/div[1]/div/div[2]"
    dropdownSelectBank_xpath = "//select[@name='banknamemian']"
    txtAccountHolderName = "//input[@placeholder='Enter Account Holder Name']"
    txtAccountHolderMobile_xpath = "//input[@placeholder='Enter Account Holder Mobile']"
    txtIfcCode_xpath = "//input[@placeholder='Enter Bank IFSC Code']"
    dropdownAccountType_xpath = "//select[@id='accounttype']"
    btnSubmit_xpath = "//div[@class='d-flex align-items-center justify-content-center gap-3 mt-10']/button"
    btnVerify_xpath = "(//table[@class='table table-hover table-bordered'])[1]/tbody/tr[1]/td[8]"
    selectBankName_xpath = "(//select[@id='dbanknamemain'])[1]"
    txtAmount_xpath = "(//input[@id='amount'])[1]"
    txtTransactionPin_xpath = "(//input[@id='txnpin'])[1]"
    selectMode_xpath = "(//select[@id='txnmode'])[1]"
    btnSubmit1_xpath = "(//div[@class='d-flex align-items-left justify-content-center gap-3'])[1]/button"
    lnkBBPSMenu_xpath = "//*[@id='sidebar-menu']/li[9]"


    def __init__(self, driver):
        self.driver = driver


    def clickonAddBank(self):
        self.driver.find_element(By.XPATH,self.btnAddBank_xpath).click()
        select = Select(self.driver.find_element(By.XPATH,self.dropdownSelectBank_xpath))
        select.select_by_visible_text("STATE BANK OF INDIA")
        self.driver.find_element(By.XPATH,self.txtAccountHolderName).send_keys("Vishal Kumar")
        self.driver.find_element(By.XPATH,self.txtAccountHolderMobile_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH,self.txtIfcCode_xpath).send_keys("SBIN0000555")
        Account = Select(self.driver.find_element(By.XPATH,self.dropdownAccountType_xpath))
        Account.select_by_visible_text("Current Account")
        self.driver.find_element(By.XPATH,self.btnSubmit_xpath).click()

    def clickonVerifyAction(self):
        self.driver.find_element(By.XPATH,self.btnVerify_xpath).click()


    def payoutForm(self):
        bank_name = Wait.wait_for_visible(self.driver,(By.XPATH,self.selectBankName_xpath))
        bank = Select(bank_name)
        bank.select_by_visible_text("STATE BANK OF INDIA")
        self.driver.find_element(By.XPATH,self.txtAmount_xpath).send_keys("100")
        self.driver.find_element(By.XPATH,self.txtTransactionPin_xpath).send_keys("1234")
        mode = Select(self.driver.find_element(By.XPATH,self.selectMode_xpath))
        mode.select_by_visible_text("IMPS")
        self.driver.find_element(By.XPATH,self.btnSubmit1_xpath).click()


    def clickonPopUp(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER).perform()

    def clickonBBPSMenu(self):
        self.driver.find_element(By.XPATH,self.lnkBBPSMenu_xpath).click()




