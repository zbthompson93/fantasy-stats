import requests

r = requests.get('https://www.espn.com/nba/team/stats/_/name/atl')
text = r.text
#print(r.text)

f = open("demofile.txt", "w")
f.write(text)
f.close()