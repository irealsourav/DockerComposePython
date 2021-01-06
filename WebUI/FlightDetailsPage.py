from WebUI.TempPage import tempPage

class FlightDetails(tempPage):


    def __init__(self,browser,text):
        super().__init__(browser,text)

## Starting Details
        self.startingAirport = "//span[@class='flightPageSummaryCity']"
        self.departureDate = "//span[@class='flightPageSummaryDepartureDayAbbrv']"
        self.departureTime = "//span[@class='flightPageSummaryDeparture flightTime']"
## Destination Details
        self.destinationAirport = "//span[@class='destinationCity']"
        self.arrivalDate = "//span[@class='flightPageSummaryArrivalDayAbbrv']"
        self.arrivalTime = "//span[@class='flightPageSummaryArrival flightTime']"


    def getStartAirport(self):
        return self.find_by_xpath(self.startingAirport).text

    def getDestinationAirport(self):
       return self.find_by_xpath(self.destinationAirport).text

    def getDepartureDate(self):
       return self.find_by_xpath(self.departureDate).text

    def getArrivalDate(self):
       return self.find_by_xpath(self.arrivalDate).text

    def getDepartureTime(self):
       return self.find_by_xpath(self.departureTime).text

    def getArrivalTime(self):
       return self.find_by_xpath(self.arrivalTime).text


