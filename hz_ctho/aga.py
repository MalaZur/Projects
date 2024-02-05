from bs4 import BeautifulSoup
with open(file='1\itgen.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup)

heading = soup.find(name='h1', id='name')
print(heading)

all_anchors_tags = soup.find_all(name='a')
for tag in all_anchors_tags:
    print(tag.getText())
    print(tag.get('href'))

paragraphs = soup.find_all(name='p')

print(paragraphs[1].getText())