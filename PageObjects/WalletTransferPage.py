from selenium import webdriver
from selenium.webdriver.common.by import By

class WalletTransferPage:
    textbox_amount_name = "amount"
    btntransfer_xpath = "(//button[@type='submit'])[2]"
    lnkwalletload_xpath = "//a[@href='https://b2b.digifintel.com/retailer/payin/transaction/create']"



    def __init__(self,driver):
        self.driver = driver


    def setAmount(self):
        self.driver.find_element(By.NAME,self.textbox_amount_name).send_keys(0.02)
        if "transaction" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_04_WalletTransferPage_wallettransferPass.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_04_WalletTransferPage_wallettransferFail.png")


    def clickonTransfer(self):
        self.driver.find_element(By.XPATH,self.btntransfer_xpath).click()

    def clickonHistory(self):
        print(self.driver.current_url)
        if "transaction" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_04_WalletTransferPage_walletHistoryPass.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_04_WalletTransferPage_walletHistoryFail.png")

    def clickonWalletLoad(self):
        self.driver.find_element(By.XPATH,self.lnkwalletload_xpath).click()

