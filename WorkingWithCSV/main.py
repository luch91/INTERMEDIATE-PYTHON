# with open("./weather_data.csv") as data_file:
#    data = data_file.readlines()
#   print(data)

# import csv

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)


import pandas

data = pandas.read_csv("./weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

average_temp = sum(temp_list)/ len(temp_list)
print(average_temp)

print(data["temp"].mean())
print(data["temp"].max())

print(data.condition)

# Get rows data
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

wednesday = data[data.day == "Wednesday"]
print(wednesday.condition)

wednesday_temp = int(wednesday.temp)
wednesday_temp_f = (wednesday_temp * 9/5) + 32
print(wednesday_temp_f)

# create a dataframe from scratch

data_dict = {
    "students": ["Amy", "Luchi", "Meme"],
    "scores": [79, 84, 65]
}
# create a new csv file
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")






