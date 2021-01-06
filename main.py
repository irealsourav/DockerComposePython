# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from WebUI.FlightDetailsPage import FlightDetails
from WebUI.TempPage import tempPage
from utilities.BrokerConnector import brokerConnector
import sys
from configparser import ConfigParser
from WebUI.SearchFlightPage import Flights

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        print("starting")
        parser=ConfigParser()
        parser.read('setup.ini')
        brokerConn=brokerConnector("resources")
        resp=brokerConn.callBroker()
        ##resp=['LH888', 'UA058', 'OS975', 'UA222', 'UA592', 'LH431', 'UA1549', 'UA3531']
        if(len(resp)==0):
            sys.exit("No Flight with new estimated departure or new estimated arrival or new gate information")
        else:
            for item in resp:
                try:
                    fDetails = FlightDetails(parser.get('Environment','browser'), item)
                    fDetails.open(parser.get('Environment','url'))
                    fDetails.setFlightNumber()
                    fDetails.click_on_submit_btn()
                    fDetails.clickOnAgree()
                    print(f"Flight Number is {item} :: ")
                    print("Starting Journey with Airport :: "+ fDetails.getStartAirport().strip())
                    print(f"Destination Airport :: "+fDetails.getDestinationAirport().strip())
                    print(" Time :: "+ fDetails.getDepartureTime().strip())
                    print("Time :: "+ fDetails.getArrivalTime().strip())
                    fDetails.close()
                except:
                    print(sys.exc_info()[0])
                    fDetails.close()

    except:
        print ("parser error"+sys.exc_info()[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
