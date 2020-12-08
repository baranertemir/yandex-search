#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 23:05:01 2020

@author: A.Baran Ertemir
"""
import string
import requests
from bs4 import BeautifulSoup

keyword = input("Search in Yandex:")
search = "https://yandex.com.tr/search/?lr=101657&text="
paramater = "&p=1"
paramater2 = "&p=2"
paramater3 = "&p=3"
paramater4 = "&p=4"
paramater5 = "&p=5"
paramater6 = "&p=6"
paramater7 = "&p=7"
paramater8 = "&p=8"
paramater9 = "&p=9"
paramater10 = "&p=10"

add = search + keyword
add1 = search + keyword + paramater
add2 = search + keyword + paramater2
add3 = search + keyword + paramater3
add4 = search + keyword + paramater4
add5 = search + keyword + paramater5
add6 = search + keyword + paramater6
add7 = search + keyword + paramater7
add8 = search + keyword + paramater8
add9 = search + keyword + paramater9
add10 = search + keyword + paramater10



response = requests.get(add)
html = response.content
soup = BeautifulSoup(html,"html.parser")

for i in soup.find("div",{"class":"content__left"}).find_all("a"):
    if i.get("href")[:2] != "//" and i.get("href")[:1] != "/":
        print(i.get("href"))
    

response1 = requests.get(add1)
html1 = response1.content
soup1 = BeautifulSoup(html1,"html.parser")

for i in soup1.find("div",{"class":"content__left"}).find_all("a"):
    if i.get("href")[:2] != "//" and i.get("href")[:1] != "/":
        print(i.get("href"))


response2 = requests.get(add2)
html2 = response2.content
soup2 = BeautifulSoup(html2,"html.parser")

for i in soup2.find("div",{"class":"content__left"}).find_all("a"):
    if i.get("href")[:2] != "//" and i.get("href")[:1] != "/":
        print(i.get("href"))



response3 = requests.get(add3)
html3 = response3.content
soup3 = BeautifulSoup(html3,"html.parser")

for i in soup3.find("div",{"class":"content__left"}).find_all("a"):
    if i.get("href")[:2] != "//" and i.get("href")[:1] != "/":
        print(i.get("href"))



response4 = requests.get(add4)
html4 = response4.content
soup4 = BeautifulSoup(html4,"html.parser")

for i in soup4.find("div",{"class":"content__left"}).find_all("a"):
    if i.get("href")[:2] != "//" and i.get("href")[:1] != "/":
        print(i.get("href"))

response5 = requests.get(add5)
html5 = response5.content
soup5 = BeautifulSoup(html5,"html.parser")

for i in soup5.find("div",{"class":"content__left"}).find_all("a"):
    if i.get("href")[:2] != "//" and i.get("href")[:1] != "/":
        print(i.get("href"))


response6 = requests.get(add6)
html6 = response6.content
soup6 = BeautifulSoup(html6,"html.parser")

for i in soup6.find("div",{"class":"content__left"}).find_all("a"):
    if i.get("href")[:2] != "//" and i.get("href")[:1] != "/":
        print(i.get("href"))

response7 = requests.get(add7)
html7 = response7.content
soup7 = BeautifulSoup(html7,"html.parser")

for i in soup7.find("div",{"class":"content__left"}).find_all("a"):
    if i.get("href")[:2] != "//" and i.get("href")[:1] != "/":
        print(i.get("href"))

response8 = requests.get(add8)
html8 = response8.content
soup8 = BeautifulSoup(html8,"html.parser")

for i in soup8.find("div",{"class":"content__left"}).find_all("a"):
    if i.get("href")[:2] != "//" and i.get("href")[:1] != "/":
        print(i.get("href"))

response9 = requests.get(add9)
html9 = response9.content
soup9 = BeautifulSoup(html9,"html.parser")

for i in soup9.find("div",{"class":"content__left"}).find_all("a"):
    if i.get("href")[:2] != "//" and i.get("href")[:1] != "/":
        print(i.get("href"))

response10 = requests.get(add10)
html10 = response10.content
soup10 = BeautifulSoup(html10,"html.parser")

for i in soup10.find("div",{"class":"content__left"}).find_all("a"):
    if i.get("href")[:2] != "//" and i.get("href")[:1] != "/":
        print(i.get("href"))