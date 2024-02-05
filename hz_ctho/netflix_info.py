import requests
from bs4 import BeautifulSoup

url = "https://www.netflix.com/lv-ru/title/81511780" #ссылка на фильм ль нетфликс, и поиск кое-какой информации

response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')

print("\nНазвание:")
print(soup.find(class_="title-title").getText())

print("\nЖанры:")
all_genres_tags = soup.find_all(class_="more-details-item item-genres")
for tag in all_genres_tags:
    print(tag.getText())

print("\nАктёры:")
all_actors = soup.find_all(class_="more-details-item item-cast")
for tag in all_actors:
    print(tag.getText())

print("\nОписание:")

print(soup.find(class_="title-info-synopsis").getText())