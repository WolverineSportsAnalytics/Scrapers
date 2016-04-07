#scraper for Rotogrinders Pace

from bs4 import BeautifulSoup
import urllib2
import csv

def team_name_to_abbreviation(name):
    return {
        "Atlanta": "ATL",
        "Brooklyn": "BKN",
        "Boston": "BOS",
        "Charlotte": "CHA",
        "Chicago": "CHI",
        "Cleveland": "CLE",
        "Dallas": "DAL",
        "Denver": "DEN",
        "Detroit": "DET",
        "Golden State": "GS",
        "Houston": "HOU",
        "Indiana": "IND",
        "L.A. Clippers": "LAC",
        "L.A. Lakers": "LAL",
        "Memphis": "MEM",
        "Miami": "MIA",
        "Milwaukee": "MIL",
        "Minnesota": "MIN",
        "New Orleans": "NOP",
        "New York": "NYK",
        "Oklahoma": "OKC",
        "Orlando": "ORL",
        "Philadelphia": "PHI",
        "Phoenix": "PHX",
        "Portland": "POR",
        "Sacramento": "SAC",
        "San Antonio": "SA",
        "Toronto": "TOR",
        "Utah": "UTA",
        "Washington": "WSH"
    }.get(name, name)

url = "https://rotogrinders.com/pages/nba-offense-vs-defense-pace-and-scoring-174522"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

rotogrinder_pace = open('rotogrinder_pace.csv', 'w')
rotogrinder_pace.write("Team, Opponent, Pace, PPG, OffRtg, Pace, PPG-A, DefRtg, Pace, Pts, AvgRtg" + "\n")

for tr in soup.find_all('tr')[5:]:
    tds = tr.find_all('td')
    data = (tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text, tds[7].text, tds[8].text, tds[9].text, tds[10].text)
    
    team = tds[0].text
    team = team.lstrip()
    team = team.rstrip()
    team = str(team.encode('utf-8'))
    team = team_name_to_abbreviation(team)

    opponent = tds[1].text
    opponent = opponent.lstrip()
    opponent = opponent.rstrip()
    opponent = str(opponent.encode('utf-8'))
    opponent = team_name_to_abbreviation(opponent)

    pace1 = tds[2].text
    pace1 = str(pace1.encode('ascii'))

    ppg = tds[3].text
    ppg = str(ppg.encode('ascii')) 

    offRtg = tds[4].text
    offRtg = str(offRtg.encode('ascii'))

    pace2 = tds[5].text
    pace2 = str(pace2.encode('ascii'))

    ppgA = tds[6].text
    ppgA = str(ppgA.encode('ascii'))

    defRtg = tds[7].text
    defRtg = str(defRtg.encode('ascii'))

    pace3 = tds[8].text
    pace3 = str(pace3.encode('ascii'))

    pts = tds[9].text
    pts = str(pts.encode('ascii'))

    avgRtg = tds[10].text
    avgRtg = str(avgRtg.encode('ascii'))

    data = (team, opponent, pace1, ppg, offRtg, pace2, ppgA, defRtg, pace3, pts, avgRtg)
    rotogrinder_pace.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

rotogrinder_pace.close()

reader = csv.reader(open("rotogrinder_pace.csv"))

row = 0

html = '<table>'

for row in reader:
    html += '<tr>'
    for column in row:
            html += '<th>' 
            html += column 
            html += '</th>'
    html += '</tr>'

html += '</table>'