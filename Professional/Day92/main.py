from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
from collections import Counter
import json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/extract_colors', methods=['POST'])
def extract_colors():
	file = request.files['image']

	if file:
		image = Image.open(file)
		image_array = np.array(image)

		# Flatten the 3D image array to a 2D array
		flat_image_array = image_array.reshape((-1, 3))

		# Get the most common colors
		common_colors = [tuple(color) for color, count in Counter(map(tuple, flat_image_array)).most_common(10)]

		# Convert RGB to HEX
		hex_colors = ['#%02x%02x%02x' % color for color in common_colors]

		response_data = {'colors': hex_colors}
		return jsonify(response_data)

	return jsonify({'error': 'No image provided'})

if __name__ == '__main__':
	app.run(debug=True)

