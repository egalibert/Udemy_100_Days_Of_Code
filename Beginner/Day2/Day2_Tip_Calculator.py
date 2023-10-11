print(f"Welcome to the tip calculator.")
total = input("What was the total bill? $")
bill = float(total)
percentage = input("What percentage tip would you like to give? 10, 12, 15? ")
perc = int(percentage)
people_count = input("how many people to split the bill? ")
people = int(people_count)

extra = (bill / 100) * perc
result = (bill + extra) / 7
round(result, 2)
print(f"Each person should pay: ${round(result, 2)}")