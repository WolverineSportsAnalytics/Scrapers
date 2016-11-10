from bs4 import BeautifulSoup
import urllib2
import csv
import demjson

url = "https://rotogrinders.com/projected-stats/mlb-hitter?site=draftkings"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

rotogrindersProjectionsMLB = open('rotogrindersBatterProjectionsMLB.csv', 'w')
rotogrindersProjectionsMLB.write("Player Name, Position, Secondary Position, Salary, Team, Opponent, Player Hand, Ceiling, Floor, Projection, Value, Pitcher Name, Pitcher Hand, Season AB, Season Average, Season wOBA, Season ISO, Season OBP, Season BABIP, Slugging Percentage, K Percentage, Walk Percentage, Season OPS" + "\n")

# get object
script = soup.find_all("script")
script = script[8].text

# strip all junk
scriptJunk,rotoObject = script.split("=")
rotoObject,scriptJunk = rotoObject.split("projectedStats.init(data)")
rotoObject = rotoObject.lstrip()
rotoObject = rotoObject.rstrip()
rotoObject = rotoObject[:-1]

rotoProj = demjson.decode(rotoObject)

for line in rotoProj:
	seasonAB = (line['ab'])
	avg = (line['avg'])
	woba = (line['woba'])
	iso = (line['iso'])
	obp = (line['obp'])
	slg = (line['slg'])
	kPercentage = (line['k%'])
	bb = (line['bb%'])
	ops = (line['ops'])
	babip = (line['babip'])
	playerName = (line['player_name'])
	position = (line['position'])
	secondaryPosition = ""
	if position.find('/') != -1:
		position,secondaryPosition = position.split("/")
	salary = (line['salary'])
	team = (line['team'])
	opponent = (line['opp'])
	playerHand = (line['player']['hand'])
	ceil = (line['ceil'])
	floor = (line['floor'])
	points = (line['points'])
	value = (float) (points / ((float) (salary) / (1000)))
	value = round(value, 3)
	pitcher = (line['pitcher'])
	pFirstName = (line['pitcher']['first_name'])
	pLastName = (line['pitcher']['last_name'])
	pitcherHand = (line['pitcher']['hand'])
	pitcherName = pFirstName + " " + pLastName

	data = (playerName, position, secondaryPosition, salary, team, opponent, playerHand, ceil, floor, points, value, pitcherName, pitcherHand, seasonAB, avg, woba, iso, obp, babip, slg, kPercentage, bb, ops)
	rotogrindersProjectionsMLB.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

rotogrindersProjectionsMLB.close()
