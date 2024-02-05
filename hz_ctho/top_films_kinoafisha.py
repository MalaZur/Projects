import requests
from bs4 import BeautifulSoup

url = "https://www.kinoafisha.info/rating/"

response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')

print("\nЛучшие фильмы в прокате:")
top_movies = soup.find_all(class_="movieItem_title")
for tag in top_movies:
    print(tag.getText())

