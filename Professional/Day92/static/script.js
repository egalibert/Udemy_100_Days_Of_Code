function extractColors() {
	const input = document.getElementById('imageInput');
	const file = input.files[0];

	if (file) {
		const formData = new FormData();
		formData.append('image', file);

		fetch('/extract_colors', {
			method: 'POST',
			body: formData
		})
		.then(response => response.json())
		.then(data => displayColors(data.colors))
		.catch(error => console.error('Error:', error));
	}
}

function displayColors(colors) {
	const colorPalette = document.getElementById('colorPalette');
	colorPalette.innerHTML = '';

	colors.forEach(color => {
		const colorBox = document.createElement('div');
		colorBox.style.backgroundColor = color;
		colorBox.classList.add('color-box');
		colorPalette.appendChild(colorBox);
	});
}
