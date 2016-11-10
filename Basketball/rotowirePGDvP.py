#scraper for RotoWire Last 10 FanDuel PG Defense vs. Position DFS Stats

from bs4 import BeautifulSoup
import urllib2
import csv

url = "http://www.rotowire.com/daily/nba/defense-vspos.htm?statview=last10"


page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

rotowireFanduelDvPLast10PG = open('rotowireFanduelDvPLast10PG.csv', 'w')
rotowireFanduelDvPLast10PG.write("Team, Vs. Pos, Season, Last 5, Last 10, PTS, REB, AST, STL, BLK, 3PM, FG%, FT%, TO" + "\n")

for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')

    name = tds[0].text
    if name in ['Philadelphia 76ers']:
        name = 'PHI'
    if name in ['Minnesota Timberwolves']:
        name = 'MIN'
    if name in ['Washington Wizards']:
        name = 'WAS'
    if name in ['Cleveland Cavaliers']:
        name = 'CLE'
    if name in ['New Orleans Pelicans']:
        name = 'NOP'
    if name in ['Houston Rockets']:
        name = 'HOU'
    if name in ['Portland Trail Blazers']:
        name = 'POR'
    if name in ['Denver Nuggets']:
        name = 'DEN'
    if name in ['Detroit Pistons']:
        name = 'DET'
    if name in ['Dallas Mavericks']:
        name = 'DAL'
    if name in ['Los Angeles Lakers']:
        name = 'LAL'
    if name in ['Los Angeles Clippers']:
        name = 'LAC'
    if name in ['Miami Heat']:
        name = 'MIA'
    if name in ['San Antonio Spurs']:
        name = 'SAS'
    if name in ['Atlanta Hawks']:
        name = 'ATL'
    if name in ['Brooklyn Nets']:
        name = 'BKN'
    if name in ['Phoenix Suns']:
        name = 'PHO'
    if name in ['New York Knicks']:
        name = 'NYK'
    if name in ['Golden State Warriors']:
        name = 'GSW'
    if name in ['Memphis Grizzlies']:
        name = 'MEM'
    if name in ['Sacramento Kings']:
        name = 'SAC'
    if name in ['Boston Celtics']:
        name = 'BOS'
    if name in ['Milwaukee Bucks']:
        name = 'MIL'
    if name in ['Charlotte Hornets']:
        name = 'CHA'
    if name in ['Toronto Raptors']:
        name = 'TOR'
    if name in ['Indiana Pacers']:
        name = 'IND'
    if name in ['Orlando Magic']:
        name = 'ORL'
    if name in ['Utah Jazz']:
        name = 'UTA'
    if name in ['Chicago Bulls']:
        name = 'CHI'
    if name in ['Oklahoma City Thunder']:
        name = 'OKC'
    name = str(name.encode('ascii'))

    vsPos = tds[1].text
    vsPos = str(vsPos.encode('ascii'))

    season = tds[2].text
    season = str(season.encode('ascii'))

    last5 = tds[3].text
    last5 = str(last5.encode('utf-8'))

    last10 = tds[4].text
    last10 = str(last10.encode('utf-8'))

    pts = tds[5].text
    pts = str(pts.encode('utf-8'))

    reb = tds[6].text
    reb = str(reb.encode('utf-8'))

    ast = tds[7].text
    ast = str(ast.encode('utf-8'))

    stl = tds[8].text
    stl = str(stl.encode('utf-8'))

    blk = tds[9].text
    blk = str(blk.encode('utf-8'))

    threePM = tds[10].text
    threePM = str(threePM.encode('utf-8'))

    fgPercent = tds[11].text
    fgPercent = str(fgPercent.encode('utf-8'))

    ftPercent = tds[12].text
    ftPercent = str(ftPercent.encode('utf-8'))

    turnOver = tds[13].text
    turnOver = str(turnOver.encode('utf-8'))

    data = (name, vsPos, season, last5, last10, pts, reb, ast, stl, blk, threePM, fgPercent, ftPercent, turnOver)
    rotowireFanduelDvPLast10PG.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

rotowireFanduelDvPLast10PG.close()

reader = csv.reader(open("rotowireFanduelDvPLast10PG.csv"))

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
