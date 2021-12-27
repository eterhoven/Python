with open("./weather_data.csv") as weather_data:
    weather = weather_data.readlines()

weather_list = []
for element in weather:
    element = element.strip("\n")
    weather_list.append(element)

print(weather_list)