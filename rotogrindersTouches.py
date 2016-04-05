#scraper for Rotogrinders Touches

from bs4 import BeautifulSoup
import urllib2
import csv

url = "https://rotogrinders.com/pages/nba-advanced-player-stats-guards-touches-201726"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

rotogrindersTouches = open('rotogrindersTouches.csv', 'w')
rotogrindersTouches.write("Player, Team, GP, MIN, TCH/G, TCH/Min, PossTm, Post, Paint, PPG, Pts/Tch, FPPG, FP/Tch" + "\n")


for tr in soup.find_all('tr')[4:]:
    tds = tr.find_all('td')

    name = tds[0].text
    name = name.lstrip()
    name = name.rstrip()
    name = str(name.encode('utf-8'))

    team = tds[1].text
    team = team.lstrip()
    team = team.rstrip()
    team = str(team.encode('utf-8'))

    gamesPlayed = tds[2].text
    gamesPlayed = gamesPlayed.lstrip()
    gamesPlayed = gamesPlayed.rstrip()
    gamesPlayed = str(gamesPlayed.encode('utf-8'))

    minutes = tds[3].text
    minutes = minutes.lstrip()
    minutes = minutes.rstrip()
    minutes = str(minutes.encode('utf-8'))

    touchG = tds[4].text
    touchG = touchG.lstrip()
    touchG = touchG.rstrip()
    touchG = str(touchG.encode('utf-8'))

    touchMin = tds[5].text
    touchMin = touchMin.lstrip()
    touchMin = touchMin.rstrip()
    touchMin = str(touchMin.encode('utf-8'))

    possTm = tds[6].text
    possTm = possTm.lstrip()
    possTm = possTm.rstrip()
    possTm = str(possTm.encode('utf-8'))

    post = tds[7].text
    post = post.lstrip()
    post = post.rstrip()
    post = str(post.encode('utf-8'))

    paint = tds[8].text
    paint = paint.lstrip()
    paint = paint.rstrip()
    paint = str(paint.encode('utf-8'))

    ppg = tds[9].text
    ppg = ppg.lstrip()
    ppg = ppg.rstrip()
    ppg = str(ppg.encode('utf-8'))

    ptsTch = tds[10].text
    ptsTch = ptsTch.lstrip()
    ptsTch = ptsTch.rstrip()
    ptsTch = str(ptsTch.encode('utf-8'))

    fppg = tds[11].text
    fppg = fppg.lstrip()
    fppg = fppg.rstrip()
    fppg = str(fppg.encode('utf-8'))

    fpTch = tds[12].text
    fpTch = fpTch.lstrip()
    fpTch = fpTch.rstrip()
    fpTch = str(fpTch.encode('utf-8'))

    data = (name, team, gamesPlayed, minutes, touchG, touchMin, possTm, post, paint, ppg, ptsTch, fppg, fpTch)
    rotogrindersTouches.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

url = "https://rotogrinders.com/pages/nba-advanced-player-stats-forwards-touches-201728"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

