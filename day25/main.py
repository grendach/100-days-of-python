# with open("./weather_data.csv") as weather_data:
#     data = weather_data.readlines()

# print(data)

# # Read CSV

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Working with Pandas library
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# # Convert DataFrames to Dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # Convert Series to List
# data_list = data["temp"].to_list()



# # Find average value of list 
# # 1. Using Python
# avg_temp = sum(data_list) / len(data_list)
# print(f"Average temp: {avg_temp}")

# # 2. Using Pandas
# print(f"Pandas average temp: {data['temp'].mean()}")

# # Find max temp using Pandas
# print(f"Pandas max temp: {data['temp'].max()}")

# # Get Data in Colomns
# print(data["condition"])
# print(data.condition)

# # Get Data in Rows
# print(data[data.day == "Monday"])

# # Get Row of data where temp was MAX:
# print(data[data.temp == data.temp.max()])

# # Get particular colomns from particular raw

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 +32
# print(monday_temp_F)

# Create DataFrame from scratch
# data_dict = {
#     "students": ["Igor", "Dmytro", "Sergii"],
#     "scores": [10, 23, 26]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# Squirell Census data analysis
data = pandas.read_csv("input_data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])


print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)


data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count ]
}
sq_data = pandas.DataFrame(data_dict)
sq_data.to_csv("output_data.csv")
