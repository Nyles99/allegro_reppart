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

def osnova(name_part_osn, all_text, href_str):

    if os.path.exists(f"allegro_{all_text}_{time.strftime('%Y-%m-%d')}.csv"):
        print("файл с таким именем уже есть")
    else:
        with open(f"allegro_{all_text}_{time.strftime('%Y-%m-%d')}.csv", "w", encoding="utf-8") as file_data:
            writer = csv.writer(file_data)

            writer.writerow(
                (
                    "АРТИКУЛ",
                    "НОМЕР ДЕТАЛИ",
                    "НОМЕР ДЕТАЛИ ОСТАЛЬНЫЕ",
                    "МАРКА",
                    "МОДЕЛЬ",
                    "ГОД",
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
    
    href_card_list = []
    count = 1
    for i in range(1, int(page)):
        href_page = f"{href_str}?id-page={i}&id-per-page=30"
        print(href_page)
        req = requests.get(url=href_page, headers=headers)
        src = req.text
        
        soup = BeautifulSoup(src, "lxml")

        name_part_obj = soup.find_all("span", class_="b-game-link-header translable")
        #print(soup)
        cards_obj = soup.find_all("a", class_="b-item-link")
        #print(cards_obj)
        
        for item_card in cards_obj:
            
            href_card = "https://wallegro.ru" + item_card.get("href")
            #print(href_card)
            if href_card not in href_card_list:
                name_part = name_part_osn
                href_card_list.append(href_card)
                print(href_card)
                req = requests.get(url=href_card, headers=headers)
                src = req.text
                soup = BeautifulSoup(src, "lxml")
                name_part_obj = soup.find_all("h1", itemprop="name",  class_="translable")

                #print(name_part_obj.text)
                for item_name in name_part_obj:
                    part = (item_name.text)
                print(part)
                if "Радиаторы масла" in all_text:
                    if "фильтр" in part.lower():
                        name_part = "Масляный фильтр"
                        #print(name_part)
                    elif "патрубок" or 'шланг' in part.lower():
                        name_part = "Патрубок масляного радиатора"
                    elif "корпус" or "основание" in part.lower():
                        name_part = "Корпус масляного радиатора"
                    elif "с корпусом" in part.lower():
                        name_part = "Масляный радиатор с корпусом"
                    elif "прокладки" or "прокладка" or "прокладок" in part.lower():
                        name_part = "Прокладка фильтра"
                    elif "с термостатом" in part.lower():
                        name_part = "Масляный радиатор с термостатом"
                    elif "кронштейн" or "крепление"  in part.lower():
                        name_part = "Кронштейн радиатора"
                    elif "кулеры" or "кулер" in part.lower():
                        name_part = "Комплект кулеров"
                    elif "гидроусилителя" or "гидроусилитель" in part.lower():
                        name_part = "Радиатор гидроусилителя"
                    elif "внешний термостат" in part.lower():
                        name_part = "Внешний термостат"
                    elif "уплотнения" or "уплотнители" or "уплотнительное" in part.lower():
                        name_part = "Уплотнитель масляного радиатора"
                    elif "крышка" in part.lower():
                        name_part = "Крышка масляного радиатора"
                    elif "выход радиатора" in part.lower():
                        name_part = "Выход радиатора"
                    elif "подставка" in part.lower():
                        name_part = "Подставка под масляный фильтр"
                    else:
                        name_part = "Радиатор масляный"
                if "Радиаторы воздуха" in all_text:
                    if "charge pipe" or "воздуховод" or "труба" or "шланг" in part.lower():
                        name_part = "Патрубок интеркулера"
                    elif "крепление" in part.lower():
                        name_part = "Крепление интеркулера"
                    elif "прокладки" or "прокладка" or "прокладок" in part.lower():
                        name_part = "Прокладка интеркулера"
                    elif "kolektor" in part.lower():
                        name_part = "Впускной коллектор"
                    elif "вентилятор" in part.lower():
                        name_part = "Вентилятор радиатора"
                    elif "правый интеркулер" in part.lower():
                        name_part = "Правый интеркулер"
                    elif "кольцо" in part.lower():
                        name_part = "Кольцо интеркулера"
                    elif "рамка" or "корпус" in part.lower():
                        name_part = "Корпус интеркулера"
                    elif "комплект радиатора" in part.lower():
                        name_part = "Комплект радиатора"
                    elif "жалюзи" in part.lower():
                        name_part = "Жалюзи интеркулера"
                    else:
                        name_part = "Интеркулер"
                if "Кулеры для воды" in all_text:

                    if "комплект кулеров" or "комплект охлаждающих" in part.lower():
                        name_part = "Комплект кулеров"
                    elif "крепление" in part.lower():
                        name_part = "Крепление радиатора"
                    else:
                        name_part = "Радиатор (основной)"
                    

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
                status = "б.у."
                num_zap = " "
                firma = " "
                version = " "
                original = " "
                all_info_obj = (soup.find_all("p"))
                weight = " "
                #print(all_info_obj)
                for item in all_info_obj:
                    #print(item, "туда")
                    item = str(item)
                    if "Состояние" or "состояние" in item: 
                        if "Новый" in item:
                            status = "Новый"
                    if "Номер детали" in item:
                        num_zap = item[item.find('<b class="translable">')+22 : item.find('</b></small>')]
                        list_num_zap = num_zap.split()
                        print(list_num_zap,"лист")
                        num_zap = ''
                        for slovo in list_num_zap:
                            if ("0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9") in slovo:
                                num_zap = num_zap + slovo + "; "
                    num_zap_all = num_zap[num_zap.find(";")+ 1 :]
                    num_zap = num_zap[: num_zap.find(";")]
                     
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
                        marka = str(marka).upper()
                        break
                string_model = " "
                
                for model, marka_1 in model_need_list.items():
                    for word in spisok_marka_model:
                        if len(word) > 1:
                            if word.lower() in model:
                                if word.lower() not in string_model:
                                    string_model = str(string_model).upper() + "!!! "+ str(word).upper()
                #print(string_model, "Смотреть сюда")
                string_model = string_model[4 : ]
                string_model = string_model[: string_model.find("!!! ")]                
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
                if int(price) > 500:
                    file = open(f"allegro_{all_text}_{time.strftime('%Y-%m-%d')}.csv", "a", encoding="utf-8", newline='')
                    writer = csv.writer(file)

                    writer.writerow(
                        (
                            artical,
                            num_zap,
                            num_zap_all,
                            marka,
                            string_model,
                            year,
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
                    print("    ")
            else:
                print(f"Уже было, давай следующую! Повторений уже {count}" )
                count += 1





with open('json_href_str.json', encoding="utf-8") as file:
    all = json.load(file)
nomer = 2
for all_text, href_str in all.items():
    #print(href_str)
    if nomer == 79:
        print(all_text)
        if href_str == "https://wallegro.ru/cat/260576-Sistema-ABS-i-ESP.html":
            href_str = "https://wallegro.ru/cat/260618-Drajvery-ABS.html"
            name_part = "Блок ABS"
            all_text = "Система ABS и ESP 22666"
            osnova(name_part, all_text, href_str)
            
        if href_str == "https://wallegro.ru/cat/254664-Reshetki-radiatora.html":
            name_part = "Решетка радиатора"
            osnova(name_part, all_text, href_str)

        if href_str == "https://wallegro.ru/cat/18690-Radiatory.html":
            href_str = "https://wallegro.ru/cat/251083-Radiatory-masla.html"
            all_text = "Радиаторы масла 130018"
            name_part_1 = "Радиатор масляный"
            print(name_part_1)    
            #osnova(name_part_1, all_text, href_str)

            href_str = "https://wallegro.ru/cat/251084-Radiatory-vozduxa-intercoolery.html"
            all_text = "Радиаторы воздуха 187095"
            name_part_2 = "Интеркулер" 
            print(name_part_2)   
            #osnova(name_part_2, all_text, href_str)

            href_str = "https://wallegro.ru/cat/251082-Kulery-dlya-vody.html"
            all_text = "Кулеры для воды 659161"
            name_part_3 = "Радиатор (основной)"    
            osnova(name_part_3, all_text, href_str)
        
    nomer += 1
    
