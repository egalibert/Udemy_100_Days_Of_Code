import pandas

data = pandas.read_csv("squirrel_count.csv")

grey_s = len(data[data["Primary Fur Color"] == "Gray"])
red_s = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_s = len(data[data["Primary Fur Color"] == "Black"])

print(grey_s, red_s, black_s)

data_dict = {
	"Fur Color": ["Gray", "Cinnamon", "Black"],
	"Count": [grey_s, red_s, black_s]
}

file = pandas.DataFrame(data_dict)

file.to_csv("Squirrels_Final")

# list_version = column.to_list()
# dict_version = column.to_dict()

# t_gray = 0
# t_black = 0
# t_red = 0

# for color in list_version:
# 	if color == "Gray":
# 		t_grey += 1
# 	elif color == "Black":
# 		t_black += 1
# 	else:
# 		t_red += 1

# # print(list_version)
# print(t_red, t_black, t_gray)