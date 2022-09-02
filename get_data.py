import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.espn.com/nba/team/stats/_/name/atl')
text = r.text
#print(r.text)

# f = open("index.html", "w")
# f.write(text)
# f.close()

players = []

soup = BeautifulSoup(text, features="html.parser")
#print(soup)

nameTable = soup.find('table', class_='Table Table--align-right Table--fixed Table--fixed-left')

nameHeader = nameTable.find('thead').string
#print(nameHeader)

names = nameTable.find_all('a', class_='AnchorLink')
for name in names:
    obj = {'name': name.text}
    players.append(obj)
    #print(name.text)

pos = nameTable.find_all('span', class_='font10')
#print(pos)

for count, position in enumerate(pos):
    obj = players[count]
    obj.update({"position": position.contents[2]})

print(players)