import requests
from bs4 import BeautifulSoup
import csv


def scrape_nba_player_stats():
	url = "https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc"

	# Make a GET request to the URL
	response = requests.get(url)
	response.raise_for_status()

	soup = BeautifulSoup(response.text, 'html.parser')

	# Find the table containing player stats
	table = soup.find('table', class_='Table')

	# Extract data and write to CSV
	with open('nba_player_stats.csv', 'w', newline='', encoding='utf-8') as csvfile:
		csv_writer = csv.writer(csvfile)
		csv_writer.writerow(['Rank', 'Name', 'Team', 'GP', 'PPG', 'RPG', 'APG', 'SPG', 'BPG'])
		rows = table.find_all('tr', class_='Table__TR')
		for row in rows:
			columns = row.find_all(['th', 'td'])
			data = [col.text.strip() for col in columns]
			csv_writer.writerow(data)
	print("Scraping completed. Data saved to nba_player_stats.csv")

if __name__ == "__main__":
	scrape_nba_player_stats()