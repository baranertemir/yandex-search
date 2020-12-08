#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 23:05:01 2020

@author: A.Baran Ertemir & Eren Şimşek <Aporlorxl23>
"""
import string
import requests
from bs4 import BeautifulSoup

keyword = input("Search in Yandex:")
main_Url = "https://yandex.com.tr/search/?lr=101657&text="+keyword
depth=5
alldata = []
for page in range(0,depth):
    search = main_Url+"&p="+str(page)
    response = requests.get(search)
    html = response.content
    soup = BeautifulSoup(html,"html.parser")

    for i in soup.find("div",{"class":"content__left"}).find_all("a"):
        if i.get("href")[:2] != "//" and i.get("href")[:1] != "/":
            if i.get("href") not in alldata:
                alldata.append(i.get("href"))

for i in alldata:
    print(i)
