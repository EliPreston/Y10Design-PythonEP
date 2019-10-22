# Eli Preston
# Upper Canada College
# This program displays the stock closing prices of APPLE from 2014 to 2019 in a bar graph using Chart js.

import requests
import json
import pprint



def writeHTML(data, closingPrices, dates):
    myfile = open("appleAPI.html","w")
    myfile.write("<h1>JSON file returned by API call</h1>")
    myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")

    bgColors = []
    for date in dates:
        if date[:4] == "2014":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2015":
            bgColors.append("'rgba(255, 255, 0, 1)'")
        elif date[:4] == "2016":
            bgColors.append("'rgba(255, 0, 0, 1)'")
        elif date[:4] == "2017":
            bgColors.append("'rgba(0, 0, 255, 1)'")
        elif date[:4] == "2018":
            bgColors.append("'rgba(255, 0, 255, 1)'")
        elif date[:4] == "2019":
            bgColors.append("'rgba(0, 255, 255, 1)'")



    fourteen = []
    fifteen = []
    sixteen = []
    seventeen = []
    eighteen = []
    nineteen = []

    index = 0
    for yr in dates:
        if yr[:4] == "2014":
            print('2014')
            fourteen.append(closingPrices[index])
        elif yr[:4] == "2015":
            print('2015')
            fifteen.append(closingPrices[index])
        elif yr[:4] == "2016":
            print('2016')
            sixteen.append(closingPrices[index])
        elif yr[:4] == "2017":
            print('2017')
            seventeen.append(closingPrices[index])
        elif yr[:4] == "2018":
            print('2018')
            eighteen.append(closingPrices[index])
        elif yr[:4] == "2019":
            print('2019')
            nineteen.append(closingPrices[index])
        index += 1
    
    print(fourteen)
    print(fifteen)
    print(sixteen)
    print(seventeen)
    print(eighteen)
    print(nineteen)


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
                    label: 'Closing Prices of Apple From 2014 - Present',
                    data: """ + "".join(str(closingPrices)) + """,
                    backgroundColor: [""" + ",".join(bgColors) + """],
                    borderColor: [
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
        datajson = response.json()
        
        dataSymbol = datajson['symbol']
        dataPoints = datajson['historical']
        print(dataSymbol)



        closingPrices = []
        dates = []

        for point in dataPoints:
            print(f"Date: {point['label']} \n\tOpening Price: {point['open']} \n\tClosing Price: {point['close']} \n\tChange: {point['change']} \n\n")
            closingPrices.append(point["close"])
            dates.append(point["date"])
            
        writeHTML(data_as_str, closingPrices, dates)

    else:
        data = "Error has occured"
        writeHTML(data, [], [])

main()


