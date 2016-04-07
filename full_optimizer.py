from bs4 import BeautifulSoup
import urllib2
import csv
import demjson

def center():
	url = "http://www.rotowire.com/daily/nba/defense-vspos.htm?statview=last10&pos=C"

	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page, "html.parser")

	rotowireFanduelDvPLast10C = open('rotowireFanduelDvPLast10C.csv', 'w')
	rotowireFanduelDvPLast10C.write("Team, Vs. Pos, Season, Last 5, Last 10, PTS, REB, AST, STL, BLK, 3PM, FG%, FT%, TO" + "\n")

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
	    rotowireFanduelDvPLast10C.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

	rotowireFanduelDvPLast10C.close()


	reader = csv.reader(open("rotowireFanduelDvPLast10C.csv"))

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
	return html

def power_forward():
	url = "http://www.rotowire.com/daily/nba/defense-vspos.htm?statview=last10&pos=PF"


	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page, "html.parser")

	rotowireFanduelDvPLast10PF = open('rotowireFanduelDvPLast10PF.csv', 'w')
	rotowireFanduelDvPLast10PF.write("Team, Vs. Pos, Season, Last 5, Last 10, PTS, REB, AST, STL, BLK, 3PM, FG%, FT%, TO" + "\n")

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
	    rotowireFanduelDvPLast10PF.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

	rotowireFanduelDvPLast10PF.close()

	reader = csv.reader(open("rotowireFanduelDvPLast10PF.csv"))

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
	return html

def point_guard():
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
	return html

def small_forward():
	url = "http://www.rotowire.com/daily/nba/defense-vspos.htm?statview=last10&pos=SF"


	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page, "html.parser")

	rotowireFanduelDvPLast10SF = open('rotowireFanduelDvPLast10SF.csv', 'w')
	rotowireFanduelDvPLast10SF.write("Team, Vs. Pos, Season, Last 5, Last 10, PTS, REB, AST, STL, BLK, 3PM, FG%, FT%, TO" + "\n")

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
	    rotowireFanduelDvPLast10SF.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

	rotowireFanduelDvPLast10SF.close()

	reader = csv.reader(open("rotowireFanduelDvPLast10SF.csv"))

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
	return html

def shooting_guard():
	url = "http://www.rotowire.com/daily/nba/defense-vspos.htm?statview=last10&pos=SG"


	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page, "html.parser")

	rotowireFanduelDvPLast10SG = open('rotowireFanduelDvPLast10SG.csv', 'w')
	rotowireFanduelDvPLast10SG.write("Team, Vs. Pos, Season, Last 5, Last 10, PTS, REB, AST, STL, BLK, 3PM, FG%, FT%, TO" + "\n")

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
	    rotowireFanduelDvPLast10SG.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

	rotowireFanduelDvPLast10SG.close()

	reader = csv.reader(open("rotowireFanduelDvPLast10SG.csv"))

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
	return html

def main():
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

	    team = (tds[2].text).replace('@', '')
	    team = str(team.encode('ascii'))

	    opponent = (tds[3].text).replace('@', '')
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
	    if projpts == '':
	        projpts = tds[9]['data-points']

	    value = tds[10].text
	    value = str(value.encode('ascii'))


	    data = (name, team, opponent, position, moneyline, overunder, projmin, salary, projpts, value)
	    rotowire.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

	rotowire.close()

	reader = csv.reader(open("rotowire.csv"))

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
	return html

def last_week():
	url = "https://rotogrinders.com/game-stats/nba-player?site=fanduel&range=1week"

	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page, "html.parser")

	rotogrinder_lastweek = open('rotogrinder_lastweek.csv', 'w')
	rotogrinder_lastweek.write("Player, Team, Pos, Salary, GP, MIN, REB, AST, STL, BLK, TO, PTS, USG, FPTS" + "\n")

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
	        rotogrinder_lastweek.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s \n' % data)

	rotogrinder_lastweek.close()

	reader = csv.reader(open("rotogrinder_lastweek.csv"))

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
	return html

