from flask import Flask
app = Flask(__name__)

print(__name__)

def make_bold(function):
	def wrapper_function():
		return "<b>" + function() + "</b>"
	return wrapper_function

def make_emphasis(function):
	def wrapper_function():
		return "<em>" + function() + "</em>"
	return wrapper_function

def make_underlined(function):
	def wrapper_function():
		return "<u>" + function() + "</u>"
	return wrapper_function

@app.route('/')
def hello_world():
	return '<h1 style="text-align: center">Verttisivu!</h1>' \
			'<p>Tässä on vertti.</p>' \
			'<img src="https://i.ytimg.com/vi/aW785SL0GxU/oar2.jpg?sqp=-oaymwEkCJUDENAFSFqQAgHyq4qpAxMIARUAAAAAJQAAyEI9AICiQ3gB&rs=AOn4CLDF26HE9B9qwpXbDzmxoWJv0KXreg" width=100>' \
			'<img src="https://i.ytimg.com/vi/YXsUR-DtwVY/oar2.jpg?sqp=-oaymwEkCJUDENAFSFqQAgHyq4qpAxMIARUAAAAAJQAAyEI9AICiQ3gB&rs=AOn4CLDJ1PKKv8LD_POXQgl4mtD4s9Cytw" width=100>' \
			'<h2><img src="https://media.giphy.com/media/MjVChG7uD9oG1kCQNy/giphy.gif"></h2>' \

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
	return "Bye!"

@app.route("/<name>")
def greet(name):
	return f"Hello {name}"

if __name__ == "__main__":
	app.run(debug=True)