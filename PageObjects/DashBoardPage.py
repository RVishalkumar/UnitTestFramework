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
    lnkchangepassword_xpath = "//a[text()=' Change Password']"
    lnksupport_xpath =  "//a[@href='https://b2b.digifintel.com/retailer/support']"
    lnkLOgout_xpath = "//a[@onclick='handleLogout()']"
    btnwalletTransfermenu_xpath = "//a[@class='active-page']"

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
    def clickonCommission(self):
        self.driver.find_element(By.XPATH,self.lnkcommission_xpath).click()
        self.driver.find_element(By.XPATH,"//button[@id='pills-recharge-tab']").click()
        self.driver.find_element(By.XPATH,"//button[@id='pills-aeps-tab']").click()
        self.driver.find_element(By.XPATH,"//button[@id='pills-payout-tab']").click()
        self.driver.find_element(By.XPATH,"//button[@id='pills-bbps-tab']").click()
        self.driver.find_element(By.XPATH,"//button[@id='pills-cc-tab']").click()
        self.driver.find_element(By.XPATH,"//button[@id='pills-upi-tab']").click()
        self.driver.find_element(By.XPATH,"//button[@id='pills-payin-tab']").click()
        self.driver.find_element(By.XPATH,"//button[@id='pills-cms-tab']").click()
        self.driver.find_element(By.XPATH,"//button[@id='pills-swiftx-tab']").click()

    def clickonSettings(self):
        self.driver.find_element(By.XPATH,self.lnksettins_xpath).click()
        #self.driver.find_element(By.XPATH,"//button[@id='pills-edit-profile-tab']").click()
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
        fathername.send_keys("Ram ji")
        dad=fathername.get_attribute("value")
        print(dad)
        mothername=self.driver.find_element(By.XPATH,"//input[@id='mothername']")
        mothername.clear()
        mothername.send_keys("Sita ji")
        mom=mothername.get_attribute("value")
        print(mom)
        shopname=self.driver.find_element(By.XPATH,"//input[@id='shopname']")
        shopname.clear()
        shopname.send_keys("New Gen Guru")
        shop=shopname.get_attribute("value")
        print(shop)
        gst=self.driver.find_element(By.XPATH,"//input[@id='gstnumber']")
        gst.clear()
        gst.send_keys("07AAGCN9155L1ZW")
        gt=gst.get_attribute("value")
        print(gt)
        addres=self.driver.find_element(By.XPATH,"//textarea[@id='address']")
        addres.clear()
        addres.send_keys("Bihar")
        add=addres.get_attribute("value")
        print(add)
        time.sleep(5)
        #Wait.wait_for_click(self.driver,(By.XPATH,"(//button[@class='btn btn-primary digiFin_orange_btn'])[1]")).click()
        # self.driver.find_element(By.XPATH,"(//button[@class='btn btn-primary digiFin_orange_btn'])[1]").click()

    def clickonChangePassword(self):
        Wait.wait_for_click(self.driver,(By.XPATH,self.lnkchangepassword_xpath)).click()
        #self.driver.find_element(By.XPATH,self.lnkchangepassword_xpath).click()
        self.driver.find_element(By.XPATH,"//input[@id='old_password']").send_keys("Test@@123")
        self.driver.find_element(By.XPATH,"//input[@id='new_password']").send_keys("Test@@123")
        self.driver.find_element(By.XPATH,"//input[@id='new_password_confirmation']").send_keys("Test@@123")
        self.driver.find_element(By.XPATH,"(//button[@type='submit'])[1]").click()

    def clickonSupport(self):
        self.driver.find_element(By.XPATH,self.lnksupport_xpath).click()
        supEmail=self.driver.find_element(By.XPATH,"//a[@href='mailto:BGRT@GMAIL.COM']").get_attribute("href")
        print(supEmail)
        callus=self.driver.find_element(By.XPATH,"//a[@href='tel:9298282828']").get_attribute("href")
        print(callus)
        suphours=self.driver.find_element(By.XPATH,"(//div[@class='support-info'])[3]").get_attribute("innerHTML")
        print(suphours)

    def clickonLogOut(self):
        self.driver.find_element(By.XPATH,self.lnkLOgout_xpath).click()

    def clickonWalletTranferMenu(self):
        Wait.wait_for_click(self.driver,(By.XPATH,self.btnwalletTransfermenu_xpath)).click()
        #self.driver.find_element(By.XPATH,self.btnwalletTransfermenu_xpath).click()

