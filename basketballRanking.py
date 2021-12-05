import requests
from bs4 import BeautifulSoup

html = requests.get("https://sports.news.naver.com/basketball/record/index?category=kbl&year=2022")
soup = BeautifulSoup(html.content,"html.parser")
 
team_rank_list = soup.select('#regularTeamRecordList_table > tr')

rank = []
team = []
games = []
wins = []
loses = []
rate = []

for o in team_rank_list :
    rank.append(o.select("strong")[0].text)
    team.append(o.select("span")[0].text)
    games.append(o.select("span")[1].text)
    wins.append(o.select("span")[2].text)
    loses.append(o.select("span")[3].text)
    rate.append(o.select("strong")[1].text)