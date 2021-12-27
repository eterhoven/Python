import csv

with open("./weather_data.csv") as weather_data:
    weather = csv.reader(weather_data)
    for row in weather:
        print(row)