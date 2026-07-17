from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Wait:

    @staticmethod
    def wait_for_click(driver, locator, timeout=5):
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @staticmethod
    def wait_for_visible(driver, locator, timeout=20):
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )