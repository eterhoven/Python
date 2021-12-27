import csv

with open("./weather_data.csv") as weather_data:
    weather = csv.reader(weather_data)
    weather.pop(0)
    print(weather)
    
    
    
    
    
    
    #temperatures = []
    #for row in weather:
        #temperatures.append(row[1])
    #print(temperatures)