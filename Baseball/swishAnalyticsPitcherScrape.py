from bs4 import BeautifulSoup
from selenium import webdriver
import urllib2
import demjson

def swishAnalyticsPitcherScrape():
	script = soup.find_all("script")
	script = script[20].text

	# strip all junk
	scriptJunk,rotoObject = script.split("this.pitcherArray")
	rotoObject,scriptJunk = rotoObject.split("this.updatedpitcherArray")
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

		opponent = (line['matchup'])
		opponent = opponent.replace("vs", "")
		opponent = opponent.replace("@", "")
		opponent = opponent.lstrip()

		projPts = (line['dk_pts'])
		projValue = (line['dk_value'])
		outs = (line['outs'])
		ER = (line['er'])
		hits = (line['h'])
		walks = (line['bb'])
		hbp = (line['hbp'])
		strikeouts = (line['so'])
		completeGame = (line['cg'])
		completeGameSO = (line['cgso'])
		noHit = (line['noh'])
		win = (line['win'])
		dk_avg = (line['dk_avg'])

		data = (playerName, salary, team, opponent, projPts, projValue, outs, ER, hits, walks, hbp, strikeouts, completeGame, completeGameSO, noHit, win, dk_avg)
		SwishAnalyticsPitcherProjections.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

url = "https://www.swishanalytics.com/optimus/mlb/dfs-pitcher-projections"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

SwishAnalyticsPitcherProjections = open('SwishAnalyticsPitcherProjections.csv', 'w')
SwishAnalyticsPitcherProjections.write("Player Name, Salary, Team, Opponent, Projected Points, Projected Value, Outs, Earned Runs, Hits, Walks, HBP, Strikeouts, Complete Game Probabiliy, Complete Game SO Probabiliy, No Hit Probabiliy, Win Probabiliy, DraftKings Average" + "\n")

swishAnalyticsPitcherScrape()

SwishAnalyticsPitcherProjections.close()