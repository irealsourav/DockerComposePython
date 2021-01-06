from WebUI.SearchFlightPage import Flights

class tempPage(Flights):

    def __init__(self,browser,text):
        super().__init__(browser,text)
        self.agreeBtn="//div[@class='qc-cmp2-summary-buttons']/button[2]"


    def clickOnAgree(self):
        return self.find_by_xpath(self.agreeBtn).click()
