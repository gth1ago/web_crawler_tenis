from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import json

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
}

while(True):
    try:
        name = input('Nome: ')
        name = name.replace(' ', '')

        # https://www.atptour.com/en/players/
        # GET -> https://www.atptour.com/en/-/ajax/PredictiveContentSearch/GetPlayerResults/tommy%20pau

        siteSearch = "https://www.atptour.com/en/-/ajax/PredictiveContentSearch/GetPlayerResults/" + name

        search = urllib.request.Request(siteSearch, None, header)

        page = urlopen(search)

        html = BeautifulSoup(page.read(), "html.parser")
        string = html.text

        text_json = json.loads(string)

        text = text_json['items']
        infos = text[0]

        hosp = infos['Url']
        host = "https://www.atptour.com"
        url = host + hosp

        req = urllib.request.Request(url, None, header)

        page = urlopen(req)
        html = BeautifulSoup(page.read(), "html.parser")

        contentName = (html.find("div", {"class": "first-name"})).text
        contentLastName = (html.find("div", {"class": "last-name"})).text
        contentRanking = (html.find("div", {"class": "data-number"})).text
        contentYear = (html.find("span", {"class": "table-birthday"})).text
        contentHeight = (
            html.find("span", {"class": "table-height-cm-wrapper"})).text
        contentWeight = (
            html.find("span", {"class": "table-weight-kg-wrapper"})).text

        print(contentName, contentLastName)
        print("Ranking: ", contentRanking[2:-24])
        print("Nasc: ", contentYear[51:-47])
        print("Altura: ", contentHeight[1:-1])
        print("Peso: ", contentWeight[1:-1])
        print("\n-----------")
    except:
        print("Nao encontraod")
        exit()

"""
RANKING
<div class="data-number" style="margin-left: 10px"> 52 </div>

IDADE
<div class="table-big-value"> 23 <span class="table-birthday-wrapper">
    <span class="table-birthday"> (1997.05.17)
                                      
"""
