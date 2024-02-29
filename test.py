import html
import json
from turtle import pd
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

href_page = "https://wallegro.ru/item/14513216880/MAHLE-ORIGINAL-CLC--s-maslyanyj-radiator-motornoe-maslo.html"
req = requests.get(url=href_page, headers=headers)
src = req.text
        
soup = BeautifulSoup(src, "lxml")

name_part_obj = soup.find_all("h1", itemprop="name",  class_="translable")

print(name_part_obj.text)
for item_name in name_part_obj:
    print(item_name.text)