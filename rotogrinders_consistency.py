#scraper for Rotogrinders Misc

from bs4 import BeautifulSoup
import urllib2
import csv
import demjson

url = "https://rotogrinders.com/game-stats/nba/consistency?site=fanduel&range=3weeks"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

rotogrinders_consistency = open('rotogrinders_consistency.csv', 'w')
rotogrinders_consistency.write("Player, Pos, Team, Salary, GP, FPPG, FPMAX, Floor, Ceil, %2x, %3x, %4x, %5x, %6x" + "\n")

script = soup.find_all('script')[6:7]
js_obj = script[0].text 

js_obj = js_obj.lstrip()
js_obj = js_obj.rstrip()
js_obj = js_obj[31:]
js_obj = js_obj.lstrip()
js_obj = js_obj[7:]

js_obj = js_obj[:-55]
js_obj = js_obj.rstrip()

py_obj = demjson.decode(js_obj)

"""
writer = csv.writer(rotogrinders_consistency, quoting=csv.QUOTE_NONE, quotechar='')
for row in py_obj:
    writer.writerow(row.values())
"""

for line in py_obj:
    player = line['player']
    pos = line['pos']
    team = line['team']
    salary = line['salary']
    gp = line['gp']
    fppg = line['fppg']
    fpmax = line['fpmax']
    floor = line['floor']
    ceil = line['ceil']
    p2x = float(line['%2x']) * 100
    p3x = float(line['%3x']) * 100
    p4x = float(line['%4x']) * 100
    p5x = float(line['%5x']) * 100
    p6x = float(line['%6x']) * 100

    if(salary is not None):
        data = (player, pos, team, salary, gp, fppg, fpmax, floor, ceil, p2x, p3x, p4x, p5x, p6x)
        rotogrinders_consistency.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s \n' % data)

rotogrinders_consistency.close()

reader = csv.reader(open("rotogrinders_consistency.csv"))

row = 0

html = '<table>'

for row in reader:
    html += '<tr>'
    for column in row:
            html += '<th>' 
            html += column 
            html += '</th>'
    html += '</tr>'

html += '</table>'
