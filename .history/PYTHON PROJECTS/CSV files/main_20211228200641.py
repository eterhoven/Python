#import csv

#with open("./weather_data.csv") as weather_data:
#    weather = csv.reader(weather_data)  
#    temperatures = []
#    for row in weather:
#        if row[1] != 'temp':
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas

#weather = pandas.read_csv("./weather_data.csv")

#print(weather[weather["temp"] == weather["temp"].max()])

#monday = weather[weather["day"] == "Monday"]
#print((monday.temp) * (9/5) + 32)

squirrels = pandas.read_csv("./CP_squirrel.csv")
gray_squirrels = squirrels[squirrels["Primary Fur Color"] == "Gray"]
print(gray_squirrels)