import pandas

data = pandas.read_csv("50_states.csv")
states = data["state"]
kirjasto = data.to_dict()

print(kirjasto)