import csv

with open("./weather_data.csv") as weather_data:
    weather = csv.reader(weather_data)  
    temperatures = []
    for row in weather:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)