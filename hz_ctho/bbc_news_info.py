import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')

print("\nСамые популярные новости:")
top_news = soup.find_all(class_="gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs")
for tag in top_news:
    print(tag.getText())

