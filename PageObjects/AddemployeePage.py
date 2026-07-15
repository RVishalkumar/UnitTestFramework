from selenium.webdriver.common.by import By

class AddEmployeePage:
    txt_Firstname_xpath = "//input[@name='firstName']"
    txt_Lastname_xpath = "//input[@name='lastName']"
    txtemailid_xpath = "//label[text()='Employee Id']/following::input[1]"
    btnSave_xpath = "//*[text()=' Save ']"

    def __init__(self,driver):
        self.driver = driver

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txt_Firstname_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txt_Lastname_xpath).send_keys(lname)


    def setEmpID(self,empid):
        self.driver.find_element(By.XPATH,self.txtemailid_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtemailid_xpath).send_keys(empid)

    def clickonSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()


