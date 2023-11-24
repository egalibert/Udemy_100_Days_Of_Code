from flask import Flask, render_template
import random
from datetime import date
import requests

NAMEURL = "https://api.genderize.io?name=peter"

app = Flask(__name__)

@app.route('/')
def main():
	random_number  = random.randint(1, 10)
	today = date.today().year
	return render_template("index.html", num=random_number, current_date=today)

@app.route('/guess/<name>')
def guess(name):
	gender_url = f"https://api.genderize.io?name={name}"
	age_url = f"https://api.agify.io?name={name}"

	# Get the gender from genderize api
	gender_response = requests.get(gender_url)
	gender_data = gender_response.json()
	gender = gender_data["gender"]

	# Get the age from agify api
	age_response = requests.get(age_url)
	age_data = age_response.json()
	age = age_data["age"]

	return render_template("guess.html", name=name, gender=gender, age=age)

@app.route('/blog')
def get_blog():
	blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
	response = requests.get(blog_url)
	all_posts = response.json()
	return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
	app.run(debug=True)

