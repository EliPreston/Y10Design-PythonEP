import requests
import pprint


def writeHTML(data):
	myfile = open("myAPI.html","w")
	myfile.write("<h1>JSON file returned by API call</h1>")
	myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
	myfile.write(data)
	myfile.close()


def main():
    response = requests.get("https://financialmodelingprep.com/api/v3/forex")

    if (response.status_code == 200):
      
        data = response.content
        #data_as_str = data.decode()
        datajson = response.json()
        dataPoints = datajson['forexList']
        pprint.pprint(datajson)

        for point in dataPoints:
            print(f"{point['ticker']}: \n\tPrice; {point['date']} \n\tChange; {point['changes']}\n")
            

    else:
        data = "Error has occured"
        writeHTML(data)

main()


