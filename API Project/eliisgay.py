import requests
import json
import pprint

# Prints JSON data in a more readable form ~ http://jsonprettyprint.com/


def writeHTML(data):
	myfile = open("myAPI.html","w")
	myfile.write("<h1>JSON file returned by API call</h1>")
	myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
	myfile.write(data)
	myfile.close()


def main():
    response = requests.get("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL")

    if (response.status_code == 200):
      
        data = response.content
        data_as_str = data.decode()
        writeHTML(data_as_str)
        datajson = response.json()
        
        dataSymbol = datajson['symbol']
        dataPoints = datajson['historical']
        #pprint.pprint(datajson)
        
        
        print(dataSymbol)

        for point in dataPoints:
            #print(f"{point['ticker']}: \n\tOpen Price; {point['open']} \n\tChange; {point['changes']} \n\tDate; {point['date']}  \n")
            print(f"Date: {point['label']} \n\tOpening Price: {point['open']} \n\tClosing Price: {point['close']} \n\tChange: {point['change']} \n\n")
           
        """
            #writeHTML(variable)
        myfile = open("myAPI.html","w")
	    myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
	    myfile.write(data)
	    myfile.close()
        """
        #writeHTML(variable)

    else:
        data = "Error has occured"
        writeHTML(data)

main()


