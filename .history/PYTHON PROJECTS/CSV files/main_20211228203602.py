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
gray_squirrels_count = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrels[squirrels["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(squirrel_dict)
df.to_csv("squirrel_count.csv")
