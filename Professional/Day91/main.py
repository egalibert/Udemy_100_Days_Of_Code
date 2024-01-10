import requests

def pdf_to_text(pdf_path):
	import fitz  # PyMuPDF
	doc = fitz.open(pdf_path)
	text = ""
	for page_num in range(doc.page_count):
		page = doc[page_num]
		text += page.get_text()
	doc.close()
	return text

def text_to_speech_with_ispeech(text, api_key):
	api_url = "http://api.ispeech.org/api/rest"
	params = {
		"apikey": api_key,
		"action": "convert",
		"text": text,
		"format": "mp3"
	}

	response = requests.post(api_url, params=params)

	if response.status_code == 200:
		with open("output.mp3", "wb") as output_file:
			output_file.write(response.content)
		print("Text converted to speech. Output saved as 'output.mp3'")
	else:
		print(f"Error: {response.status_code}, {response.text}")

def pdf_to_speech_with_ispeech(pdf_path, api_key):
	text = pdf_to_text(pdf_path)
	text_to_speech_with_ispeech(text, api_key)

if __name__ == "__main__":
	# Replace 'your_pdf_file.pdf' and 'your_api_key' with the actual PDF file path and iSpeech API key
	pdf_file_path = 'CV.pdf'
	ispeech_api_key = 'your_api_key'
	
	pdf_to_speech_with_ispeech(pdf_file_path, ispeech_api_key)