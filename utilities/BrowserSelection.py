from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager import chrome


class BrowserSelection(object):

    def __init__(self,browser):
        self.browser=browser


    def get_browser(self):
        if self.browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")
            options.add_argument("--headless")

            return webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options)
        if self.browser == "firefox":
            return webdriver.firefox(executable_path=GeckoDriverManager().install())