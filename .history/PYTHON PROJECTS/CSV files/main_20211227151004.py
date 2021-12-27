import csv

with open("./weather_data.csv") as weather_data:
    weather = csv.reader(weather_data)
    temperatures = []
    for row[1::] in weather:
        temperatures.append(row[1])
    print(temperatures)