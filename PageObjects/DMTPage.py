from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DMTPage:

    textSearch_xpath = "//input[@id='dmobile']"
    radiobtnBank_xpath = "//*[@id='searchFormContainer']/div[2]/label[1]/span"
    btnSearch_xpath = "//button[@id='dmobileSearch']"
    txtfirstName_xpath = "//input[@id='firstName']"
    txtlastName_xpath = "//input[@id='lastName']"
    txtaadharNumber_xpath = "//input[@id='aadharnumber']"
    btnScanfingprint_xpath = "//a[@href='javascript:void(0);']"
    btncompleteKYC_xpath = "//button[@id='submitBtnKy']"
    txtOTP_xpath = "//input[@id='otp']"
    btnSubmit_xpath = "//*[@id='remitterForm']/div/div[2]/button"
    btnAddBeneficiary_xpath = "//button[@data-bs-target='#exampleModal']"
    dropdownBankName_xpath = "//button[@data-bs-target='#exampleModal']"
    txtaccountHolderName_xpath = "//input[@placeholder='Enter Account Holder Name']"
    txtbeneficiaryMobile_xpath = "//input[@id='receivermobile']"
    txtaccountNumber_xpath = "//input[@placeholder='Enter Bank Account Number']"
    txtifcCode_xpath = "//input[@id='bifsccode']"
    btnSubmit2_xpath = "//*[@id='exampleModal']/div/div/div[2]/form/div/div[6]/button"
    dropdown2Bankname_xpath = "//*[@id='dbankname']"
    txtamount_xpath = "//input[@id='amount']"
    txttransactionPIN_xpath = "//input[@id='txnpin']"
    btnsubmit3_xpath = "//*[@id='DmtMoneyForm']/div/div[2]/button"
    lnkrechargeMenu_xpath = "//*[@id='sidebar-menu']/li[5] "


    def __init__(self,driver):
        self.driver = driver

    # BANK 1


    def dmtTransactionBank1(self,number):
        self.driver.find_element(By.XPATH,self.textSearch_xpath).send_keys(number)
        self.driver.find_element(By.XPATH,self.radiobtnBank_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()

    def kycRemitterBank1(self):
        self.driver.find_element(By.XPATH,self.txtfirstName_xpath).send_keys("Vishal")
        self.driver.find_element(By.XPATH,self.txtlastName_xpath).send_keys("Kumar")
        self.driver.find_element(By.XPATH,self.txtaadharNumber_xpath).send_keys(123456789999)
        self.driver.find_element(By.XPATH,self.btnScanfingprint_xpath).click()
        self.driver.find_element(By.XPATH,self.btncompleteKYC_xpath).click()


    def addRemitterBank1(self):
        alert_success=self.driver.find_element(By.XPATH,"//div[@role='alert']")
        alert=alert_success.get_attribute('value')
        print(alert)
        if alert == "Remitter Kyc Done Successfully":
            assert True
        else:
            assert False
        self.driver.find_element(By.XPATH,self.txtOTP_xpath).send_keys(1234)

        self.driver.find_element(By.XPATH,self.btnSubmit_xpath).click()

    def clickonAddBeneficiaryBank1(self):
        self.driver.find_element(By.XPATH,self.btnAddBeneficiary_xpath).click()
        self.driver.find_element(By.XPATH,self.dropdownBankName_xpath).click()
        select=Select(self.driver.find_element(By.XPATH,"//input[@id='bbanknamesmain-selectized']"))
        select.select_by_visible_text("STATE BANK OF INDIA")
        self.driver.find_element(By.XPATH,self.txtaccountHolderName_xpath).send_keys("Vishal kumar")
        self.driver.find_element(By.XPATH,self.txtbeneficiaryMobile_xpath).send_keys(9407271094)
        self.driver.find_element(By.XPATH,self.txtaccountNumber_xpath).send_keys(9898980989)
        self.driver.find_element(By.XPATH,self.txtifcCode_xpath).send_keys("SBIN00555")
        self.driver.find_element(By.XPATH,self.btnSubmit2_xpath).click()

    def clickonFetchallBeneficiaryBank1(self):
        select = Select(self.driver.find_element(By.XPATH,self.dropdown2Bankname_xpath))
        select.select_by_visible_text("HDFC BANK")
        self.driver.find_element(By.XPATH,self.txtamount_xpath).send_keys(100)
        self.driver.find_element(By.XPATH,self.txttransactionPIN_xpath).click()
        self.driver.find_element(By.XPATH,self.btnsubmit3_xpath).click()
        if "YmFuazE=" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_06_DMTPage_invoiceBank1Pass.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_06_DMTPage_invoiceBank1Fail.png")
        self.driver.find_element(By.XPATH,"(//button[@onclick='CloseModal()'])[2]").click()


    # BANK 2


    def dmtTransactionBank2(self,number):
        self.driver.find_element(By.XPATH,self.textSearch_xpath).send_keys(number)
        self.driver.find_element(By.XPATH,self.radiobtnBank_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()

    def kycRemitterBank2(self):
        self.driver.find_element(By.XPATH, self.txtfirstName_xpath).send_keys("Vishal")
        self.driver.find_element(By.XPATH, self.txtlastName_xpath).send_keys("singh")
        self.driver.find_element(By.XPATH, self.txtaadharNumber_xpath).send_keys(876543219999)
        self.driver.find_element(By.XPATH,self.btnScanfingprint_xpath).click()
        self.driver.find_element(By.XPATH,self.btncompleteKYC_xpath).click()

    def addRemitterBank2(self):
        alert_success=self.driver.find_element(By.XPATH,"//div[@role='alert']")
        alert=alert_success.get_attribute('value')
        print(alert)
        if alert == "Remitter Kyc Done Successfully":
            assert True
        else:
            assert False
        self.driver.find_element(By.XPATH,self.txtOTP_xpath).send_keys(1234)
        self.driver.find_element(By.XPATH,self.btnSubmit_xpath).click()

    def clickonAddBeneficiaryBank2(self):
        self.driver.find_element(By.XPATH,self.dropdownBankName_xpath).click()
        select=Select(self.driver.find_element(By.XPATH,"//input[@id='bbanknamesmain-selectized']"))
        select.select_by_visible_text("CITI BANK")
        self.driver.find_element(By.XPATH,self.txtaccountHolderName_xpath).send_keys("Vishal Singh")
        self.driver.find_element(By.XPATH,self.txtbeneficiaryMobile_xpath).send_keys(9631312967)
        self.driver.find_element(By.XPATH,self.txtaccountNumber_xpath).send_keys(6766678987)
        self.driver.find_element(By.XPATH,self.txtifcCode_xpath).send_keys("citi0101A")
        self.driver.find_element(By.XPATH,self.btnSubmit2_xpath).click()

    def clickonFetchallBeneficiaryBank2(self):
        select = Select(self.driver.find_element(By.XPATH, self.dropdown2Bankname_xpath))
        select.select_by_visible_text("CITI BANK")
        self.driver.find_element(By.XPATH, self.txtamount_xpath).send_keys(100)
        self.driver.find_element(By.XPATH, self.txttransactionPIN_xpath).click()
        self.driver.find_element(By.XPATH, self.btnsubmit3_xpath).click()
        if "YmFuazE=" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_06_DMTPage_invoiceBank2Pass.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_06_DMTPage_invoiceBank2Fail.png")
        self.driver.find_element(By.XPATH, "(//button[@onclick='CloseModal()'])[2]").click()

    # Bank 7

    def dmtTransactionBank7(self,number):
        self.driver.find_element(By.XPATH,self.textSearch_xpath).send_keys(number)
        self.driver.find_element(By.XPATH,self.radiobtnBank_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()

    def kycRemitterBank7(self):
        self.driver.find_element(By.XPATH, self.txtfirstName_xpath).send_keys("Vishal")
        self.driver.find_element(By.XPATH, self.txtlastName_xpath).send_keys("singh")
        self.driver.find_element(By.XPATH, self.txtaadharNumber_xpath).send_keys(876543219999)
        self.driver.find_element(By.XPATH,self.btnScanfingprint_xpath).click()
        self.driver.find_element(By.XPATH,self.btncompleteKYC_xpath).click()

    def addRemitterBank7(self):
        alert_success=self.driver.find_element(By.XPATH,"//div[@role='alert']")
        alert=alert_success.get_attribute('value')
        print(alert)
        if alert == "Remitter Kyc Done Successfully":
            assert True
        else:
            assert False
        self.driver.find_element(By.XPATH,self.txtOTP_xpath).send_keys(1234)
        self.driver.find_element(By.XPATH,self.btnSubmit_xpath).click()

    def clickonAddBeneficiaryBank7(self):
        self.driver.find_element(By.XPATH,self.dropdownBankName_xpath).click()
        select=Select(self.driver.find_element(By.XPATH,"//input[@id='bbanknamesmain-selectized']"))
        select.select_by_visible_text("AXIS BANK")
        self.driver.find_element(By.XPATH,self.txtaccountHolderName_xpath).send_keys("Vishal Singh")
        self.driver.find_element(By.XPATH,self.txtbeneficiaryMobile_xpath).send_keys(9407271094)
        self.driver.find_element(By.XPATH,self.txtaccountNumber_xpath).send_keys(5416096313)
        self.driver.find_element(By.XPATH,self.txtifcCode_xpath).send_keys("AXIS0007G")
        self.driver.find_element(By.XPATH,self.btnSubmit2_xpath).click()

    def clickonFetchallBeneficiaryBank7(self):
        select = Select(self.driver.find_element(By.XPATH, self.dropdown2Bankname_xpath))
        select.select_by_visible_text("AXIS BANK")
        self.driver.find_element(By.XPATH, self.txtamount_xpath).send_keys(100)
        self.driver.find_element(By.XPATH, self.txttransactionPIN_xpath).click()
        self.driver.find_element(By.XPATH, self.btnsubmit3_xpath).click()
        if "YmFuazE=" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_06_DMTPage_invoiceBank7Pass.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_06_DMTPage_invoiceBank7Fail.png")
        self.driver.find_element(By.XPATH, "(//button[@onclick='CloseModal()'])[2]").click()


    def clickonRechargeMenu(self):
        self.driver.find_element(By.XPATH,self.lnkrechargeMenu_xpath).click()


