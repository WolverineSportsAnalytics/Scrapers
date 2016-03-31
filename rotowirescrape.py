#scraper for RotoWire DFS Stats

from bs4 import BeautifulSoup
import urllib2
import csv

url = "http://www.rotowire.com/daily/nba/optimizer.htm?site=FanDuel&sport=NBA&projections="


page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

rotowire = open('rotowire.csv', 'w')
rotowire.write("Name, Team, Opponent, Position, Money Line, O/U, Proj. Mins, FD Salary, Proj. Points, Value" + "\n")

for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    data = (tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text, tds[7].text, tds[8].text, tds[9].text, tds[10].text)
    
    #name
    name = tds[1].text
    if name.find('GTD') != -1: #throws an error if "GTD" is listed in the table after player name, so we must remove it
    	name = name[:-4]
    if name.find('Out') != -1:
    	name = name[:-4]
    name = name.encode('ascii')
    name = str(name)

    team = tds[2].text
    team = str(team.encode('ascii'))

    opponent = tds[3].text
    opponent = str(opponent.encode('ascii'))

    position = tds[4].text

    moneyline = tds[5].text
    moneyline = str(moneyline.encode('ascii'))

    overunder = tds[6].text
    overunder = str(overunder.encode('ascii'))

    projmin = tds[7].text
    projmin = str(projmin.encode('ascii'))

    salary = tds[8].text
    salary = str(salary[1:])
    salaries = salary.split(',') #this must be created because some salaries are > 10,000 and some are 9,000 and below
    salary = str(salaries[0]) + str(salaries[1]) #FIXME

    projpts = tds[9].text
    projpts = str(projpts.encode('ascii'))

    value = tds[10].text
    value = str(value.encode('ascii'))


    data = (name, team, opponent, position, moneyline, overunder, projmin, salary, projpts, value)
    rotowire.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

rotowire.close()