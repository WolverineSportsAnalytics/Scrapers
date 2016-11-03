#scraper for RotoWire DFS Stats

from bs4 import BeautifulSoup
import urllib2
import csv

def fantasypros_qb_scraper():
    url = "https://www.fantasypros.com/nfl/projections/qb.php"
    csv_filename = 'fantasypros_qb_table.csv'
    stats = ["Name", "Team", "Passing Attempts", "Passing Completions", "Passing Yards", "Passing Touchdowns", "Passing Interceptions", "Rushing Attempts", "Rushing Yards", "Rushing Touchdowns", "FL", "FPTS"]
    fantasypros_scraper(url, csv_filename, stats)
    
def fantasypros_rb_scraper():
    url = "https://www.fantasypros.com/nfl/projections/rb.php"
    csv_filename = 'fantasypros_rb_table.csv'
    stats = ["Name", "Team", "Rushing Attempts", "Rushing Yards", "Rushing Touchdowns", "Receiving Receptions", "Receiving Yards", "Receiving Touchdowns", "FL", "FPTS"]
    fantasypros_scraper(url, csv_filename, stats)

def fantasypros_wr_scraper():
    url = "https://www.fantasypros.com/nfl/projections/wr.php"
    csv_filename = 'fantasypros_wr_table.csv'
    stats = ["Name", "Team", "Rushing Attempts", "Rushing Yards", "Rushing Touchdowns", "Receptions", "Recieving Yards", "Recieving Touchdowns", "FL", "FPTS"]
    fantasypros_scraper(url, csv_filename, stats)
    
def fantasypros_te_scraper():
    url = "https://www.fantasypros.com/nfl/projections/te.php"
    csv_filename = 'fantasypros_te_table.csv'
    stats = ["Name", "Team", "Receptions", "Yards", "Touchdowns", "FL", "FPTS"]
    fantasypros_scraper(url, csv_filename, stats)
    
def fantasypros_k_scraper():
    url = "https://www.fantasypros.com/nfl/projections/k.php"
    csv_filename = 'fantasypros_k_table.csv'
    stats = ["Name", "Team", "Field Goals", "Field Goal Attemps", "Extra Points", "FPTS"]
    fantasypros_scraper(url, csv_filename, stats)
    
def fantasypros_dst_scraper():
    url = "https://www.fantasypros.com/nfl/projections/dst.php"
    csv_filename = 'fantasypros_dst_table.csv'
    stats = ["Name", "Sack", "Interceptions", "Fumble Recoveries", "Forced Fumbles", "TD", "Assist", "Safety", "Points Allowed", "Yards Allowed", "FPTS"]
    fantasypros_scraper(url, csv_filename, stats)
    
def fantasypros_scraper(url, csv_filename, stats):
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, "html.parser")

    file = open(csv_filename, 'w')
    for stat in stats:
        file.write(stat + ", ")
    file.write("\n")

    qb_table = soup.find_all('tbody')[0] 

    for tr in qb_table.find_all('tr')[0:]:
        tds = tr.find_all('td')
        
        if tds[0].a.text != (tds[0].text).strip():
            name = tds[0].a.text
            team = tds[0].text.split()[2]
            file.write(name + ',')
            file.write(team + ',')
        else:
            name = tds[0].a.text
            file.write(name + ',')
        
        for td in range(1, len(tds)):
            file.write(tds[td].text + ',')
        file.write('\n')

    file.close()
    
if __name__ == "__main__":
    fantasypros_qb_scraper()
    fantasypros_rb_scraper()
    fantasypros_wr_scraper()
    fantasypros_te_scraper()
    fantasypros_k_scraper()
    fantasypros_dst_scraper()