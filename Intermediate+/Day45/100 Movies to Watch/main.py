import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL).text

soup = BeautifulSoup(response, "html.parser")
movies = soup.find_all(name="h3", class_ = "title")

list_of_movies = []

for movie in movies:
	list_of_movies.append(movie.getText())

with open("movies.txt", "w") as file:
	index = len(list_of_movies) - 1
	while index >= 0:
		file.write(f"{list_of_movies[index]}\n")
		index -= 1
	