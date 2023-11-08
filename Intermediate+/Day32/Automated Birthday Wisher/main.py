import datetime as dt
import smtplib
import pandas
import random

MY_EMAIL = "elliotgalibert@gmail.com"
MY_PASSWORD = "1234567890123456"

# Date creation
now = dt.datetime.now()
month = dt.datetime.month
weekday = dt.datetime.day

today_tuple = (month, weekday)

# File formatting
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row)in data.iterrows()}

# print(birthdays_dict)

# Matching
if today_tuple in birthdays_dict:
	person = birthdays_dict[today_tuple]
	with open(f"letter_templates/letter_{random.randint(1, 4)}", "r") as letter:
		# print(letter)
		contents = letter.read()
		contents = contents.replace("[NAME]", person["name"])

# Mailing

	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(MY_EMAIL, MY_PASSWORD)
		connection.sendmail(
			from_addr=MY_EMAIL,
			to_addrs=person["email"],
			msg=f"Subject: Happy Birtday\n\n {contents}"
			)