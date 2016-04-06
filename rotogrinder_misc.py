#scraper for Rotogrinders Misc

from bs4 import BeautifulSoup
import urllib2
import csv
import demjson

url = "https://rotogrinders.com/game-stats/nba-player?site=fanduel&range=3weeks"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

rotogrinder_misc = open('rotogrinder_misc.csv', 'w')
rotogrinder_misc.write("Player, Team, Pos, Salary, GP, MIN, REB, AST, STL, BLK, TO, PTS, USG, FPTS" + "\n")

script = soup.find_all('script')[6:7]
js_obj = script[0].text
js_obj = js_obj.lstrip()
js_obj = js_obj.rstrip()
js_obj = js_obj[31:]
js_obj = js_obj.lstrip()
js_obj = js_obj[11:]
js_obj = js_obj[:-55]
js_obj = js_obj.rstrip()
js_obj = js_obj[:-30]
js_obj = js_obj.rstrip()
js_obj = js_obj[:-1]

py_obj = demjson.decode(js_obj)




for line in py_obj:
    player = line['player']
    team = line['team']
    pos = line['pos']
    salary = line['salary']
    gp = line['gp']
    mins = line['min']
    reb = line['reb']
    ast = line['ast']
    stl = line['stl']
    blk = line['blk']
    to = line['to']
    pts = line['pts']
    usg = line['usg']
    fpts = line['fpts']
    fpts = float(fpts) / float(gp)
    fpts = round(fpts, 2)

    if(salary is not None):
        data = (player, team, pos, salary, gp, mins, reb, ast, stl, blk, to, pts, usg, fpts)
        rotogrinder_misc.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

rotogrinder_misc.close()