def misc():
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
	        rotogrinder_misc.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s \n' % data)

	rotogrinder_misc.close()

	reader = csv.reader(open("rotogrinder_misc.csv"))

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
	return html

def consistency():
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
	return html

def advanced_stats():
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

	reader = csv.reader(open("rotogrindersAdvancedStats.csv"))

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
	return html

def touches():
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

	reader = csv.reader(open("rotogrindersTouches.csv"))

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
	return html

def pace():
	def team_name_to_abbreviation(name):
	    return {
	        "Atlanta": "ATL",
	        "Brooklyn": "BKN",
	        "Boston": "BOS",
	        "Charlotte": "CHA",
	        "Chicago": "CHI",
	        "Cleveland": "CLE",
	        "Dallas": "DAL",
	        "Denver": "DEN",
	        "Detroit": "DET",
	        "Golden State": "GS",
	        "Houston": "HOU",
	        "Indiana": "IND",
	        "L.A. Clippers": "LAC",
	        "L.A. Lakers": "LAL",
	        "Memphis": "MEM",
	        "Miami": "MIA",
	        "Milwaukee": "MIL",
	        "Minnesota": "MIN",
	        "New Orleans": "NOP",
	        "New York": "NYK",
	        "Oklahoma City": "OKC",
	        "Orlando": "ORL",
	        "Philadelphia": "PHI",
	        "Phoenix": "PHX",
	        "Portland": "POR",
	        "Sacramento": "SAC",
	        "San Antonio": "SA",
	        "Toronto": "TOR",
	        "Utah": "UTA",
	        "Washington": "WSH"
	    }.get(name, name)

	url = "https://rotogrinders.com/pages/nba-offense-vs-defense-pace-and-scoring-174522"

	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page, "html.parser")

	rotogrinder_pace = open('rotogrinder_pace.csv', 'w')
	rotogrinder_pace.write("Team, Opponent, Pace, PPG, OffRtg, Pace, PPG-A, DefRtg, Pace, Pts, AvgRtg" + "\n")

	for tr in soup.find_all('tr')[5:]:
	    tds = tr.find_all('td')
	    data = (tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text, tds[7].text, tds[8].text, tds[9].text, tds[10].text)
	    
	    team = tds[0].text
	    team = team.lstrip()
	    team = team.rstrip()
	    team = str(team.encode('utf-8'))
	    team = team_name_to_abbreviation(team)

	    opponent = tds[1].text
	    opponent = opponent.lstrip()
	    opponent = opponent.rstrip()
	    opponent = str(opponent.encode('utf-8'))
	    opponent = team_name_to_abbreviation(opponent)

	    pace1 = tds[2].text
	    pace1 = str(pace1.encode('ascii'))

	    ppg = tds[3].text
	    ppg = str(ppg.encode('ascii')) 

	    offRtg = tds[4].text
	    offRtg = str(offRtg.encode('ascii'))

	    pace2 = tds[5].text
	    pace2 = str(pace2.encode('ascii'))

	    ppgA = tds[6].text
	    ppgA = str(ppgA.encode('ascii'))

	    defRtg = tds[7].text
	    defRtg = str(defRtg.encode('ascii'))

	    pace3 = tds[8].text
	    pace3 = str(pace3.encode('ascii'))

	    pts = tds[9].text
	    pts = str(pts.encode('ascii'))

	    avgRtg = tds[10].text
	    avgRtg = str(avgRtg.encode('ascii'))

	    data = (team, opponent, pace1, ppg, offRtg, pace2, ppgA, defRtg, pace3, pts, avgRtg)
	    rotogrinder_pace.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n' % data)

	rotogrinder_pace.close()

	reader = csv.reader(open("rotogrinder_pace.csv"))

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
	return html
