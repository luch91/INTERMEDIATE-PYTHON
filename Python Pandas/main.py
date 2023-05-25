# The Great Squirrel Census Data Analysis

import pandas

data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(f"The number of grey squirrels = {grey_squirrels_count}")
print(f"The number of red squirrels = {red_squirrels_count}")
print(f"The number of black squirrels = {black_squirrels_count}")

# to construct dataframe

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

