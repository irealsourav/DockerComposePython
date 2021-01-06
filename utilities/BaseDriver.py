from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.BrowserSelection import BrowserSelection

class WebDriverBase(BrowserSelection):
    __TIMEOUT = 10

    def __init__(self,browser):
        super().__init__(browser)
        self._web_driver=self.get_browser()
        self._web_driver_wait = WebDriverWait(self._web_driver, WebDriverBase.__TIMEOUT)

    def open(self, url):
        self._web_driver.get(url)

    def find_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_name(self, name):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def finds_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def close(self):
        self._web_driver.quit()

    def javascript_executpr(self,xpath,sendKey_text):
        self._web_driver.execute_script('''
              var elem = arguments[0];
              var value = arguments[1];
              elem.value = value;
              ''', xpath, sendKey_text)
