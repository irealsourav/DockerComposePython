from utilities.BaseDriver import WebDriverBase

class Flights(WebDriverBase):

    def __init__(self,browser,text):
        super().__init__(browser)
        self.flight_Xpath="//input[@id='s2id_autogen2']"
        self.getBtnXpath="//div[@id='omniSearch']/../div[2]/button"
        self.text=text
    def setFlightNumber(self):

        return self.find_by_xpath(self.flight_Xpath).send_keys(self.text)
    def click_on_submit_btn(self):
        return self.find_by_xpath(self.getBtnXpath).click()






