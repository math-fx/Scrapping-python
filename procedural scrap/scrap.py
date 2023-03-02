import re
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.autosphere.fr'
uri = "/recherche?market=VO&marque[]=DS&page="
num_pages = 17

def get_soup(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print("ERROR: Failed Connect on :" + str(url))
        return None

def get_links(base_url, uri, num_pages):
    urls = []
    for i in range(1, num_pages):
        urls.append(base_url + uri + str(i))
    return urls

def get_car_info(info):
    try:
        brand = ''.join(info.find("span", class_="marque").stripped_strings).strip().replace('  ', ' ')
        model = ''.join(info.find("span", class_="modele").stripped_strings).strip().replace('  ', ' ')
        characteristics = ''.join(info.find("div", class_="caract").stripped_strings).strip().replace('  ', ' ')
        price = ''.join(info.find("span", class_="bloc_prix").stripped_strings).strip().replace('  ', ' ')
        alink = info.find("a", class_="lien-fiche link_veh")["href"]

        return {'brand': brand, 'model': model, 'characteristics': characteristics, 'price': price, 'alink': alink}
    except AttributeError:
        return None

def scrap_cars(base_url, uri, num_pages):
    links = get_links(base_url, uri, num_pages)
    cars = []
    for link in links:
        soup = get_soup(link)
        infos = soup.findAll("div", class_="bloc_infos_veh_parent")
        for info in infos:
            car = get_car_info(info)
            if car:
                cars.append(car)
    return cars

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8")

def finish():
    cars = scrap_cars(base_url, uri, num_pages)
    save_to_csv(cars, "DS_cars.csv")
    print("Done")

finish()