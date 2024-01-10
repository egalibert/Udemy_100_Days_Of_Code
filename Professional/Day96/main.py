import json
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():

	params = {
	'api_key': '',
	'airline_iata' : 'AY'
	}

	method = 'flights'
	api_base = 'http://airlabs.co/api/v9/'
	
	try:
		api_result = requests.get(api_base+method, params)
		api_response = api_result.json()
		pretty_json = json.dumps(api_response, indent=4)
		print(pretty_json)
		return render_template('index.html', data=api_response)
	except Exception as e:
		return f"Error: {str(e)}"


if __name__ == '__main__':
	app.run(debug=True)