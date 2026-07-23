from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities.wait import Wait


class BbpsPage:

    btnDTH_xpath = "//a[@href='https://b2b.digifintel.com/retailer/bbps/getbbpsoperator/DTH']"
    selectMode_xpath = "//select[@id='mode']"
    selectBiller_xpath = "//select[@id='operatorSubcategories']"
    txtBillerNumber_xpath = "//input[@id='ad0_name']"
    btnFitchBill_xpath = "//form[@id='dynamicForm']//button[@type='submit']"
    txtAmount_xpath = "//input[@id='amountInput']"
    txtTransactionPin_xpath = "//input[@id='userInput']"
    btnPayBill_xpath = "//div[@id='billContainer']/button"
    btnElectricity_xpath = "//a[@href='https://b2b.digifintel.com/retailer/bbps/getbbpsoperator/Electricity']"
    btnInsurance_xpath = "//a[@href='https://b2b.digifintel.com/retailer/bbps/getbbpsoperator/Insurance']"
    txtDOB_xpath = "//input[@id='ad1_name']"
    txtEmail_xpath = "//input[@id='ad2_name']"
    btnPrepaid_xpath = "//a[@href='https://b2b.digifintel.com/retailer/bbps/getbbpsoperator/PREPAID']"
    btnEBill_xpath = "//a[@href='https://b2b.digifintel.com/retailer/bbps/getbbpsoperator/Ebill']"
    btnGas_xpath = "//a[@href='https://b2b.digifintel.com/retailer/bbps/getbbpsoperator/gas']"
    btnIns_xpath = "//a[@href='https://b2b.digifintel.com/retailer/bbps/getbbpsoperator/Ins']"
    lnkccPaymentMenu_xpath = "//*[@id='sidebar-menu']/li[10]"




    def __init__(self,driver):
        self.driver = driver

    def clickonDTH(self):

        # AIRTELDTH
        self.driver.find_element(By.XPATH,self.btnDTH_xpath).click()
        mode = Select(self.driver.find_element(By.XPATH,self.selectMode_xpath))
        mode.select_by_visible_text("Online")
        biller_AirtelDTH = Select(self.driver.find_element(By.XPATH,self.selectBiller_xpath))
        biller_AirtelDTH.select_by_visible_text("AIRTELDTH")
        self.driver.find_element(By.XPATH,self.txtBillerNumber_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH,self.btnFitchBill_xpath).click()
        self.driver.find_element(By.XPATH,self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH,self.btnPayBill_xpath).click()

        # YES Bank
        self.driver.refresh()
        mode = Select(self.driver.find_element(By.XPATH, self.selectMode_xpath))
        mode.select_by_visible_text("Online")
        biller_YesBank = Select(self.driver.find_element(By.XPATH, self.selectBiller_xpath))
        biller_YesBank.select_by_visible_text("YES Bank")
        self.driver.find_element(By.XPATH, self.txtBillerNumber_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH, self.btnFitchBill_xpath).click()
        self.driver.find_element(By.XPATH, self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH, self.btnPayBill_xpath).click()

        # IDFC
        self.driver.refresh()
        mode = Select(self.driver.find_element(By.XPATH, self.selectMode_xpath))
        mode.select_by_visible_text("Online")
        biller_IDFC = Select(self.driver.find_element(By.XPATH, self.selectBiller_xpath))
        biller_IDFC.select_by_visible_text("IDFC")
        self.driver.find_element(By.XPATH, self.txtBillerNumber_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH, self.btnFitchBill_xpath).click()
        self.driver.find_element(By.XPATH, self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH, self.btnPayBill_xpath).click()

    def clickonElectricity(self):
        self.driver.find_element(By.XPATH,self.btnElectricity_xpath).click()

        # Himachal Pradesh State Electricity Board (HPSEB) Electricity,BBPS

        mode = Select(self.driver.find_element(By.XPATH,self.selectMode_xpath))
        mode.select_by_visible_text("Offline")
        biller_Hima = Select(self.driver.find_element(By.XPATH, self.selectBiller_xpath))
        biller_Hima.select_by_visible_text("Himachal Pradesh State Electricity Board (HPSEB) Electricity,BBPS")
        self.driver.find_element(By.XPATH,self.txtBillerNumber_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH,self.btnFitchBill_xpath).click()
        self.driver.find_element(By.XPATH,self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH,self.btnPayBill_xpath).click()
        if "Electricity" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_11_BBPSPage_electricitybillHimachalPass.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_11_BBPSPage_electricitybillHimachalFail.png")
        self.driver.find_element(By.XPATH,"//button[@id='closeModalButton']").click()


        # Bangalore Electricity Supply Company Ltd. (BESCOM) Electricity,BBPS
        Wait.wait_for_click(self.driver,(By.XPATH,self.btnElectricity_xpath)).click()
        mode = Select(self.driver.find_element(By.XPATH, self.selectMode_xpath))
        mode.select_by_visible_text("Offline")
        biller_Bang = Select(self.driver.find_element(By.XPATH, self.selectBiller_xpath))
        biller_Bang.select_by_visible_text("Bangalore Electricity Supply Company Ltd. (BESCOM) Electricity,BBPS")
        self.driver.find_element(By.XPATH,self.txtBillerNumber_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH,self.btnFitchBill_xpath).click()
        self.driver.find_element(By.XPATH,self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH,self.btnPayBill_xpath).click()
        if "Electricity" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_11_BBPSPage_electricitybillBangalorePass.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_11_BBPSPage_electricitybillBangaloreFail.png")
        self.driver.find_element(By.XPATH,"//button[@id='closeModalButton']").click()


        # BSES Rajdhani Power Limited - Delhi Electricity,BBPS
        Wait.wait_for_click(self.driver,(By.XPATH,self.btnElectricity_xpath)).click()
        mode = Select(self.driver.find_element(By.XPATH, self.selectMode_xpath))
        mode.select_by_visible_text("Offline")
        biller_Delhi = Select(self.driver.find_element(By.XPATH, self.selectBiller_xpath))
        biller_Delhi.select_by_visible_text("BSES Rajdhani Power Limited - Delhi Electricity,BBPS")
        self.driver.find_element(By.XPATH, self.txtBillerNumber_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH, self.btnFitchBill_xpath).click()
        self.driver.find_element(By.XPATH, self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH, self.btnPayBill_xpath).click()
        if "Electricity" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_11_BBPSPage_electricitybillDelhiPass.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_11_BBPSPage_electricitybillDelhiFail.png")
        self.driver.find_element(By.XPATH, "//button[@id='closeModalButton']").click()

    def clickonInsurance(self):

        # LIC- Life Insurance Corporation Of India Insurance Premium,BBPS Optionals

        Wait.wait_for_click(self.driver, (By.XPATH, self.btnInsurance_xpath)).click()
        mode = Select(self.driver.find_element(By.XPATH,self.selectMode_xpath))
        mode.select_by_visible_text("Offline")
        biller_Lic = Select(self.driver.find_element(By.XPATH, self.selectBiller_xpath))
        biller_Lic.select_by_visible_text("LIC- Life Insurance Corporation Of India Insurance Premium,BBPS Optionals")
        self.driver.find_element(By.XPATH,self.txtDOB_xpath).send_keys("14/10/1998")
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys("vrk9407@gmail.com")
        self.driver.find_element(By.XPATH,self.txtBillerNumber_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH,self.btnFitchBill_xpath).click()
        self.driver.find_element(By.XPATH,self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH,self.btnPayBill_xpath).click()
        if "Insurance" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_11_BBPSPage_LICPass.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_11_BBPSPage_LICFail.png")
        self.driver.find_element(By.XPATH, "//button[@id='closeModalButton']").click()

    def clickonPrepaid(self):


        # VI Bill Payment Prepaid

        Wait.wait_for_click(self.driver, (By.XPATH, self.btnPrepaid_xpath)).click()
        mode = Select(self.driver.find_element(By.XPATH, self.selectMode_xpath))
        mode.select_by_visible_text("Offline")
        biller_vi = Select(self.driver.find_element(By.XPATH, self.selectBiller_xpath))
        biller_vi.select_by_visible_text("VI Bill Payment Prepaid")
        self.driver.find_element(By.XPATH,self.txtBillerNumber_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH,self.btnFitchBill_xpath).click()
        self.driver.find_element(By.XPATH,self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH,self.btnPayBill_xpath).click()
        if "PREPAID" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_11_BBPSPage_viBillPass.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_11_BBPSPage_viBillFail.png")
        self.driver.find_element(By.XPATH, "//button[@id='closeModalButton']").click()


    def clickonEbill(self):
        Wait.wait_for_click(self.driver, (By.XPATH, self.btnEBill_xpath)).click()


    def clickonGas(self):

        # Aavantika Gas Ltd.

        Wait.wait_for_click(self.driver,(By.XPATH,self.btnGas_xpath)).click()
        mode = Select(self.driver.find_element(By.XPATH, self.selectMode_xpath))
        mode.select_by_visible_text("Offline")
        biller_vi = Select(self.driver.find_element(By.XPATH, self.selectBiller_xpath))
        biller_vi.select_by_visible_text("Aavantika Gas Ltd.")
        self.driver.find_element(By.XPATH,self.txtBillerNumber_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH,self.btnFitchBill_xpath).click()
        self.driver.find_element(By.XPATH,self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH,self.btnPayBill_xpath).click()

    def clickobCCPayment(self):
        self.driver.find_element(By.XPATH,self.lnkccPaymentMenu_xpath).click()




































