from paho.mqtt import subscribe
import os
import json

class brokerConnector(object):

    def __init__(self,resources):
        self.resource_folder=resources
        os.chdir(os.getcwd()+os.sep+self.resource_folder)
        self.topic = "prd/FlightUpdate/#"
        self.connect_url = "a35ixnrwyoljwq.iot.eu-central-1.amazonaws.com"
        self.my_ca_cert = "VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem"
        self.my_key_cert = "pkey.pem"
        self.my_pri_cert = "mycert.pem"


    def callBroker(self):
        self.dict = {'ca_certs':self.my_ca_cert, 'certfile':self.my_pri_cert, 'keyfile':self.my_key_cert}
        brokerResponse= subscribe.simple(topics=self.topic,msg_count=10,hostname=self.connect_url,port=8883,transport="tcp",tls=self.dict)
        flight_list=[]
        for a in brokerResponse:
            print(a.topic)
            str_decode = str(a.payload.decode("utf-8", "ignore"))
            str_decode_json=json.loads(str_decode)
            print(str_decode_json["Update"]["Message"])
            if (str_decode_json["Update"]["Message"]=="New Estimated Departure"
                    or str_decode_json["Update"]["Message"]=="New Estimated Arrival"
                    or str_decode_json["Update"]["Message"]=="New Gate Information"):
                print(str_decode_json)
                flight_list.append(str_decode_json["Update"]["FlightNumber"])
        return flight_list

