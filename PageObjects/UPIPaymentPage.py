from selenium import webdriver
from selenium.webdriver.common.by import By

class UPIPaymentPage:

    txtAmount_xpath = "//div[@class='row pt-3']/div[1]/input"
    radioBtnQR_xpath = "//input[@id='payViaQR']"
    btncreateUPIOrder_xpath = "//span[@id='btnText']"
    radioBtnVPA_xpath = "//input[@id='payViaVPA']"
    txtPayerVPA_xpath = "//input[@id='payerVpa']"
    btnVerify_xpath = "//button[@id='verifyVpaBtn']"
    txtRemark_xpath = "//input[@placeholder='Enter payment remarks']"
    btnPayNow_xpath = "//div[@class='modal-footer']/button"
    lnkCMSMenu_xpath = "//*[@id='sidebar-menu']/li[12]"

    def __init__(self,driver):
        self.driver = driver

    def paymenyViaQR(self):
        self.driver.find_element(By.XPATH,self.txtAmount_xpath).send_keys("100")
        self.driver.find_element(By.XPATH,self.radioBtnQR_xpath).click()
        self.driver.find_element(By.XPATH,self.btncreateUPIOrder_xpath).click()
        if "create" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_13_UPIPaymentPage_QRpass.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_12_UPIPaymentPage_QRfail.png")


    def paymentViaVPA(self):
        self.driver.find_element(By.XPATH,self.txtAmount_xpath).send_keys("100")
        self.driver.find_element(By.XPATH,self.radioBtnVPA_xpath).click()
        self.driver.find_element(By.XPATH,self.btncreateUPIOrder_xpath).click()
        self.driver.find_element(By.XPATH,self.txtPayerVPA_xpath).send_keys("success@upi")
        self.driver.find_element(By.XPATH,self.btnVerify_xpath).click()
        self.driver.find_element(By.XPATH,self.txtRemark_xpath).send_keys("food")
        self.driver.find_element(By.XPATH,self.btnPayNow_xpath).click()

    def clickonCMS(self):
        self.driver.find_element(By.XPATH,self.lnkCMSMenu_xpath).click()












