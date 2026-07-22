from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BbpsPage:

    btnDTH_xpath = "//a[@href='https://b2b.digifintel.com/retailer/bbps/getbbpsoperator/DTH']"
    selectModeDTH_xpath = "//select[@id='mode']"
    selectBiller_xpath = "//select[@id='operatorSubcategories']"
    txtBillerNumber_xpath = "//input[@id='ad0_name']"
    btnFitchBill_xpath = "//form[@id='dynamicForm']//button[@type='submit']"
    txtAmount_xpath = "//input[@id='amountInput']"
    txtTransactionPin_xpath = "//input[@id='userInput']"
    btnPayBill_xpath = "//div[@id='billContainer']/button"




    def __init__(self,driver):
        self.driver = driver

    def clickonDTH(self):

        # AIRTELDTH
        self.driver.find_element(By.XPATH,self.btnDTH_xpath).click()
        mode = Select(self.driver.find_element(By.XPATH,self.selectModeDTH_xpath))
        mode.select_by_visible_text("Online")
        biller_AirtelDTH = Select(self.driver.find_element(By.XPATH,self.selectBiller_xpath))
        biller_AirtelDTH.select_by_visible_text("AIRTELDTH")
        self.driver.find_element(By.XPATH,self.txtBillerNumber_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH,self.btnFitchBill_xpath).click()
        self.driver.find_element(By.XPATH,self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH,self.btnPayBill_xpath).click()

        # YES Bank
        self.driver.refresh()
        mode = Select(self.driver.find_element(By.XPATH, self.selectModeDTH_xpath))
        mode.select_by_visible_text("Online")
        biller_YesBank = Select(self.driver.find_element(By.XPATH, self.selectBiller_xpath))
        biller_YesBank.select_by_visible_text("YES Bank")
        self.driver.find_element(By.XPATH, self.txtBillerNumber_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH, self.btnFitchBill_xpath).click()
        self.driver.find_element(By.XPATH, self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH, self.btnPayBill_xpath).click()

        # IDFC
        self.driver.refresh()
        mode = Select(self.driver.find_element(By.XPATH, self.selectModeDTH_xpath))
        mode.select_by_visible_text("Online")
        biller_AirtelDTH = Select(self.driver.find_element(By.XPATH, self.selectBiller_xpath))
        biller_AirtelDTH.select_by_visible_text("IDFC")
        self.driver.find_element(By.XPATH, self.txtBillerNumber_xpath).send_keys("9407271094")
        self.driver.find_element(By.XPATH, self.btnFitchBill_xpath).click()
        self.driver.find_element(By.XPATH, self.txtTransactionPin_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH, self.btnPayBill_xpath).click()

