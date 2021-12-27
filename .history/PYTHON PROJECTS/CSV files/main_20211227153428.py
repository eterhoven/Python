#import csv

#with open("./weather_data.csv") as weather_data:
#    weather = csv.reader(weather_data)  
#    temperatures = []
#    for row in weather:
#        if row[1] != 'temp':
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas

weather = pandas.read_csv("./weather_data.csv")

temp_list = weather["temp"].to_list()
print(temp_list)