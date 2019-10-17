# Eli Preston
# Upper Canada College
# This program displays the stock closing prices of APPLE from the past 4 years in a bar graph using Chart js

import requests
import json
import pprint

# Prints JSON data in a more readable form ~ http://jsonprettyprint.com/


def writeHTML(data, closingPrices, dates):
    myfile = open("myAPI.html","w")
    myfile.write("<h1>JSON file returned by API call</h1>")
    myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")

    # newColor2015 = []
    # color2015 = dates[:53]
    # print(color2015)

    # for i in color2015:
    #     print(i)
    #     newColor2015.append("'rgba(255, 0, 0, 1)'")
    # print(newColor2015)



    myfile.write("""
    <html>
        <canvas id="myChart" width="300" height="200"></canvas>
        <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>

        <script>
        var ctx = document.getElementById('myChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: """ + "".join(str(dates)) + """,
                datasets: [{
                    label: 'Closing Prices',
                    data: """ + "".join(str(closingPrices)) + """,
                    backgroundColor: [],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            },
            options: {     
                layout: {
                    padding: {
                        left: 50,
                        right: 50,
                        top: 50,
                        bottom: 50
                    }
                }
            }
        });

        </script>
    </html>
    """)
    myfile.close()



def main():
    response = requests.get("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL")

    if (response.status_code == 200):
      
        data = response.content
        data_as_str = data.decode()
        # writeHTML(data_as_str)
        datajson = response.json()
        
        dataSymbol = datajson['symbol']
        dataPoints = datajson['historical']
        #pprint.pprint(datajson)
        print(dataSymbol)



        closingPrices = []
        dates = []

        for point in dataPoints:
            #print(f"{point['ticker']}: \n\tOpen Price; {point['open']} \n\tChange; {point['changes']} \n\tDate; {point['date']}  \n")
            print(f"Date: {point['label']} \n\tOpening Price: {point['open']} \n\tClosing Price: {point['close']} \n\tChange: {point['change']} \n\n")
            closingPrices.append(point["close"])
            dates.append(point["date"])
            
        writeHTML(data_as_str, closingPrices, dates)
           
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
        writeHTML(data, [], [])

main()


