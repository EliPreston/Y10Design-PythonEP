# Eli Preston
# Upper Canada College
# This program displays the stock closing prices of APPLE from 2014 to 2019 in a bar graph using Chart js.

import requests
import json
import pprint



def writeHTML(data, closingPrices, dates):
    myfile = open("appleAPI.html","w")
    myfile.write("""
    
    <!DOCTYPE html>
    <html>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">

    <head>
    
    <title>API Home Page</title>
    
    <link rel="stylesheet" href="../HTML/homestyle.css">
    <link rel='icon' href='favicon (1).ico' type='image/x-icon'/ >


    <ul>
        <li><a href="../HTML/eli.html" id="special"class="left" style="float:left;">Home</a></li>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </ul>


    
    """)


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
        
        <div class="headerAPI" id="home">
            <p id="big"><b>Apple API Display</b></p>
            <p id="small">This website is displaying data from an Apple API.</p>
            <p></p>
        </div>

        
        <canvas id="myChart" width="300" height="200"></canvas>
        <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>

        <script>
        var ctx = document.getElementById('myChart').getContext('2d');
        var myChart = new Chart(ctx, {
        
            type: 'bar',
            data: {
                labels: """ + "".join(str(dates)) + """,
                datasets: [{
                    label: 'Closing Prices of Apple From 2014 to Present Day (In $$$)',
                    
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
        </head>

        <body>
            
            <div class="rowapi" id="rowapi">

                <div class="column">
                    <a href="https://financialmodelingprep.com/api/v3/historical-price-full/AAPL" style="text-decoration:none;" target="_blank">
                    <img src="../HTML/ImagesHTML/apiuseddoc.png" style="width:100%" onclick="" class="hover-shadow cursor">
                    <div class="overlay">
                    <div class="text">API Used</div>
                    </div>
                </div>
            
                
                <div class="column">
                    <a href="https://www.chartjs.org/docs/latest/" style="text-decoration:none;" target="_blank">
                    <img src="../HTML/ImagesHTML/gettingstarted.png" style="width:100%" onclick="" class="hover-shadow cursor">
                    <div class="overlay">
                    <div class="text">Chart JS; Used For Graph</div>
                    </div>
                </div>


                <div class="column">
                    <a href="https://github.com/EliPreston" style="text-decoration:none;">
                    <img src="../HTML/ImagesHTML/github-logo.jpeg" style="width:100%" onclick="" class="hover-shadow cursor">
                    <div class="overlay">
                    <div class="text">GitHub</div>
                    </div>
                </div>
            
                
                <div class="column">
                    <a href="https://sites.google.com/ucc.on.ca/y10design-epres" style="text-decoration:none;">
                    <img src="../HTML/ImagesHTML/googlesitesnew99.png" style="width:100%" onclick="" class="hover-shadow cursor">
                    <div class="overlay">
                    <div class="text">Google Site</div>
                    </div>
                </div>
            

            </div>
            
        </body>

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
        changes = []


        for point in dataPoints:
            print(f"Date: {point['label']} \n\tOpening Price: {point['open']} \n\tClosing Price: {point['close']} \n\tChange: {point['change']} \n\n")
            closingPrices.append(point["close"])
            dates.append(point["date"])
            changes.append(point["change"])

            
        writeHTML(data_as_str, closingPrices, dates)

    else:
        data = "Error has occured"
        writeHTML(data, [], [])

main()


