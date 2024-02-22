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

year_list = []
file1 = open("year.txt", "r")
while True:
    # считываем строку
    line = file1.readline()
    line = line.replace("\n","").replace("'","").replace(" ","")
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    year_list.append(line)
#print(black_list)
# закрываем файл
file1.close


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
    #print(href_str)
    if "Решетки радиатора" in all_text:
        name_part = "Решетка радиатора"

    if os.path.exists(f"allegro_{name_part}_{time.strftime('%Y-%m-%d')}.csv"):
        print("файл с таким именем уже есть")
    else:
        with open(f"allegro_{name_part}_{time.strftime('%Y-%m-%d')}.csv", "w", encoding="utf-8") as file_data:
            writer = csv.writer(file_data)

            writer.writerow(
                (
                    "АРТИКУЛ",
                    "МАРКА",
                    "МОДЕЛЬ",
                    "ГОД",
                    "НОМЕР ЗАПЧАСТИ",
                    "ССЫЛКА НА ЗАПЧАСТЬ",
                    "ТОПЛИВО",
                    "ОБЪЕМ",
                    "ТИП ДВИГАТЕЛЯ",
                    "КОРОБКА",
                    "ТИП КУЗОВА",
                    "ЗАПЧАСТЬ",
                    "ОПИСАНИЕ",
                    "ПОД ЗАКАЗ",
                    "ЦЕНА",
                    "НОВАЯ",
                    "ФОТО",
                    "ФИРМА ПРОИЗВОДИТЕЛЬ",
                    "ОРИГИНАЛ",
                    "ВЕРСИЯ СБОРКИ",
                    "ВЕС ДЛЯ ОТГРУЗКИ",
                    "СТРАНИЦА ОКОНЧАНИЯ",
                )
            )



    
    quantity = ''
    for char in all_text:
        if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
            quantity = quantity + char
    page = int(int(quantity)/30 + 2)
    #print(page)
    for i in range(1, int(page)):
        href_page = f"{href_str}?id-page={i}&id-per-page=30"
        print(href_page)
        req = requests.get(url=href_page, headers=headers)
        src = req.text
        
        soup = BeautifulSoup(src, "lxml")
        #print(soup)
        cards_obj = soup.find_all("a", class_="b-item-link")
        #print(cards_obj)
        for item_card in cards_obj:
            href_card = "https://wallegro.ru" + item_card.get("href")
            #print(href_card)
            req = requests.get(url=href_card, headers=headers)
            src = req.text
            
            soup = BeautifulSoup(src, "lxml")
            art_obj = soup.find_all("div", class_="timeline")
            #print(art_obj)
            artical = ""
            for item_art in art_obj:
                #print(item_art.text)
                for char in item_art.text:
                    #print(char)
                    if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
                        artical = artical + char
            print(artical)
            status = "Б.у."
            num_zap = " "
            firma = " "
            version = " "
            original = " "
            all_info_obj = (soup.find_all("p"))
            #print(all_info_obj)
            for item in all_info_obj:
                #print(item, "туда")
                item = str(item)
                if "Состояние" or "состояние" in item: 
                    if "Новый" in item:
                        status = "Новый"
                if "Номер детали" in item:
                    num_zap = item[item.find('<b class="translable">')+22 : item.find('</b></small>')]
                if "Производитель части" in item:
                    firma = item[item.find('<b class="translable">')+22 : item.find('</b></small>')]
                if '"translable">Версия</span>' in item:
                    version = item[item.find('<b class="translable">')+22 : item.find('</b></small>')]
                if '"translable">Качество деталей' in item:
                    original = item[item.find('<b class="translable">')+22 : item.find('</b></small>')]
                if '"translable">Вес с индивидуальной упаковкой' in item:
                    weight = item[item.find('<b class="translable">')+22 : item.find('</b></small>')]
                
            print(status)
            print(num_zap)
            print(firma)
            print(version)
            print(original)
            print(name_part)
            print(weight)
            print(href_card)
            
            
            img_obj = soup.find_all("div", class_="container", style="padding: 0px 0 0 0")
            #print(img_obj)
            for item in img_obj:
                #print(item, "Новая строка")
                href_foto = str(item)
                #print(href_foto)
                href_foto = href_foto[href_foto.find('"image": [')+12 : href_foto.find('],')- 2].replace("/n","").replace("\r","").replace(" ","")
                href_foto =  href_foto[href_foto.find('"')+1 : href_foto.find('" ')-1]
            print(href_foto)
            price_obj = soup.find_all("span", itemprop="price")
            #print(price_obj)
            for item in price_obj:
                price = item.text
            print(price)

            marka_and_model_obj = (soup.find_all("h1", itemprop="name", class_="translable"))
            #print(marka_and_model_obj)
            for item_mm in marka_and_model_obj:
                info = item_mm.text.lower()
                spisok_marka_model = info.split()
            print(info)
            year = " "
            year_obj = soup.find_all("div", class_="translable")
            #print(year_obj)
            for item_year in year_obj:
                item_year = item_year.text
                for word_year in year_list:
                
                    if word_year in item_year:
                    #print(word_year)
                        year = word_year
            
                
            
            with open('modelu_new.json', encoding="utf-8") as file:
                model_need_list = json.load(file)
            
            for model, marka in model_need_list.items():
                if str(marka).lower() in info:
                    marka = marka
                    break
            string_model = " "
            
            for model, marka_1 in model_need_list.items():
                for word in spisok_marka_model:
                    if len(word) > 1:
                        if word.lower() in model:
                            if word.lower() not in string_model:
                                string_model = str(string_model) + " "+ str(word)
            print(year)       
            print(string_model)
            print(marka)
            fuel = ""
            engine = ""
            transmission = ""
            car_body = ""
            volume = ""
            order = ""
            nomer_str = 1

            file = open(f"allegro_{name_part}_{time.strftime('%Y-%m-%d')}.csv", "a", encoding="utf-8", newline='')
            writer = csv.writer(file)

            writer.writerow(
                (
                    artical,
                    marka,
                    string_model,
                    year,
                    num_zap,
                    href_card,
                    fuel,
                    volume,
                    engine,
                    transmission,
                    car_body,
                    name_part,
                    info,
                    order,
                    price,
                    status,
                    href_foto,
                    firma,
                    original,
                    version,
                    weight,
                    nomer_str
                )
            )
            file.close()
            
        break
    break
