import json
from turtle import pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
import os
import shutil
import csv
from PIL import Image, UnidentifiedImageError
import time

headers = {
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

"""url = "https://wallegro.ru/cat/620-bAvtozapchastib.html"
#Первое погружение
req = requests.get(url, headers=headers)
src = req.text

soup = BeautifulSoup(src, "lxml")
repeat_href = []
json_href_str = {}
first_href = soup.find_all("a", class_="list-group-item")
#print (price_obj)
n = 1

for item_one_href in first_href:
    href_one = "https://wallegro.ru" + item_one_href.get("href")
    #print(href_one)
    #Второе погружение
    req = requests.get(href_one, headers=headers)
    src = req.text
#<span class="label label-default">162487</span>
    soup = BeautifulSoup(src, "lxml")
    second_href = soup.find_all("a", class_="list-group-item")
    #print(second_href)
        
    for item_href in second_href:
        #print(item_price.text)
        
        href_two = "https://wallegro.ru" + item_href.get("href")
        all_text = item_href.text
        print(href_two, all_text)
        
        #print(href_two)
        if href_two not in repeat_href:
            repeat_href.append(href_two)
            json_href_str[all_text] = href_two
            n += 1
            print(href_two)

with open("json_href_str.json", "a", encoding="utf-8") as file:
    json.dump(json_href_str, file, indent=4, ensure_ascii=False)"""

with open('json_href_str.json', encoding="utf-8") as file:
    all = json.load(file)

for all_text, href_str in all.items():
    quantity = ''
    for char in all_text:
        if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
            quantity = quantity + char
    page = int(quantity)/30 + 2
    for i in range(1, int(page)):
        href_page = f"{href_str}?id-page={i}&id-per-page=30"
        req = requests.get(url=href_page, headers=headers)
        src = req.text

        soup = BeautifulSoup(src, "lxml")
        cards_obj = soup.find_all("a", class_="b-item-link")
        
        for item_card in cards_obj:
            href_card = "https://wallegro.ru" + item_card.get("href")
            print(href_card)
            req = requests.get(url=href_card, headers=headers)
            src = req.text

            soup = BeautifulSoup(src, "lxml")
            art_obj = soup.find_all("div", class_="timeline")
            for item_art in art_obj.items():
                
            break
        break
    break
