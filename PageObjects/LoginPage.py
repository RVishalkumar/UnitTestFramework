
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_name = "username"
    textbox_password_name = "password"
    btnLogin = "//button[@type='submit']"
    lnkPIM_menu_xpath = "//span[text()='PIM']"
    btnAddCustomer_xpath = "//a[text()='Add Employee']"




    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.NAME,self.textbox_username_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btnLogin).click()

    def clickonPIMMenu(self):
        self.driver.find_element(By.XPATH,self.lnkPIM_menu_xpath).click()

    def clickaddCustomer(self):
        self.driver.find_element(By.XPATH,self.btnAddCustomer_xpath).click()

