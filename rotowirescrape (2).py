#scraper for RotoWire DFS Stats

from bs4 import BeautifulSoup
import urllib2

url = "http://www.rotowire.com/daily/nba/optimizer.htm?site=FanDuel&sport=NBA&projections="


page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

print "Name Team Opponent Position Money Line O/U Proj. Mins FD Salary Proj. Points Value"

for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    print "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % \
    (tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text, tds[7].text, tds[8].text, tds[9].text, tds[10].text)