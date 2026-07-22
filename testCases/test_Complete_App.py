import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from PageObjects import DMTPage
from PageObjects.AepsPage import AepsPage
from PageObjects.AepsSettlementPage import AepsSettlementPage
from PageObjects.DirectPayoutPage import DirectPayoutPage
from PageObjects.LoginPage import LoginPage
from PageObjects.DashBoardPage import DashBoardPage
from PageObjects.RechargePlan import RechargePage
from PageObjects.WalletLoadPage import WalletLoadPage
from PageObjects.WalletTransferPage import WalletTransferPage
from PageObjects.DMTPage import DMTPage
from Utilities.readProperties import ReadConfig

class Test_001_Login(unittest.TestCase):


    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()



    @classmethod
    def setUpClass(cls):
        service_obj = Service("C://Users//dell//Desktop//chromedriver.exe")
        global driver
        driver = webdriver.Chrome(service=service_obj)
        driver.get(cls.baseurl)
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_01_homePageTitle(self):
        act_title = driver.title
        if act_title == "digi":
            #self.driver.close()
            assert True

        else:
            driver.save_screenshot(".\\screenshot\\test_homePageTitle.png")
            #self.driver.close()
            assert False

    def test_02_loginPage(self):
        self.lp = LoginPage(driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickonView()
        self.lp.clickLogin()
        self.lp.setOTP1(1)
        self.lp.setOTP2(2)
        self.lp.setOTP3(3)
        self.lp.setOTP4(4)
        self.lp.setOTP5(5)
        self.lp.setOTP6(6)
        self.lp.clickonContinue()
        print(driver.current_url)

    def test_03_DashBoardPage(self):
        self.db = DashBoardPage(driver)
        #self.db.clickSubscriptionModel()
        self.db.clickonMode()
        self.db.clickonNotification()
        self.db.clickonProfileImage()
        self.db.clickonMyProfile()
        self.db.clickonProfileImage()
        self.db.clickonActiveCommission()
        self.db.clickonDefaultCommission()
        self.db.clickonProfileImage()
        self.db.clickonSettings()
        self.db.clickonTransectionPIN()
        self.db.clickonProfileImage()
        self.db.clickonChangePassword()
        time.sleep(3)
        self.db.clickonProfileImage()
        time.sleep(3)
        self.db.clickonSupport()
        time.sleep(2)
        self.db.clickonWalletTranferMenu()
        #self.db.clickonLogOut()

    def test_04_WalletTransferPage(self):
        self.wtp = WalletTransferPage(driver)
        self.wtp.setAmount()
        self.wtp.clickonTransfer()
        self.wtp.clickonHistory()
        self.wtp.clickonWalletLoad()


    def test_05_WalletLoadPage(self):
        self.wlp = WalletLoadPage(driver)
        self.wlp.clickonInstantSattlement()
        self.wlp.clickonDMT()

    def test_06_DMTPage(self):
        self.dmt = DMTPage(driver)
        self.dmt.dmtTransactionBank1(9407271094)
        self.dmt.kycRemitterBank1()
        self.dmt.addRemitterBank1()
        self.dmt.clickonAddBeneficiaryBank1()
        self.dmt.clickonFetchallBeneficiaryBank1()
        self.wlp.clickonDMT()
        self.dmt.dmtTransactionBank2(9631312967)
        self.dmt.kycRemitterBank2()
        self.dmt.addRemitterBank2()
        self.dmt.clickonAddBeneficiaryBank2()
        self.dmt.clickonFetchallBeneficiaryBank2()
        self.wlp.clickonDMT()
        self.dmt.dmtTransactionBank7(9407271094)
        self.dmt.kycRemitterBank7()
        self.dmt.addRemitterBank7()
        self.dmt.clickonAddBeneficiaryBank7()
        self.dmt.clickonFetchallBeneficiaryBank7()
        self.dmt.clickonRechargeMenu()


    def test_07_RechargePage(self):
        self.rp = RechargePage(driver)
        self.rp.mobileRecharge()
        self.rp.dthRecharge()
        self.rp.clickonHistory()
        self.rp.clickonAEPSMenu()


    def test_08_AepsPage(self):
        self.aeps = AepsPage(driver)
        self.aeps.clickonAepsSettlement()



    def test_09_AepsSettlementPage(self):
        self.aepsSett = AepsSettlementPage(driver)
        self.aepsSett.clickonDirectPayoutMenu()


    def test_10_DirectPayoutPage(self):
        self.dp = DirectPayoutPage(driver)
        self.dp.clickonAddBank()
        self.dp.clickonVerifyAction()
        self.dp.payoutForm()
        self.dp.clickonPopUp()
        self.dp.clickonBBPSMenu()




    @classmethod
    def tearDownClass(cls):
        print("TearDownClass passed")
        driver.quit()

if __name__ == "__main__":
    unittest.main()
