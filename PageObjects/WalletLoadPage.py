from selenium import webdriver
from selenium.webdriver.common.by import By

class WalletLoadPage:

    btnInsSattlement_xpath = "//button[@id='payInSecDivBtn']"
    lnkdmt_xpath = "//*[@id='sidebar-menu']/li[4] "

    def __init__(self,driver):
        self.driver = driver


    def clickonInstantSattlement(self):
        self.driver.find_element(By.XPATH,self.btnInsSattlement_xpath).click()


        # Razorpay

        self.driver.find_element(By.NAME,"name").send_keys("Vishal")
        self.driver.find_element(By.NAME,"mobile").send_keys(9407271094)
        self.driver.find_element(By.NAME,"email").send_keys("vrk9407@gmail.com")
        self.driver.find_element(By.NAME,"amount").send_keys("100")
        self.driver.find_element(By.NAME,"profileimg").send_keys("C://Users//dell//Pictures//Screenshots//image.png")
        self.driver.find_element(By.NAME,"adfrontimg").send_keys("C://Users//dell//Pictures//Screenshots//img.png")
        self.driver.find_element(By.NAME,"adbackimg").send_keys("C://Users//dell//Pictures//Screenshots//pic.png")
        if "vishal" not in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_05_WalletLoadPage_walletSettlementFail.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_05_WalletLoadPage_walletSettlementPass.png")
        self.driver.find_element(By.XPATH,"//button[@id='submitOrderBtn']").click()
        self.driver.find_element(By.XPATH,"//button[@id='backToSettlementBtn']").click()


    def clickonDMT(self):
        self.driver.find_element(By.XPATH,self.lnkdmt_xpath).click()




