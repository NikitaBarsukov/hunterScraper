from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json

html = urlopen("https://spb.hh.ru/search/vacancy?text=Java&area=2").read()

f = open("page.html", "w", encoding="utf-8")
res = open("result.txt", "w", encoding="utf-8")

f.write(str(html.decode("UTF-8")))

soup = BeautifulSoup(html, "html.parser")

set = soup.findAll("script", {"data-name": "HH/VacancyResponsePopup/VacancyResponsePopup"})



for i in range(0,len(set)):
    data = set[i]["data-params"]
    print(json.loads(data)["vacancyId"])

print(len(set))