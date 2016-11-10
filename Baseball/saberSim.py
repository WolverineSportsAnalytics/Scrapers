from bs4 import BeautifulSoup
from selenium import webdriver
import urllib2
import csv

def saberSimScrape():
	for tr in soup.find_all('tr')[76:]:
		tds = tr.find_all('td')

		playerLink = tds[0].find_all('a')
		player = playerLink[0].text
		player = str(player.encode('utf-8'))

		team = tds[1].text
		team = str(team.encode('utf-8'))

		game = tds[2].text
		game = str(game.encode('utf-8'))

		pos = tds[3].text
		pos = str(pos.encode('utf-8'))

		pa = tds[4].text
		pa = str(pa.encode('utf-8'))

		hits = tds[5].text
		hits = str(hits.encode('utf-8'))

		singles = tds[6].text
		singles = str(singles.encode('utf-8'))

		doubles = tds[7].text
		doubles = str(doubles.encode('utf-8'))

		triples = tds[8].text
		triples = str(triples.encode('utf-8'))

		homeruns = tds[9].text
		homeruns = str(homeruns.encode('utf-8'))

		runs = tds[10].text
		runs = str(runs.encode('utf-8'))

		rbi = tds[11].text
		rbi = str(rbi.encode('utf-8'))

		stolenbases = tds[12].text
		stolenbases = str(stolenbases.encode('utf-8'))

		caughtstealing = tds[13].text
		caughtstealing = str(caughtstealing.encode('utf-8'))

		walks = tds[14].text
		walks = str(walks.encode('utf-8'))

		strikeouts = tds[15].text
		strikeouts = str(strikeouts.encode('utf-8'))

		yahooProj = tds[16].text
		yahooProj = str(yahooProj.encode('utf-8'))

		fanduelProj = tds[17].text
		fanduelProj = str(fanduelProj.encode('utf-8'))

		draftkingsProj = tds[18].text
		draftkingsProj = str(draftkingsProj.encode('utf-8'))

		data = (player, team, game, pos, pa, hits, singles, doubles, triples, homeruns, runs, rbi, stolenbases, caughtstealing, walks, strikeouts, yahooProj, fanduelProj, draftkingsProj)
		SaberSimProjections.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

SaberSimProjections = open('SaberSimProjections.csv', 'w')
SaberSimProjections.write("Player, Team, Game, Pos, PA, H, 1B, 2B, 3B, HR, R, RBI, SB, CS, BB, SO, Yahoo, FanDuel, DraftKings" + "\n")

driver = webdriver.Chrome()
driver.get('http://www.fangraphs.com/dailyprojections.aspx?pos=all&stats=bat&type=sabersim')

html = driver.page_source
soup = BeautifulSoup(html)
saberSimScrape()

driver.execute_script("__doPostBack('DFSBoard1$dg1$ctl00$ctl03$ctl01$ctl06','')")

html = driver.page_source
soup = BeautifulSoup(html)
saberSimScrape()

driver.execute_script("__doPostBack('DFSBoard1$dg1$ctl00$ctl03$ctl01$ctl07','')")

html = driver.page_source
soup = BeautifulSoup(html)
saberSimScrape()

driver.execute_script("__doPostBack('DFSBoard1$dg1$ctl00$ctl03$ctl01$ctl08','')")

html = driver.page_source
soup = BeautifulSoup(html)
saberSimScrape()

driver.execute_script("__doPostBack('DFSBoard1$dg1$ctl00$ctl03$ctl01$ctl09','')")

html = driver.page_source
soup = BeautifulSoup(html)
saberSimScrape()

driver.execute_script("__doPostBack('DFSBoard1$dg1$ctl00$ctl03$ctl01$ctl10','')")

html = driver.page_source
soup = BeautifulSoup(html)
saberSimScrape()

driver.execute_script("__doPostBack('DFSBoard1$dg1$ctl00$ctl03$ctl01$ctl11','')")

html = driver.page_source
soup = BeautifulSoup(html)
saberSimScrape()

driver.execute_script("__doPostBack('DFSBoard1$dg1$ctl00$ctl03$ctl01$ctl12','')")

html = driver.page_source
soup = BeautifulSoup(html)
saberSimScrape()

driver.execute_script("__doPostBack('DFSBoard1$dg1$ctl00$ctl03$ctl01$ctl13','')")

html = driver.page_source
soup = BeautifulSoup(html)
saberSimScrape()

SaberSimProjections.close()