for tr in soup.find_all('tr')[4:]:
    tds = tr.find_all('td')

    name = tds[0].text
    name = name.lstrip()
    name = name.rstrip()
    name = str(name.encode('utf-8'))

    team = tds[1].text
    team = team.lstrip()
    team = team.rstrip()
    team = str(team.encode('utf-8'))

    gamesPlayed = tds[2].text
    gamesPlayed = gamesPlayed.lstrip()
    gamesPlayed = gamesPlayed.rstrip()
    gamesPlayed = str(gamesPlayed.encode('utf-8'))

    minutes = tds[3].text
    minutes = minutes.lstrip()
    minutes = minutes.rstrip()
    minutes = str(minutes.encode('utf-8'))

    touchG = tds[4].text
    touchG = touchG.lstrip()
    touchG = touchG.rstrip()
    touchG = str(touchG.encode('utf-8'))

    touchMin = tds[5].text
    touchMin = touchMin.lstrip()
    touchMin = touchMin.rstrip()
    touchMin = str(touchMin.encode('utf-8'))

    possTm = tds[6].text
    possTm = possTm.lstrip()
    possTm = possTm.rstrip()
    possTm = str(possTm.encode('utf-8'))

    post = tds[7].text
    post = post.lstrip()
    post = post.rstrip()
    post = str(post.encode('utf-8'))

    paint = tds[8].text
    paint = paint.lstrip()
    paint = paint.rstrip()
    paint = str(paint.encode('utf-8'))

    ppg = tds[9].text
    ppg = ppg.lstrip()
    ppg = ppg.rstrip()
    ppg = str(ppg.encode('utf-8'))

    ptsTch = tds[10].text
    ptsTch = ptsTch.lstrip()
    ptsTch = ptsTch.rstrip()
    ptsTch = str(ptsTch.encode('utf-8'))

    fppg = tds[11].text
    fppg = fppg.lstrip()
    fppg = fppg.rstrip()
    fppg = str(fppg.encode('utf-8'))

    fpTch = tds[12].text
    fpTch = fpTch.lstrip()
    fpTch = fpTch.rstrip()
    fpTch = str(fpTch.encode('utf-8'))

    data = (name, team, gamesPlayed, minutes, touchG, touchMin, possTm, post, paint, ppg, ptsTch, fppg, fpTch)
    rotogrindersTouches.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

url = "https://rotogrinders.com/pages/nba-advanced-player-stats-centers-touches-201727"

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

for tr in soup.find_all('tr')[4:]:
    tds = tr.find_all('td')

    name = tds[0].text
    name = name.lstrip()
    name = name.rstrip()
    name = str(name.encode('utf-8'))

    team = tds[1].text
    team = team.lstrip()
    team = team.rstrip()
    team = str(team.encode('utf-8'))

    gamesPlayed = tds[2].text
    gamesPlayed = gamesPlayed.lstrip()
    gamesPlayed = gamesPlayed.rstrip()
    gamesPlayed = str(gamesPlayed.encode('utf-8'))

    minutes = tds[3].text
    minutes = minutes.lstrip()
    minutes = minutes.rstrip()
    minutes = str(minutes.encode('utf-8'))

    touchG = tds[4].text
    touchG = touchG.lstrip()
    touchG = touchG.rstrip()
    touchG = str(touchG.encode('utf-8'))

    touchMin = tds[5].text
    touchMin = touchMin.lstrip()
    touchMin = touchMin.rstrip()
    touchMin = str(touchMin.encode('utf-8'))

    possTm = tds[6].text
    possTm = possTm.lstrip()
    possTm = possTm.rstrip()
    possTm = str(possTm.encode('utf-8'))

    post = tds[7].text
    post = post.lstrip()
    post = post.rstrip()
    post = str(post.encode('utf-8'))

    paint = tds[8].text
    paint = paint.lstrip()
    paint = paint.rstrip()
    paint = str(paint.encode('utf-8'))

    ppg = tds[9].text
    ppg = ppg.lstrip()
    ppg = ppg.rstrip()
    ppg = str(ppg.encode('utf-8'))

    ptsTch = tds[10].text
    ptsTch = ptsTch.lstrip()
    ptsTch = ptsTch.rstrip()
    ptsTch = str(ptsTch.encode('utf-8'))

    fppg = tds[11].text
    fppg = fppg.lstrip()
    fppg = fppg.rstrip()
    fppg = str(fppg.encode('utf-8'))

    fpTch = tds[12].text
    fpTch = fpTch.lstrip()
    fpTch = fpTch.rstrip()
    fpTch = str(fpTch.encode('utf-8'))

    data = (name, team, gamesPlayed, minutes, touchG, touchMin, possTm, post, paint, ppg, ptsTch, fppg, fpTch)
    rotogrindersTouches.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

rotogrindersTouches.close()
