from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", rel= "noreferrer")
article_texts = []
article_links = []
for article_tag in articles:
	text = article_tag.getText()
	article_texts.append(text)
	link = article_tag.get("href")
	article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name= "span", class_ = "score")]

biggest = max(article_upvotes)
index = article_upvotes.index(biggest)

print(article_texts[index])
print(article_links[index])
print(article_upvotes[index])