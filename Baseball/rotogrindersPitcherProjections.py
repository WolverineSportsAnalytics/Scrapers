from bs4 import BeautifulSoup
import urllib2
import csv
import demjson

url = "https://rotogrinders.com/projected-stats/mlb-pitcher?site=draftkings"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

rotogrindersProjectionsMLB = open('rotogrindersPitcherProjections.csv', 'w')
rotogrindersProjectionsMLB.write("Player Name, Position, Salary, Team, Opponent, Player Hand, Ceiling, Floor, Projection, Value, xISO, xR, xSLG, xWOBA, xL, GP, lWOBA, rWOBA, lSLG, rSLG, SIERA, xFIP, lISO, rISO, GBPercentage, FBPercentage, IP" + "\n")

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
	xIso = (line['xiso'])
	xR = (line['xr'])
	xSLG = (line['xslg'])
	xWOBA = (line['xwoba'])
	#xk9 = (line["xk\/9"])
	xl = (line['xl'])
	gp = (line['gp'])
	lwoba = (line['lwoba'])
	rwoba = (line['rwoba'])
	#lk9 = (line['lk\/9'])
	#rk9 = (line['rk\/9'])
	lSLG = (line['lslg'])
	rSLG = (line['rslg'])
	SIERA = (line['siera'])
	xFIP = (line['xfip'])
	#HRFB = (line['hr\/fb'])
	lISO = (line['liso'])
	rISO = (line['riso'])
	GBPercentage = (line['gb%'])
	FBPercentage = (line['fb%'])
	IP = (line['ip'])
	playerName = (line['player_name'])
	position = (line['position'])
	salary = (line['salary'])
	team = (line['team'])
	opponent = (line['opp'])
	playerHand = (line['player']['hand'])
	ceil = (line['ceil'])
	floor = (line['floor'])
	points = (line['points'])
	value = (float) (points / ((float) (salary) / (1000)))
	value = round(value, 3)

	data = (playerName, position, salary, team, opponent, playerHand, ceil, floor, points, value, xIso, xR, xSLG, xWOBA,  xl, gp, lwoba, rwoba, lSLG, rSLG, SIERA, xFIP, lISO, rISO, GBPercentage, FBPercentage, IP)
	rotogrindersProjectionsMLB.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

rotogrindersProjectionsMLB.close()
