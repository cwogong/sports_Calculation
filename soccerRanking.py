import requests
from bs4 import BeautifulSoup

html = requests.get("https://sports.news.naver.com/wfootball/index.nhn")
soup = BeautifulSoup(html.content,"html.parser")
 
team_rank_list = soup.select('#_team_rank_epl > table > tbody > tr')

rank = []
team = []
games = []
wins = []
draws = []
loses = []
points = []

for o in team_rank_list :
    rank.append(o.select("span")[1].text)
    team.append(o.select("span")[2].text)
    games.append(o.select("span")[3].text)
    wins.append(o.select("span")[4].text)
    draws.append(o.select("span")[5].text)
    loses.append(o.select("span")[6].text)
    points.append(o.select("span")[7].text)

