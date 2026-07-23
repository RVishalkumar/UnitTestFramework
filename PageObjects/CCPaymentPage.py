from selenium import webdriver
from selenium.webdriver.common.by import By

class CCPaymentPage:

    btnccPayServer1 = "//ul[@id='ccPayTabs']//button"
    txtCardHolderName_xpath = "//input[@id='cardHolderName']"
    txtMobile_xpath = "//input[@name='mobile']"
    txtCardNumber_xpath = "//input[@id='cardNumber']"
    txtAmount_xpath = "//input[@name='amount']"
    btnRequestOTP_xpath = "//button[@id='requestOtpBtn']"
    txtOTP1_xpath = "//div[@class='modal-content']/div[2]//form[@id='verifyOtpForm']/div/input[1]"
    txtOTP2_xpath = "//div[@class='modal-content']/div[2]//form[@id='verifyOtpForm']/div/input[2]"
    txtOTP3_xpath = "//div[@class='modal-content']/div[2]//form[@id='verifyOtpForm']/div/input[3]"
    txtOTP4_xpath = "//div[@class='modal-content']/div[2]//form[@id='verifyOtpForm']/div/input[4]"
    txtOTP5_xpath = "//div[@class='modal-content']/div[2]//form[@id='verifyOtpForm']/div/input[5]"
    txtOTP6_xpath = "//div[@class='modal-content']/div[2]//form[@id='verifyOtpForm']/div/input[6]"
    btnVerifyOtp_xpath = "//div[@class='modal-content']/div[2]//form[@id='verifyOtpForm']/button"
    lnkUpiPayment_xpath = "//*[@id='sidebar-menu']/li[11]"



    def __init__(self,driver):
        self.driver = driver

    def clickonccPayServer1(self):
        self.driver.find_element(By.XPATH,self.btnccPayServer1).click()
        self.driver.find_element(By.XPATH,self.txtCardHolderName_xpath).send_keys("Vishal Kumar")
        self.driver.find_element(By.XPATH,self.txtMobile_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH,self.txtCardNumber_xpath).send_keys("2221232419056588")
        self.driver.find_element(By.XPATH,self.txtAmount_xpath).send_keys("100")
        self.driver.find_element(By.XPATH,self.btnRequestOTP_xpath).click()

    def setOTP(self,otp1,otp2,otp3,otp4,otp5,otp6):
        self.driver.find_element_by_xpath(self.txtOTP1_xpath).send_keys(otp1)
        self.driver.find_element_by_xpath(self.txtOTP2_xpath).send_keys(otp2)
        self.driver.find_element_by_xpath(self.txtOTP3_xpath).send_keys(otp3)
        self.driver.find_element_by_xpath(self.txtOTP4_xpath).send_keys(otp4)
        self.driver.find_element_by_xpath(self.txtOTP5_xpath).send_keys(otp5)
        self.driver.find_element_by_xpath(self.txtOTP6_xpath).send_keys(otp6)

    def clickonVerifyOTP(self):
        self.driver.find_element(By.XPATH,self.btnVerifyOtp_xpath).click()

    def clickonUpiPayment(self):
        self.driver.find_element(By.XPATH,self.lnkUpiPayment_xpath).click()




