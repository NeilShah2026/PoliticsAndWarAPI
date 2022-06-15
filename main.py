from unicodedata import name
import requests
from bs4 import BeautifulSoup

r = requests.get('https://politicsandwar.com/nation/id=452632')
soup = BeautifulSoup(r.content, 'html.parser')


tags = soup.find_all('td', class_='notranslate')
tag_no_class = soup.find_all('td')

for i in tag_no_class:
    test_retrun = i.text
    print(test_retrun.strip())
    print('-----------------------------------------------------')

tag_list = []
for i in tags:
    tag_list.append(i.text)

print(f'Nation Name: {tag_list[0]}')
print(f'Nation Leader: {tag_list[1]}')