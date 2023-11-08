import datetime as dt
import smtplib
import random
import pandas

now = dt.datetime.now()
weekday = now.day()

my_email = "elliotgalibert@gmail.com"
my_password="yrrpfimetqopovhv"

if weekday == 0:
	with open("quotes.txt", "r") as file:
		all_quotes = file.readlines()
		quote = random.choice(all_quotes)

	connection = smtplib.SMTP("smpt.gmail.com", port=587)
	connection.starttls()
	connection.login(user=my_email, password=my_password)
	connection.sendmail(from_addr=my_email,
						to_addrs="extream-man@hotmail.com",
						msg=f"Subject: Monday Motivation\n\n{quote}")
	connection.close()

