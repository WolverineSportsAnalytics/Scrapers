from bs4 import BeautifulSoup
from selenium import webdriver
import urllib2
import demjson

def swishAnalyticsPitcherScrape():
	script = soup.find_all("script")
	script = script[18].text

	# strip all junk
	scriptJunk,rotoObject = script.split("this.batterArray")
	rotoObject,scriptJunk = rotoObject.split("this.updatedBatterArray")
	rotoObject = rotoObject[2:]
	rotoObject = rotoObject.lstrip()
	rotoObject = rotoObject.rstrip()
	rotoObject = rotoObject[:-1]

	rotoProj = demjson.decode(rotoObject)

	for line in rotoProj:
		team = (line['team_short'])
		playerName = (line['player_name'])
		salary = (line['dk_salary'])
		salary = salary.replace(",", "")
		bats = (line['bats'])
		dk_pos = (line['dk_pos'])

		opponent = (line['matchup'])
		opponent = opponent.replace("vs", "")
		opponent = opponent.replace("@", "")
		opponent = opponent.lstrip()

		projPts = (line['dk_pts'])
		projValue = (line['dk_value'])
		outs = (line['outs'])
		ab = (line['ab'])
		bb = (line['bb'])
		hbp = (line['hbp'])
		singles = (line['singles'])
		doubles = (line['doubles'])
		triples = (line['triples'])
		hr = (line['hr'])
		rbi = (line['rbi'])
		runs = (line['runs'])
		sb = (line['sb'])
		cs = (line['cs'])
		dk_avg = (line['dk_avg'])

		data = (playerName, salary, bats, dk_pos, team, opponent, projPts, projValue, outs, ab, bb, hbp, singles, doubles, triples, hr, rbi, sb, cs, dk_avg)
		SwishAnalyticsBatterProjections.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

url = "https://www.swishanalytics.com/optimus/mlb/dfs-batter-projections"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

SwishAnalyticsBatterProjections = open('SwishAnalyticsBatterProjections.csv', 'w')
SwishAnalyticsBatterProjections.write("Player Name, Salary, Bats, Position, Team, Opponent, Projected Points, Projected Value, Outs, AB, Walks, HBP, Singles, Doubles, Triples, HR, RBI, SB, CS, DraftKings Average" + "\n")

swishAnalyticsPitcherScrape()

SwishAnalyticsBatterProjections.close()