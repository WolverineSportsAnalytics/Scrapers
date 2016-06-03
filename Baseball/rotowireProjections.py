#scraper for RotoWire MLB DFS Stats

from bs4 import BeautifulSoup
from string import whitespace
import urllib2
import csv

url = "http://www.rotowire.com/daily/mlb/optimizer.htm?site=DraftKings&sport=MLB"


page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

rotowireMLB = open('rotowireMLB.csv', 'w')
rotowireMLB.write("Name, Bats, Team, Pitcher Thowing Arm, Position, Batting Order Position, Opponent, Opponent Throwing Arm, Salary, Proj. Points, Ceiling, Floor, Value, Money Line, Over Under" + "\n")

for tr in soup.find_all('tr')[4:]:
	tds = tr.find_all('td')

	#name
	playerInfo = tds[1]

	playerName = playerInfo.a
	playerName = playerName.text
	playerName = str(playerName.encode('utf-8'))

	playerStance = playerInfo.span

	if playerStance != None:
		playerStance = playerStance.text
		if playerStance == 'B':
			playerStance = 'S'
		if playerStance == 'DTD':
			playerStance = "None"
		playerStance = str(playerStance.encode('utf-8'))

	team = tds[2]['data-team']
	team = str(team.encode('utf-8'))

	teamPitcherArm = tds[2].span
	teamPitcherArm = teamPitcherArm.text
	teamPitcherArm = str(teamPitcherArm.encode('utf-8'))

	position = tds[3].text
	position = str(position.encode('utf-8'))

	battingOrder = tds[4]['data-slot']
	battingOrder = str(battingOrder.encode('utf-8'))

	tds2 = tr.find_all('td', recursive=False)

	opponent = tds2[5].text
	opponent = opponent.replace('@', '')
	opponent = opponent.encode('ascii', 'ignore')
	opponent = opponent.translate(None, whitespace)
	opponent = opponent.replace("(L)", "")
	opponent = opponent.replace("(R)", "")
	opponent = str(opponent.encode('utf-8'))

	opponentData = tds[5]
	opponentThrowArm = opponentData.span
	if opponentThrowArm != None:
		opponentThrowArm = opponentThrowArm.text
		opponentThrowArm = opponentThrowArm.lstrip()
		opponentThrowArm = opponentThrowArm.rstrip()
		opponentThrowArm = str(opponentThrowArm.encode('utf-8'))

	salary = tds[6].text
	salary = str(salary[1:])
	salaries = salary.split(',') #this must be created because some salaries are > 10,000 and some are 9,000 and below
	salary = str(salaries[0]) + str(salaries[1]) #FIXME

	projpts = tds[7].text
	projpts = projpts.lstrip()
	projpts = projpts.rstrip()
	projpts = str(projpts.encode('utf-8'))
	if projpts == '':
		projpts = tds[7]['data-points']
		projpts = projpts.lstrip()
		projpts = projpts.rstrip()
		projpts = str(projpts.encode('utf-8'))

	ceiling = tds[7]['data-ceiling']
	ceiling = ceiling.lstrip()
	ceiling = ceiling.rstrip()
	ceiling = str(ceiling.encode('utf-8'))

	floor = tds[7]['data-floor']
	floor = floor.lstrip()
	floor = floor.rstrip()
	floor = str(floor.encode('utf-8'))

	value = tds[8].text
	value = value.lstrip()
	value = value.rstrip()
	value = str(value.encode('utf-8'))

	moneyLine = tds[9].text
	moneyLine = str(moneyLine.encode('utf-8'))

	overUnder = tds[10].text
	overUnder = str(overUnder.encode('utf-8'))

	data = (playerName, playerStance, team, teamPitcherArm, position, battingOrder, opponent, opponentThrowArm, salary, projpts, ceiling, floor, value, moneyLine, overUnder)
	rotowireMLB.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

rotowireMLB.close()