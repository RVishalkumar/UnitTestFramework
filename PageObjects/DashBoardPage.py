import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from Utilities.wait import Wait


class DashBoardPage:

    btnsubscriptionmodel_xpath = "//button[text()='Maybe Later']"
    btnmode_xpath = "//button[@title='Switch to Light/Dark mode']"
    btnnotifications_xpath = "(//button[@type='button'])[4]"
    btnprofile_Xpath = "(//button[@type='button'])[5]"
    lnkprofile_xpath = "/html/body/main/div[1]/div/div[2]/div/div[3]/div/ul/li[1]/a"
    lnkcommission_xpath = "//a[text()=' My Commission']"
    lnksettins_xpath = "//a[text()=' Settings']"
    btntransictionpin_xpath = "//*[@id='pills-tab']/li[2]"
    lnkchangepassword_xpath = "//a[text()=' Change Password']"
    lnksupport_xpath =  "//a[@href='https://b2b.digifintel.com/retailer/support']"
    lnkLOgout_xpath = "//a[@onclick='handleLogout()']"
    btnwalletTransfermenu_xpath = "//*[@id='sidebar-menu']/li[2]"

    def __init__(self,driver):
        self.driver = driver

    def clickSubscriptionModel(self):
        self.driver.find_element(By.XPATH,self.btnsubscriptionmodel_xpath).click()

    def clickonMode(self):
        self.driver.find_element(By.XPATH,self.btnmode_xpath).click()


    def clickonNotification(self):
        self.driver.find_element(By.XPATH,self.btnnotifications_xpath).click()



    def clickonProfileImage(self):
        self.driver.find_element(By.XPATH,self.btnprofile_Xpath).click()



    def clickonMyProfile(self):
        self.driver.find_element(By.XPATH,self.lnkprofile_xpath).click()
        if "profile" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_Profile.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_Profile.png")



    def clickonActiveCommission(self):
        self.driver.find_element(By.XPATH, self.lnkcommission_xpath).click()
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/div/div/div[2]/div[3]/div[1]").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionActiveAEPS.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionActiveAEPS.png")
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div/div/div[2]/div[3]/div[1]").click()


        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/div/div/div[2]/div[4]/div[1]").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionActiveCCPAYMENT.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionActiveCCPAYMENT.png")
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div/div/div[2]/div[4]/div[1]").click()


        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/div/div/div[2]/div[5]/div[1]").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionActivePAYOUT.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionActivePAYOUT.png")
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div/div/div[2]/div[5]/div[1]").click()


        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/div/div/div[2]/div[6]/div[1]").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionActiveBBPS.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionActiveBBPS.png")
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div/div/div[2]/div[6]/div[1]").click()



        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div/div/div[2]/div[7]/div[1]").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionActiveSWIFTX.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionActiveSWIFTX.png")
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div/div/div[2]/div[7]/div[1]").click()



        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div/div/div[2]/div[8]/div[1]").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionActiveDMT.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionActiveDMT.png")
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div/div/div[2]/div[8]/div[1]").click()



        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/div/div/div[2]/div[9]/div[1]").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionActiveRecharge.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionActiveRecharge.png")
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/div/div/div[2]/div[9]/div[1]").click()



        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/div/div/div[2]/div[10]/div[1]").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionActivePAYIN.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionActivePAYIN.png")
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/div/div/div[2]/div[10]/div[1]").click()



        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/div/div/div[2]/div[11]/div[1]").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionActiveUPI.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionActiveUPI.png")
        self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/div/div/div[2]/div[11]/div[1]").click()






    def clickonDefaultCommission(self):
        element=self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/div/div/div[2]/div[12]")
        self.driver.execute_script("arguments[0].scrollIntoView();",element)

        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionDMT.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionDMT.png")


        self.driver.find_element(By.XPATH,"//button[@id='pills-recharge-tab']").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionRecharge.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionRecharge.png")


        self.driver.find_element(By.XPATH,"//button[@id='pills-aeps-tab']").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionAEPS.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionAEPS.png")


        self.driver.find_element(By.XPATH,"//button[@id='pills-payout-tab']").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionPAYOUT.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionPAYOUT.png")


        self.driver.find_element(By.XPATH,"//button[@id='pills-bbps-tab']").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionBBPS.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionBBPS.png")


        self.driver.find_element(By.XPATH,"//button[@id='pills-cc-tab']").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionCCPAYMENT.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionCCPAYMENT.png")


        self.driver.find_element(By.XPATH,"//button[@id='pills-upi-tab']").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionUPI.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionUPI.png")


        self.driver.find_element(By.XPATH,"//button[@id='pills-payin-tab']").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionPAYIN.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionPAYIN.png")


        self.driver.find_element(By.XPATH,"//button[@id='pills-cms-tab']").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionCMS.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionCMS.png")


        self.driver.find_element(By.XPATH,"//button[@id='pills-swiftx-tab']").click()
        if "commission" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_commissionSWIFTX.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_commissionSWIFTX.png")




    def clickonSettings(self):
        self.driver.find_element(By.XPATH,self.lnksettins_xpath).click()
        if "all" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_settingPreviousData.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_settingPreviousData.png")
        name=self.driver.find_element(By.XPATH,"//input[@id='name']").get_attribute("value")
        print(name)
        email=self.driver.find_element(By.XPATH,"//input[@id='email']").get_attribute("value")
        print(email)
        mobile=self.driver.find_element(By.XPATH,"//input[@id='mobile']").get_attribute("value")
        print(mobile)
        username=self.driver.find_element(By.XPATH,"//input[@id='username']").get_attribute("value")
        print(username)
        fathername=self.driver.find_element(By.XPATH,"//input[@id='fathername']")
        fathername.clear()
        fathername.send_keys("Ram")
        dad=fathername.get_attribute("value")
        print(dad)
        mothername=self.driver.find_element(By.XPATH,"//input[@id='mothername']")
        mothername.clear()
        mothername.send_keys("Sita")
        mom=mothername.get_attribute("value")
        print(mom)
        shopname=self.driver.find_element(By.XPATH,"//input[@id='shopname']")
        shopname.clear()
        shopname.send_keys("Gen Guru")
        shop=shopname.get_attribute("value")
        print(shop)
        gst=self.driver.find_element(By.XPATH,"//input[@id='gstnumber']")
        gst.clear()
        gst.send_keys("07AAGCN9155L1")
        gt=gst.get_attribute("value")
        print(gt)
        addres=self.driver.find_element(By.XPATH,"//textarea[@id='address']")
        addres.clear()
        addres.send_keys("chhapra")
        add=addres.get_attribute("value")
        print(add)
        if "all" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_settingCurrentData.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_settingCurrentData.png")
        time.sleep(5)
        Wait.wait_for_click(self.driver,(By.XPATH,"//div[@id='pills-tabContent']/div[1]/form/div[3]/button")).click()
        #self.driver.find_element(By.XPATH,"(//button[@class='btn btn-primary digiFin_orange_btn'])[1]").click()


    def clickonTransectionPIN(self):
        Wait.wait_for_click(self.driver,(By.XPATH,self.btntransictionpin_xpath)).click()
        oldTranPin=self.driver.find_element(By.XPATH,"//input[@id='txnpin']")
        oldTranPin.send_keys("1234")
        oldTran=oldTranPin.get_attribute("value")
        print(oldTran)
        newTranPin=self.driver.find_element(By.XPATH,"//input[@id='acpassword']")
        newTranPin.send_keys("1234")
        newTran=newTranPin.get_attribute("value")
        print(newTran)
        if "all" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_settingsTransPinPass1.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_settingTranPinFail1.png")
        self.driver.find_element(By.XPATH,"(//button[@type='submit'])[2]").click()


    def clickonChangePassword(self):
        Wait.wait_for_click(self.driver,(By.XPATH,self.lnkchangepassword_xpath)).click()
        #self.driver.find_element(By.XPATH,self.lnkchangepassword_xpath).click()
        self.driver.find_element(By.XPATH,"//input[@id='old_password']").send_keys("Test@@123")
        self.driver.find_element(By.XPATH,"//span[@data-toggle='#old_password']").click()
        self.driver.find_element(By.XPATH,"//input[@id='new_password']").send_keys("Test@@123")
        self.driver.find_element(By.XPATH,"//span[@data-toggle='#new_password']").click()
        self.driver.find_element(By.XPATH,"//input[@id='new_password_confirmation']").send_keys("Test@@123")
        self.driver.find_element(By.XPATH,"//span[@data-toggle='#new_password_confirmation']").click()
        if "password" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_changePassword.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_changePassword.png")
        self.driver.find_element(By.XPATH,"(//button[@type='submit'])[1]").click()


    def clickonSupport(self):
        self.driver.find_element(By.XPATH,self.lnksupport_xpath).click()
        # supEmail=self.driver.find_element(By.XPATH,"//a[@href='mailto:BGRT@GMAIL.COM']")
        # mail=supEmail.get_attribute("value")
        # print(mail)
        # callus=self.driver.find_element(By.XPATH,"//a[@href='tel:9298282828']")
        # call=callus.get_attribute("value")
        # print(call)
        # suphours=self.driver.find_element(By.XPATH,"(//div[@class='support-info'])[3]")
        # support=suphours.get_attribute("value")
        # print(support)
        if "support" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_03_DashBoardPage_support.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_03_DashBoardPage_support.png")

    def clickonLogOut(self):
        self.driver.find_element(By.XPATH,self.lnkLOgout_xpath).click()

    def clickonWalletTranferMenu(self):
        Wait.wait_for_click(self.driver,(By.XPATH,self.btnwalletTransfermenu_xpath)).click()
        #self.driver.find_element(By.XPATH,self.btnwalletTransfermenu_xpath).click()

