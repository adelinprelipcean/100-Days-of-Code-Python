# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except:
#             print("Error! Value couldn't be converted to integer!")
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# print("%.2f" % (sum(data["temp"])/len(data["temp"])))
# print(data["temp"].max())
# print(data.temp)
# print(data[data.temp == data.temp.max()])
# print((data[data.day == "Monday"].temp[0]) * 1.8 + 32)

data_dict = {
    "students" : ["Adelin", "Pictor", "Denys"],
    "scores" : [77, 34, 76]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")