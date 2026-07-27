from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities.wait import Wait


class SwiftXMoneyTransferPage:

    txtSearchMobile_xpath = "//input[@id='dmobile']"
    radiobtnDMT_xpath = "//div[@class='radio-buttons d-inline-block']/label[1]/span"
    radiobtnSwifX_xpath = "//div[@class='radio-buttons d-inline-block']/label[2]/span"
    btnSearch_xpath = "//button[@id='SmobileSearch']"
    btnAddBeneficiary_xpath = "//button[@data-bs-target='#exampleModal']"
    dropdownBankName_xpath = "//select[@id='bbanknamesmain']"
    txtaccountHolderName_xpath = "//input[@placeholder='Enter Account Holder Name']"
    txtbeneficiaryMobile_xpath = "//input[@id='receivermobile']"
    txtaccountNumber_xpath = "//input[@placeholder='Enter Bank Account Number']"
    txtifcCode_xpath = "//input[@id='bifsccode']"
    btnSubmit_xpath = "//*[@id='exampleModal']/div/div/div[2]/form/div/div[6]/button"
    btnVerify_xpath = "//div[@id='dmtData']/table/tbody/tr[1]/td[8]/a"
    dropdownBankName2_xpath = "//select[@id='dbanknamemain']"
    txtAmount_xpath = "//input[@id='amount']"
    txtTransactionPin_xpath = "//input[@id='txnpin']"
    btnsubmit2_xpath = "//div[@class='d-flex align-items-left justify-content-center gap-3']/button"
    lnkbtnReportsMenu = "//*[@id='sidebar-menu']/li[14]"




    def __init__(self,driver):
        self.driver = driver

    def setMobileNumber(self,number):
        self.driver.find_element(By.XPATH,self.txtSearchMobile_xpath).send_keys(number)

    def clickonDMT(self):
        self.driver.find_element(By.XPATH,self.radiobtnDMT_xpath).click()

    def clickonSwifX(self):
        self.driver.find_element(By.XPATH,self.radiobtnSwifX_xpath).click()

    def clickonSearch(self):
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()




    def clickonAddBeneficiary(self):
        self.driver.find_element(By.XPATH,self.btnAddBeneficiary_xpath).click()
        select=Select(self.driver.find_element(By.XPATH,self.dropdownBankName_xpath))
        select.select_by_visible_text("STATE BANK OF INDIA")
        self.driver.find_element(By.XPATH,self.txtaccountHolderName_xpath).send_keys("Vishal kumar")
        self.driver.find_element(By.XPATH,self.txtbeneficiaryMobile_xpath).send_keys(9407271094)
        self.driver.find_element(By.XPATH,self.txtaccountNumber_xpath).send_keys(989898989812)
        self.driver.find_element(By.XPATH,self.txtifcCode_xpath).send_keys("SBIN00555")
        self.driver.find_element(By.XPATH,self.btnSubmit_xpath).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Wait.wait_for_click(self.driver,(By.XPATH,self.btnVerify_xpath)).click()

    def fillForm(self,amount):
        bank = Select(self.driver.find_element(By.XPATH,self.dropdownBankName2_xpath))
        bank.select_by_visible_text("VISHAL KUMAR (STATE BANK OF INDIA -- 989898989812 --9407271094 )")
        self.driver.find_element(By.XPATH,self.txtAmount_xpath).send_keys(amount)
        self.driver.find_element(By.XPATH,self.txtTransactionPin_xpath).send_keys("1234")
        mode = Select(self.driver.find_element(By.XPATH,"//select[@id='txnmode']"))
        mode.select_by_visible_text("IMPS")
        self.driver.find_element(By.XPATH,self.btnsubmit2_xpath).click()

    def clickonPopUp(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER).perform()


    def clickonReportsPage(self,dropdownMenuList):
        dropdown=self.driver.find_element(By.XPATH,self.lnkbtnReportsMenu)
        dropdown.click()
        report=Select(dropdown)
        report.select_by_visible_text("dropdownMenuList")