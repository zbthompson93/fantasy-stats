import requests
import json
from bs4 import BeautifulSoup

teams = ['atl', 'bos', 'bkn', 'cha', 'chi', 'cle', 'dal', 'den', 'det', 'gs', 'hou', 'ind', 'lac', 'lal', 'mem', 'mia', 'mil', 'min', 'no', 'ny', 'okc', 'orl', 'pho', 'phi', 'por', 'sac', 'sa', 'tor', 'utah', 'was']

print(len(teams))

data = []

for team in teams:
    url = 'https://www.espn.com/nba/team/stats/_/name/{0}'.format(team)
    print(team)
    r = requests.get(url)
    text = r.text

    # Create soup object
    soup = BeautifulSoup(text, features="html.parser")
    #print(soup)

    # Initialize list for player stats
    players = []


    '''Get the data from the name table'''
    # Get name table
    nameTable = soup.find('table', class_='Table Table--align-right Table--fixed Table--fixed-left')

    # Get table header
    nameHeader = nameTable.find('thead').string

    # Get player names and add to players list as an object
    names = nameTable.find_all('a', class_='AnchorLink')
    for name in names:
        obj = {'name': name.text}
        players.append(obj)
        #print(name.text)


    '''Get the data from the stats table'''
    # Get stats table
    statsTable = soup.find('table', class_='Table Table--align-right')

    # Get headers for stats list
    statsList = statsTable.find('thead', class_='Table__header-group Table__THEAD')
    statsName = statsList.find_all('th')

    # Get table where stats are listed for each player
    statsBody = statsTable.find('tbody', class_='Table__TBODY')
    # Get the rows from that stats table to loop thru
    statsRows = statsBody.find_all('tr')

    # Get player positions and update players list
    pos = nameTable.find_all('span', class_='font10')
    # Loop thru each position
    for count, position in enumerate(pos):
        obj = players[count]
        obj.update({"position": position.contents[2]})
        obj.update({"team": team.upper()})

        # Get the matching row in the stats body table
        row = statsRows[count].find_all('td')

        #Add stats headers as keys and the stats from the rows var to each player object
        for count2, stats in enumerate(statsName):
            stat = row[count2].string
            obj.update({stats.string: stat})

    data = data + players


#print(players[9])


with open('data.json', 'w') as f:
    json.dump(data, f)


print("Done")