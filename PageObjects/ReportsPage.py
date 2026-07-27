from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ReportsPage:

    txtFrom_xpath = "//input[@id='fromDate']"
    txtTo_xpath = "//input[@id='toDate']"
    dropdownStatus_xpath = "//select[@id='status']"
    btnSearch_xpath = "//div[@class='form-group d-flex gap-2 col-lg-3']/button[1]"
    btnAction1_xpath = "//table[@id='dataTable']/tbody/tr[5]/td[13]"
    btnClose_xpath = "//div[@class='modal-footer']/button[1]"
    btnReset_xpath = "//div[@class='form-group d-flex gap-2 col-lg-3']/button[3]"
    txtTransactionID_xpath = "//input[@id='txnid']"
    btnAction2_xpath = "//table[@id='dataTable']/tbody/tr/td[13]"
    btnAction3_xpath = "//table[@id='dataTable']/tbody/tr[3]/td[16]"
    btnAction4_xpath = "//table[@id='dataTable']/tbody/tr/td[16]"
    txtOrderId_xpath = "//input[@id='orderid']"
    btnAction5_xpath = "//table[@id='dataTable']/tbody/tr/td[16]"
    btnAction6_xpath = "//table[@id='dataTable']/tbody/tr[2]/td[17]"
    btnAction7_xpath = "//table[@id='dataTable']/tbody/tr/td[17]"
    btnAction8_xpath = "//table[@id='dataTable']/tbody/tr[1]/td[13]"
    btnAction9_xpath = "//table[@id='dataTable']/tbody/tr/td[13]"
    btnAction10_xpath = "//table[@id='dataTable']/tbody/tr[3]/td[16]"
    btnAction11_xpath = "//table[@id='dataTable']/tbody/tr[2]/td[16]"
    btnAction12_xpath = "//table[@id='dataTable']/tbody/tr/td[16]"
    btnAction13_xpath = "//table[@id='dataTable']/tbody/tr[2]/td[12]"
    btnAction14_xpath = "//table[@id='dataTable']/tbody/tr/td[12]"
    btnAction15_xpath = "//table[@id='dataTable']/tbody/tr/td[15]"
    lnkMyPlanMenu_xpath = "//*[@id='sidebar-menu']/li[15]"




    def __init__(self,driver):
        self.driver = driver

    # Ledger Reports

    def setFillterByDateAndStatusLadger(self):
        self.driver.find_element(By.XPATH,self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH,self.txtTo_xpath).send_keys("24-07-2026")
        status = Select(self.driver.find_element(By.XPATH,self.dropdownStatus_xpath))
        status.select_by_visible_text("Pending")
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH,self.btnAction1_xpath).click()
        if "ledger?_token?" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_PendingStatusLadger.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_PendingStatusLadger.png")
        self.driver.find_element(By.XPATH,self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH,self.btnReset_xpath).click()


    def setFillterByTransactionIDLadger(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        self.driver.find_element(By.XPATH,self.txtTransactionID_xpath).send_keys("DEMOPDV4888463b97")
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH,self.btnAction2_xpath).click()
        if "ledger?_token?" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByTransactionIDLadger.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByTransactionIDLadger.png")
        self.driver.find_element(By.XPATH,self.btnClose_xpath).click()


        # DMT Reports

    def setFillterByDateAndStatusDMT(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        status = Select(self.driver.find_element(By.XPATH, self.dropdownStatus_xpath))
        status.select_by_visible_text("Failed")
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH,self.btnAction3_xpath).click()
        if "dmt" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FailedDMTStatusp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FailedDMTStatusf.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH,self.btnReset_xpath).click()

    def setFillterByTransactionIDDMT(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).send_keys("DEMODMTd1400c455c")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction4_xpath).click()
        if "dmt" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByTransactionIDDMTp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByTransactionIDDMTf.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).clear()
        self.driver.find_element(By.XPATH,self.btnReset_xpath).click()



    def setFillterByOrderIdDMT(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("27-07-2026")
        self.driver.find_element(By.XPATH,self.txtOrderId_xpath).send_keys("260721184713")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH,self.btnAction5_xpath).click()
        if "dmt" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByOrderIDDMTp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByOrderIDDMTf.png")

    # Payout Reports

    def setFillterByDateAndStatusPayout(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        status = Select(self.driver.find_element(By.XPATH, self.dropdownStatus_xpath))
        status.select_by_visible_text("Failed")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH,self.btnAction6_xpath).click()
        if "payout" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FailedPayoutReportp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FailedPayoutReportf.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH,self.btnReset_xpath).click()

    def setFillterByTransactionIDPayout(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).send_keys("DEMODPAY4f72721d91")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction7_xpath).click()
        if "payout" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByTransactionIPayoutp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByTransactionIDPayoutf.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).clear()
        self.driver.find_element(By.XPATH, self.btnReset_xpath).click()


    def setFillterByOrderIdPayout(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("27-07-2026")
        self.driver.find_element(By.XPATH,self.txtOrderId_xpath).send_keys("260722484895")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH,self.btnAction7_xpath).click()
        if "payout" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByOrderIDPayoutp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByOrderIDPayoutf.png")

    # Recharge Reports

    def setFillterByDateandStatusRecharge(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        status = Select(self.driver.find_element(By.XPATH, self.dropdownStatus_xpath))
        status.select_by_visible_text("Success")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH,self.btnAction8_xpath).click()
        if "payout" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_RechargePage_FilterByDateandStatusRechargep.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportPage_FilterByDateandStatusRechargef.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH, self.btnReset_xpath).click()


    def setFillterByTransactionIDRecharge(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).send_keys("DEMOREd3bdde129a")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction9_xpath).click()
        if "recharge" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByTransactionIDRechargep.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByTransactionIDRechargef.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).clear()
        self.driver.find_element(By.XPATH, self.btnReset_xpath).click()


    def setFillterByOrderIdRecharge(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("27-07-2026")
        self.driver.find_element(By.XPATH,self.txtOrderId_xpath).send_keys("260721936055")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH,self.btnAction9_xpath).click()
        if "recharge" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByOrderIDRechargep.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByOrderIDRechargef.png")

    #  BBPS Reports

    def setFillterByDateandStatusBbps(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        status = Select(self.driver.find_element(By.XPATH, self.dropdownStatus_xpath))
        status.select_by_visible_text("Success")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction10_xpath).click()
        if "bbps" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_RechargePage_FilterByDateandStatusBbpsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportPage_FilterByDateandStatusBbpsf.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH, self.btnReset_xpath).click()

    def setFillterByTransactionIDBbps(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).send_keys("DEMOBBPS62cbebe350")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction11_xpath).click()
        if "bbps" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByTransactionIDBbpsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByTransactionIDBbpsf.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).clear()
        self.driver.find_element(By.XPATH, self.btnReset_xpath).click()


    def setFillterByOrderIdBbps(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("27-07-2026")
        self.driver.find_element(By.XPATH,self.txtOrderId_xpath).send_keys("260723302271")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH,self.btnAction12_xpath).click()
        if "bbps" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByOrderIDBbpsp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByOrderIDBbpsf.png")


    #    Credit Card Reports

    def setFillterByDateandStatusCCPay(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        status = Select(self.driver.find_element(By.XPATH, self.dropdownStatus_xpath))
        status.select_by_visible_text("Failed")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction13_xpath).click()
        if "ccpay" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_RechargePage_FilterByDateandStatusCCPayp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportPage_FilterByDateandStatusCCPayf.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH, self.btnReset_xpath).click()


    def setFillterByTransactionIDCCPay(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).send_keys("DEMOCCPdbd306b647")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction14_xpath).click()
        if "ccpay" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByTransactionIDCCPayp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByTransactionIDCCPayf.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).clear()
        self.driver.find_element(By.XPATH, self.btnReset_xpath).click()

    def setFillterByOrderIdCCPay(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("27-07-2026")
        self.driver.find_element(By.XPATH, self.txtOrderId_xpath).send_keys("260723704467")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction14_xpath).click()
        if "ccpay" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByOrderIDCCPayp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByOrderIDCCPayf.png")

    #  UPI Reports

    def setFillterByDateandStatusUPIPayment(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        status = Select(self.driver.find_element(By.XPATH, self.dropdownStatus_xpath))
        status.select_by_visible_text("Success")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction8_xpath).click()
        if "upi" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_RechargePage_FilterByDateandStatusUPIPaymentp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportPage_FilterByDateandStatusUPIPaymentf.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH, self.btnReset_xpath).click()


    def setFillterByTransactionIDUPIPayment(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).send_keys("DEMOUPIPAY3ec3b5afe4")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction8_xpath).click()
        if "upi" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByTransactionIDUPIPayment.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByTransactionIDUPIPaymentf.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).clear()
        self.driver.find_element(By.XPATH, self.btnReset_xpath).click()

    def setFillterByOrderIdUPIPayment(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("27-07-2026")
        self.driver.find_element(By.XPATH, self.txtOrderId_xpath).send_keys("260723916110")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction9_xpath).click()
        if "upi" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByOrderIDUPIPaymentp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByOrderIDUPIPaymentf.png")

    # Swiftx Reports

    def setFillterByDateandStatusSwiftX(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        status = Select(self.driver.find_element(By.XPATH, self.dropdownStatus_xpath))
        status.select_by_visible_text("Failed")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction15_xpath).click()
        if "swiftx" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_RechargePage_FilterByDateandStatusSwiftXPaymentp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportPage_FilterByDateandStatusSwiftXPaymentf.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH, self.btnReset_xpath).click()


    def setFillterByTransactionIDSwiftX(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("24-07-2026")
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).send_keys("DEMOSWXf8f96db8ba")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction15_xpath).click()
        if "swiftx" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByTransactionIDSwiftPayment.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByTransactionIDSwiftPaymentf.png")
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()
        self.driver.find_element(By.XPATH, self.txtTransactionID_xpath).clear()
        self.driver.find_element(By.XPATH, self.btnReset_xpath).click()

    def setFillterByOrderIdUPIPayment(self):
        self.driver.find_element(By.XPATH, self.txtFrom_xpath).send_keys("01-07-2026")
        self.driver.find_element(By.XPATH, self.txtTo_xpath).send_keys("27-07-2026")
        self.driver.find_element(By.XPATH, self.txtOrderId_xpath).send_keys("260724279379")
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAction15_xpath).click()
        if "swiftx" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_16_ReportsPage_FilterByOrderIDSwiftPaymentp.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_16_ReportsPage_FilterByOrderIDSwiftPaymentf.png")


    def clickonMyPlanMenu(self):
        self.driver.find_element(By.XPATH,self.lnkMyPlanMenu_xpath).click()





