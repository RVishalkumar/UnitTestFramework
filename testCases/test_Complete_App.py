import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from PageObjects import SwiftXMoneyTransferPage
from PageObjects.AepsPage import AepsPage
from PageObjects.AepsSettlementPage import AepsSettlementPage
from PageObjects.BbpsPage import BbpsPage
from PageObjects.CCPaymentPage import CCPaymentPage
from PageObjects.ComparePlans import ComparePlans
from PageObjects.DirectPayoutPage import DirectPayoutPage
from PageObjects.FundRequest import FundRequest
from PageObjects.LoginPage import LoginPage
from PageObjects.DashBoardPage import DashBoardPage
from PageObjects.MyPlan import MyPlan
from PageObjects.RechargePlan import RechargePage
from PageObjects.ReportsPage import ReportsPage
from PageObjects.UPIPaymentPage import UPIPaymentPage
from PageObjects.CMSPage import CMSPage
from PageObjects.SwiftXMoneyTransferPage import SwiftXMoneyTransferPage
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


    def test_11_BbpsPage(self):
        self.bbps = BbpsPage(driver)
        self.bbps.clickonElectricity()
        self.bbps.clickonInsurance()
        self.bbps.clickonPrepaid()
        self.bbps.clickobCCPayment()


    def test_12_CCPaymentPage(self):
        self.cc = CCPaymentPage(driver)
        self.cc.clickonccPayServer1()
        self.cc.setOTP(1,2,3,4,5,6)
        self.cc.clickonVerifyOTP()
        self.cc.clickonUpiPayment()


    def test_13_UPIPaymentPage(self):
        self.upi = UPIPaymentPage(driver)
        self.upi.paymenyViaQR()
        self.upi.clickonCMS()

    def test_14_CMSPage(self):
        self.cms = CMSPage(driver)
        self.cms.clickonSwiftXMoneytransferMenu()


    def test_15_SwiftXMoneyTransferPage(self):
        self.swift = SwiftXMoneyTransferPage(driver)
        self.swift.setMobileNumber(9407271094)
        self.swift.clickonDMT()
        self.swift.clickonSearch()
        self.swift.clickonAddBeneficiary()
        self.swift.fillForm("5000")
        self.swift.clickonPopUp()
        self.cms.clickonSwiftXMoneytransferMenu()
        self.swift.setMobileNumber(9407271094)
        self.swift.clickonSwifX()
        self.swift.clickonSearch()
        self.swift.clickonAddBeneficiary()
        self.swift.fillForm("25000")
        self.swift.clickonPopUp()
        self.swift.clickonReportsPage("Ledger Reports")

    def test_16_ReportsPage(self):
        self.rp = ReportsPage(driver)
        self.rp.setFillterByDateAndStatusLadger()
        self.rp.setFillterByTransactionIDLadger()
        self.swift.clickonReportsPage("DMT Reports")
        self.rp.setFillterByDateAndStatusDMT()
        self.rp.setFillterByTransactionIDDMT()
        self.rp.setFillterByOrderIdDMT()
        self.swift.clickonReportsPage("Payout Reports")
        self.rp.setFillterByDateAndStatusPayout()
        self.rp.setFillterByTransactionIDPayout()
        self.rp.setFillterByOrderIdPayout()
        self.swift.clickonReportsPage("Recharge Reports")
        self.rp.setFillterByDateandStatusRecharge()
        self.rp.setFillterByTransactionIDRecharge()
        self.rp.setFillterByOrderIdRecharge()
        self.swift.clickonReportsPage("BBPS Reports")
        self.rp.setFillterByDateandStatusBbps()
        self.rp.setFillterByTransactionIDBbps()
        self.rp.setFillterByOrderIdBbps()
        self.swift.clickonReportsPage("Credit Card Reports")
        self.rp.setFillterByDateandStatusCCPay()
        self.rp.setFillterByTransactionIDCCPay()
        self.rp.setFillterByOrderIdCCPay()
        self.swift.clickonReportsPage("UPI Reports")
        self.rp.setFillterByDateandStatusUPIPayment()
        self.rp.setFillterByTransactionIDUPIPayment()
        self.rp.setFillterByOrderIdUPIPayment()
        self.swift.clickonReportsPage("SwiftX Reports")
        self.rp.setFillterByDateandStatusSwiftX()
        self.rp.setFillterByTransactionIDSwiftX()
        self.rp.setFillterByOrderIdUPIPayment()
        self.rp.clickonMyPlanMenu()

    def test_17_MyPlan(self):
        self.mp = MyPlan(driver)
        self.mp.clickonRenewNow()
        self.mp.clickonPopupRenewNow()
        self.mp.clickonCompairPlanMenu()


    def test_18_ComparePlans(self):
        self.cp = ComparePlans(driver)
        self.cp.compareAEPS()
        self.cp.clickonDMT()
        self.cp.clickonPayout()
        self.cp.clickonBBPS()
        self.cp.clickonRecharge()
        self.cp.clickonPayIn()
        self.cp.clickonCMS()
        self.cp.clickonUPI()
        self.cp.clickonCCPay()
        self.cp.clickonSwiftX()
        self.cp.clickonFundRequestMenu()

    def test_19_FundRequest(self):
        self.fr = FundRequest(driver)
        self.fr.cliconCreateFundRequest()
        self.fr.clickonBiometricSupportMenu()
        self.db.clickonLogOut()


    @classmethod
    def tearDownClass(cls):
        print("TearDownClass passed")
        driver.quit()

if __name__ == "__main__":
    unittest.main()
