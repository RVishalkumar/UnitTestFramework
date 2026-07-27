from selenium import webdriver
from selenium.webdriver.common.by import By

class ComparePlans:

    tagDMT_xpath = "//a[@href='https://b2b.digifintel.com/subscription/compare?service=dmt']"
    tagPayout_xpath = "//a[@href='https://b2b.digifintel.com/subscription/compare?service=payout']"
    tagBBPS_xpath = "//a[@href='https://b2b.digifintel.com/subscription/compare?service=bbps']"
    tagRecharge_xpath = "//a[@href='https://b2b.digifintel.com/subscription/compare?service=recharge']"
    tagPayin_xpath = "//a[@href='https://b2b.digifintel.com/subscription/compare?service=payin']"
    tagCMS_xpath = "//a[@href='https://b2b.digifintel.com/subscription/compare?service=cms']"
    tagUPI_xpath = "//a[@href='https://b2b.digifintel.com/subscription/compare?service=upi']"
    tagCCPay_xpath = "//a[@href='https://b2b.digifintel.com/subscription/compare?service=ccpay']"
    tagSwiftX_xpath = "//a[@href='https://b2b.digifintel.com/subscription/compare?service=swiftx']"
    lnkFundRequest_xpath = "//*[@id='sidebar-menu']/li[17]"

    def __init__(self,driver):
        self.driver = driver

    def compareAEPS(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if "compare" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_18_ComparePlanPage_AEPSComparePlanp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_18_ComparePlanPage_AEPSComparePlanf.png")


    def clickonDMT(self):
        self.driver.find_element(By.XPATH,self.tagDMT_xpath).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if "compare" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_18_ComparePlanPage_DMTComparePlanp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_18_ComparePlanPage_DMTComparePlanf.png")


    def clickonPayout(self):
        self.driver.find_element(By.XPATH,self.tagPayout_xpath).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if "compare" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_18_ComparePlanPage_PayoutComparePlanp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_18_ComparePlanPage_PayoutComparePlanf.png")

    def clickonBBPS(self):
        self.driver.find_element(By.XPATH,self.tagBBPS_xpath).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if "compare" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_18_ComparePlanPage_BbpsComparePlanp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_18_ComparePlanPage_BbpsComparePlanf.png")


    def clickonRecharge(self):
        self.driver.find_element(By.XPATH,self.tagRecharge_xpath).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if "compare" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_18_ComparePlanPage_RechargeComparePlanp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_18_ComparePlanPage_RechargeComparePlanf.png")


    def clickonPayIn(self):
        self.driver.find_element(By.XPATH,self.tagPayin_xpath).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if "compare" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_18_ComparePlanPage_PayInComparePlanp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_18_ComparePlanPage_PayInComparePlanf.png")

    def clickonCMS(self):
        self.driver.find_element(By.XPATH,self.tagCMS_xpath).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if "compare" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_18_ComparePlanPage_CMSComparePlanp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_18_ComparePlanPage_CMSComparePlanf.png")


    def clickonUPI(self):
        self.driver.find_element(By.XPATH,self.tagUPI_xpath).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if "compare" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_18_ComparePlanPage_UPIComparePlanp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_18_ComparePlanPage_UPIComparePlanf.png")


    def clickonCCPay(self):
        self.driver.find_element(By.XPATH,self.tagCCPay_xpath).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if "compare" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_18_ComparePlanPage_CCPayComparePlanp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_18_ComparePlanPage_CCPayComparePlanf.png")


    def clickonSwiftX(self):
        self.driver.find_element(By.XPATH,self.tagSwiftX_xpath).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if "compare" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_18_ComparePlanPage_SwiftComparePlanp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_18_ComparePlanPage_SwiftComparePlanf.png")


    def clickonFundRequestMenu(self):
        self.driver.find_element(By.XPATH,self.lnkFundRequest_xpath).click()




