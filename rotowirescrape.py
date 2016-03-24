#scraper for RotoWire DFS Stats

from bs4 import BeautifulSoup
import urllib2

url = "http://www.rotowire.com/daily/nba/optimizer.htm?site=FanDuel&sport=NBA&projections="


page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    print "Name: %s, Team: %s, Opponent: %s, Position: %s, Money Line: $%s, O/U: $%s, Proj. Mins: %s, FD Salary: %s, Proj. Points: %s, Value: %s" % \
    (tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text, tds[7].text, tds[8].text, tds[9].text, tds[10].text)