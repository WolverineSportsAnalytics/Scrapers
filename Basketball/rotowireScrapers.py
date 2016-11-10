#scraper for RotoWire Last 10 FanDuel PG Defense vs. Position DFS Stats

from bs4 import BeautifulSoup
import urllib2
import csv

def rotowire_scraper_pg():
	url = "http://www.rotowire.com/daily/nba/defense-vspos.htm?statview=last10"
	csv_filename = 'rotowireDvP_PG_basketball.csv'
	rotowire_scraper(url, csv_filename)

def rotowire_scraper_sg():
	url = "http://www.rotowire.com/daily/nba/defense-vspos.htm?statview=last10&pos=SG"
	csv_filename = 'rotowireDvP_SG_basketball.csv'
	rotowire_scraper(url, csv_filename)

def rotowire_scraper_sf():
	url = "http://www.rotowire.com/daily/nba/defense-vspos.htm?statview=last10&pos=SF"
	csv_filename = 'rotowireDvP_SF_basketball.csv'
	rotowire_scraper(url, csv_filename)

def rotowire_scraper_pf():
	url = "http://www.rotowire.com/daily/nba/defense-vspos.htm?statview=last10&pos=PF"
	csv_filename = 'rotowireDvP_PF_basketball.csv'
	rotowire_scraper(url, csv_filename)

def rotowire_scraper_c():
	url = "http://www.rotowire.com/daily/nba/defense-vspos.htm?statview=last10&pos=C"
	csv_filename = 'rotowireDvP_C_basketball.csv'
	rotowire_scraper(url, csv_filename)

def rotowire_scraper(url, csv_filename):
	abbrevs = {'Philadelphia 76ers':'PHI','Minnesota Timberwolves':'MIN','Washington Wizards':'WAS', 'Cleveland Cavaliers':'CLE',
			   'New Orleans Pelicans':'NOP', 'Houston Rockets':'HOU', 'Portland Trail Blazers':'POR', 'Denver Nuggets':'DEN',
			   'Detroit Pistons':'DET', 'Dallas Mavericks':'DAL', 'Los Angeles Lakers':'LAL', 'Los Angeles Clippers':'LAC',
			   'Miami Heat':'MIA', 'San Antonio Spurs':'SAS', 'Atlanta Hawks':'ATL', 'Brooklyn Nets':'BKN', 'Phoenix Suns':'PHO',
			   'New York Knicks':'NYK', 'Golden State Warriors':'GSW', 'Memphis Grizzlies':'MEM', 'Sacramento Kings':'SAC',
			   'Boston Celtics':'BOS', 'Milwaukee Bucks':'MIL', 'Charlotte Hornets':'CHA', 'Toronto Raptors':'TOR',
			   'Indiana Pacers':'IND', 'Orlando Magic':'ORL', 'Utah Jazz':'UTA', 'Chicago Bulls':'CHI', 'Oklahoma City Thunder':'OKC'}

	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page, "html.parser")

	file = open(csv_filename, 'w')
	file.write("Team, Vs. Pos, Season, Last 5, Last 10, PTS, REB, AST, STL, BLK, 3PM, FG%, FT%, TO" + "\n")

	for tr in soup.find_all('tr')[2:]:
		stats = tr.find_all('td')
		for stat in stats:
			if stat.text in abbrevs.keys():
				stat = stat.text
				file.write(abbrevs[stat] + ',')
			else:
				file.write(stat.text + ',')
		file.write('\n')

if __name__ == "__main__":
	rotowire_scraper_pg()
	rotowire_scraper_sg()
	rotowire_scraper_sf()
	rotowire_scraper_pf()
	rotowire_scraper_c()