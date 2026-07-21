from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class RechargePage:

    txtmobilenumber_xpath = "//input[@id='premobile']"
    dropdownmobileOperator_xpath = "//select[@id='preoperator']"
    btnbrowsPlan_xpath = "//button[@id='checkMobileButton']"


    def __init__(self,driver):
        self.driver = driver


    def mobileRecharge(self):
        self.driver.find_element(By.XPATH,self.txtmobilenumber_xpath).send_keys("9407271094")
        select = Select(self.driver.find_element(By.XPATH,self.dropdownmobileOperator_xpath))
        select.select_by_visible_text("BSNL Prepaid")
        self.driver.find_element(By.XPATH,self.btnbrowsPlan_xpath).click()
        topup=self.driver.find_element(By.XPATH,"(//h5[@class='mt-4'])[3]")
        self.driver.execute_script("arguments[0].scrollIntoView()", topup)
        self.driver.find_element(By.XPATH,"//div[@id='plansContainer'']/table[3]/tbody/tr[4]/td[4]/button").click()
        self.driver.find_element(By.XPATH,"(//button[@data-bs-dismiss='modal'])[1]").click()
        self.driver.find_element(By.XPATH,"//input[@id='pretxnpin']").send_keys("1234")
        self.driver.find_element(By.XPATH,"//form[@id='prepaidForm']/div[3]/div[3]").click()


    def dthRecharge(self):
        self.driver.find_element(By.XPATH,"(//li[@role='presentation'])[2]").click()
        self.driver.find_element(By.XPATH,"//input[@id='dthmobile']").send_keys("9631312967")
        select = Select(self.driver.find_element(By.XPATH,"//select[@id='dthoperator']"))
        select.select_by_visible_text("Airtel Digital Tv Bill Payment DTH")
        self.driver.find_element(By.XPATH,"//button[@id='checkdthplan']").click()
        self.driver.find_element(By.XPATH,"//input[@id='dthamount']").send_keys("499")
        self.driver.find_element(By.XPATH,"//input[@id='dthtxnpin']").send_keys("1234")
        self.driver.find_element(By.XPATH,"//*[@id='dthForm']/div[3]/div[3]/button").click()


    def clickonHistory(self):
        self.driver.find_element(By.XPATH,"(//li[@role='presentation'])[3]").click()
        if "transaction" in self.driver.current_url:
            self.driver.save_screenshot(".\\Screenshortpass\\test_07_RechargePage_HistoryPass.png")
        else:
            self.driver.save_screenshot(".\\Screenshortfail\\test_07_DMTPage_HistoryFail.png")


    def clickonAEPSMenu(self):
        self.driver.find_element(By.XPATH,"//*[@id='sidebar-menu']/li[6] ").click()