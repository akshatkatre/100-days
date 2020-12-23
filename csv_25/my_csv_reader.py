import csv
import pandas as pd

# with open('weather_data.csv') as file_handler:
#     data = csv.reader(file_handler)
#     temperature = []
#     next(data)
#     for row in data:
#         # print(row[1])
#         temperature.append(int(row[1]))
#
#     print(temperature)

# data = pd.read_csv('weather_data.csv')
# print(sum(data['temp'])/len(data['temp']))
# print(data['temp'].mean())

# print(data['temp'].max())
# print(data)
# print(data[data.day == 'Monday'])
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])
#
# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp) * 9/5 + 32
# print(monday_temp)

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_color_list = data['Primary Fur Color'].to_list()
fur_dict = {}
for item in fur_color_list:
    if item in fur_dict:
        fur_dict[item] += 1
    else:
        fur_dict[item] = 1

print(fur_dict)

squirrel_count_df = pd.DataFrame.from_dict(fur_dict)
print(squirrel_count_df)
