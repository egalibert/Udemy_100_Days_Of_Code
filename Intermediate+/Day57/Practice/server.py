from flask import Flask, render_template
import random
from datetime import date

app = Flask(__name__)

@app.route('/')
def main():
	random_number  = random.randint(1, 10)
	today = date.today().year
	return render_template("index.html", num=random_number, current_date=today)

if __name__ == "__main__":
	app.run(debug=True)