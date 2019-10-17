

import requests
import json
import pprint



def writeHTML(data):
	myfile = open("justinAPI.html","w")
	myfile.write("<h1>JSON file returned by API call</h1>")
	myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
	myfile.write(data)
	myfile.close()

def main():
    response = requests.get("https://financialmodelingprep.com/api/cryptocurrency?datatype=json")

    if (response.status_code == 200):
        data = response.content
        datajson = response.json()
        dataPoints = datajson['BTC']
        pprint.pprint(datajson)

    for point in dataPoints:
        print(f"{point['ticker']}: \n\tPrice; {point['date']} \n\tChange; {point['changes']}\n")
        #print(dataPoints)
        
    else:
        data = "Error has occured"
        writeHTML(data)
main()