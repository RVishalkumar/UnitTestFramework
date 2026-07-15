import time

from selenium.webdriver.common.by import By

class SearchEmployee:

    txt_searchemp_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
    btnsearch_xpath = "//button[@type='submit']"


    def __init__(self,driver):
        self.driver = driver

    def setEmployeeName(self,employeename):
        self.driver.find_element(By.XPATH,self.txt_searchemp_xpath).send_keys(employeename)

    def clickonSearch(self):
        self.driver.find_element(By.XPATH,self.btnsearch_xpath).click()
        k = self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div")
        for i in k:
            if "Vishal " in i.text:
                a = self.driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']").click()
                a.click()
            else:
                pass

time.sleep(5)