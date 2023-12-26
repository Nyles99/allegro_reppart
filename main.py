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

url = "https://wallegro.ru/cat/620-bAvtozapchastib.html"

req = requests.get(url, headers=headers)
src = req.text

soup = BeautifulSoup(src, "lxml")


class Zapchast():

    def __init__(self, name, count, href):
        self.name = name
        self.count = count
        self.href = href



object = soup.find_all("li", style="list-style-type: none; padding: 2px;")
#print(object)
for item in object:
    item = str(item)
    name = item[item.find("translable")+12 : item.find("</span")]
    href = "https://wallegro.ru" + item[item.find("href")+ 6 : item.find("html")+4]
    count = item[item.find('label-default">')+15 : item.find('</span></a></li>')] 
    print(name, href, count)