#scraper for Rotogrinders Advanced Stats

from bs4 import BeautifulSoup
import urllib2
import csv

url = "https://rotogrinders.com/pages/nba-advanced-player-stats-guards-181885"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

rotogrindersAdvancedStats = open('rotogrindersAdvancedStats.csv', 'w')
rotogrindersAdvancedStats.write("Player, Team, Pts, Reb, Ast, Stl, Blk, eFG%, TS%, USG%, O-Rt, D-Rt, DRE/36, PER" + "\n")

for tr in soup.find_all('tr')[5:]:
    tds = tr.find_all('td')

    name = tds[0].text
    name = name.lstrip()
    name = name.rstrip()
    name = str(name.encode('utf-8'))

    team = tds[1].text
    team = team.lstrip()
    team = team.rstrip()
    team = str(team.encode('utf-8'))

    pts = tds[2].text
    pts = pts.lstrip()
    pts = pts.rstrip()
    pts = str(pts.encode('utf-8'))

    reb = tds[3].text
    reb = reb.lstrip()
    reb = reb.rstrip()
    reb = str(reb.encode('utf-8'))

    ast = tds[4].text
    ast = ast.lstrip()
    ast = ast.rstrip()
    ast = str(ast.encode('utf-8'))

    stl = tds[5].text
    stl = stl.lstrip()
    stl = stl.rstrip()
    stl = str(stl.encode('utf-8'))

    blk = tds[6].text
    blk = blk.lstrip()
    blk = blk.rstrip()
    blk = str(blk.encode('utf-8'))

    eFG = tds[7].text
    eFG = eFG.lstrip()
    eFG = eFG.rstrip()
    eFG = str(eFG.encode('utf-8'))

    ts = tds[8].text
    ts = ts.lstrip()
    ts = ts.rstrip()
    ts = str(ts.encode('utf-8'))

    usg = tds[9].text
    usg = usg.lstrip()
    usg = usg.rstrip()
    usg = str(usg.encode('utf-8'))

    ort = tds[10].text
    ort = ort.lstrip()
    ort = ort.rstrip()
    ort = str(ort.encode('utf-8'))

    drt = tds[11].text
    drt = drt.lstrip()
    drt = drt.rstrip()
    drt = str(drt.encode('utf-8'))

    dre36 = tds[12].text
    dre36 = dre36.lstrip()
    dre36 = dre36.rstrip()
    dre36 = str(dre36.encode('utf-8'))

    per = tds[13].text
    per = per.lstrip()
    per = per.rstrip()
    per = str(per.encode('utf-8'))

    data = (name, team, pts, reb, ast, stl, blk, eFG, ts, usg, ort, drt, dre36, per)
    rotogrindersAdvancedStats.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

url = "https://rotogrinders.com/pages/nba-advanced-player-stats-centers-181888"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

for tr in soup.find_all('tr')[5:]:
    tds = tr.find_all('td')

    name = tds[0].text
    name = name.lstrip()
    name = name.rstrip()
    name = str(name.encode('utf-8'))

    team = tds[1].text
    team = team.lstrip()
    team = team.rstrip()
    team = str(team.encode('utf-8'))

    pts = tds[2].text
    pts = pts.lstrip()
    pts = pts.rstrip()
    pts = str(pts.encode('utf-8'))

    reb = tds[3].text
    reb = reb.lstrip()
    reb = reb.rstrip()
    reb = str(reb.encode('utf-8'))

    ast = tds[4].text
    ast = ast.lstrip()
    ast = ast.rstrip()
    ast = str(ast.encode('utf-8'))

    stl = tds[5].text
    stl = stl.lstrip()
    stl = stl.rstrip()
    stl = str(stl.encode('utf-8'))

    blk = tds[6].text
    blk = blk.lstrip()
    blk = blk.rstrip()
    blk = str(blk.encode('utf-8'))

    eFG = tds[7].text
    eFG = eFG.lstrip()
    eFG = eFG.rstrip()
    eFG = str(eFG.encode('utf-8'))

    ts = tds[8].text
    ts = ts.lstrip()
    ts = ts.rstrip()
    ts = str(ts.encode('utf-8'))

    usg = tds[9].text
    usg = usg.lstrip()
    usg = usg.rstrip()
    usg = str(usg.encode('utf-8'))

    ort = tds[10].text
    ort = ort.lstrip()
    ort = ort.rstrip()
    ort = str(ort.encode('utf-8'))

    drt = tds[11].text
    drt = drt.lstrip()
    drt = drt.rstrip()
    drt = str(drt.encode('utf-8'))

    dre36 = tds[12].text
    dre36 = dre36.lstrip()
    dre36 = dre36.rstrip()
    dre36 = str(dre36.encode('utf-8'))

    per = tds[13].text
    per = per.lstrip()
    per = per.rstrip()
    per = str(per.encode('utf-8'))

    data = (name, team, pts, reb, ast, stl, blk, eFG, ts, usg, ort, drt, dre36, per)
    rotogrindersAdvancedStats.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

url = "https://rotogrinders.com/pages/nba-advanced-player-stats-forwards-181887"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

for tr in soup.find_all('tr')[5:]:
    tds = tr.find_all('td')

    name = tds[0].text
    name = name.lstrip()
    name = name.rstrip()
    name = str(name.encode('utf-8'))

    team = tds[1].text
    team = team.lstrip()
    team = team.rstrip()
    team = str(team.encode('utf-8'))

    pts = tds[2].text
    pts = pts.lstrip()
    pts = pts.rstrip()
    pts = str(pts.encode('utf-8'))

    reb = tds[3].text
    reb = reb.lstrip()
    reb = reb.rstrip()
    reb = str(reb.encode('utf-8'))

    ast = tds[4].text
    ast = ast.lstrip()
    ast = ast.rstrip()
    ast = str(ast.encode('utf-8'))

    stl = tds[5].text
    stl = stl.lstrip()
    stl = stl.rstrip()
    stl = str(stl.encode('utf-8'))

    blk = tds[6].text
    blk = blk.lstrip()
    blk = blk.rstrip()
    blk = str(blk.encode('utf-8'))

    eFG = tds[7].text
    eFG = eFG.lstrip()
    eFG = eFG.rstrip()
    eFG = str(eFG.encode('utf-8'))

    ts = tds[8].text
    ts = ts.lstrip()
    ts = ts.rstrip()
    ts = str(ts.encode('utf-8'))

    usg = tds[9].text
    usg = usg.lstrip()
    usg = usg.rstrip()
    usg = str(usg.encode('utf-8'))

    ort = tds[10].text
    ort = ort.lstrip()
    ort = ort.rstrip()
    ort = str(ort.encode('utf-8'))

    drt = tds[11].text
    drt = drt.lstrip()
    drt = drt.rstrip()
    drt = str(drt.encode('utf-8'))

    dre36 = tds[12].text
    dre36 = dre36.lstrip()
    dre36 = dre36.rstrip()
    dre36 = str(dre36.encode('utf-8'))

    per = tds[13].text
    per = per.lstrip()
    per = per.rstrip()
    per = str(per.encode('utf-8'))

    data = (name, team, pts, reb, ast, stl, blk, eFG, ts, usg, ort, drt, dre36, per)
    rotogrindersAdvancedStats.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

rotogrindersAdvancedStats.close()
