import csv

with open("./weather_data.csv") as weather_data:
    weather = csv.reader(weather_data)
    temperatures = []
    for row in weather:
        temperatures.append(row[2])
    print(temperatures)