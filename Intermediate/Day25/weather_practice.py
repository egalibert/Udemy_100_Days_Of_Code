import csv
import pandas

# with open("weather_data.csv", "r") as file:
# 	data = file.readlines()
# 	print(data)


#EX1 extract all temperatures from file

temperatures = []

with open("weather_data.csv", "r") as file:
	data = csv.reader(file)
	for row in data:
		for info in row:
			if info.isdigit():
				temperatures.append(int(info))

	print(temperatures)

# EX2 Get Maximum temperature value

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
max_value = data["temp"].max()
print(max_value)

# EX3 calculate average temperatures from file

print(f"Average is {sum(temp_list) / len(temp_list)}")

print(data[data.temp == data.temp.max()])

data = pandas.read_csv("weather_data.csv")

# EX4 Get Monday temp as Fahrenheit

monday = data[data.day == "Monday"]
print((monday["temp"] * 1.8000) + 32)