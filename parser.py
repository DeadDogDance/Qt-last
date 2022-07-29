from bs4 import BeautifulSoup as BS
import requests

import database

def parse():
    #
    #               WARFRAMES
    #
    r = requests.get('https://warframe.fandom.com/wiki/Warframes')
    arr = []
    html = BS(r.text, 'html.parser')

    s = set()

    for el in html.select('.WarframeNavBoxImage > a > img'):
        s.add(el['alt'].replace('Icon272.png',''))

    for el in html.select('.WarframeNavBoxImage2 > a > img'):
        text = el['alt'].replace('PrimeIcon272.png','').replace('PrimeIcon.png','').strip()
        s.add(text+' Prime')

    s = sorted(s)
    for i in s:
        database.insertItem(i,'warframe')


    #
    #           PRIMARY
    #
    s = list()

    r = requests.get('https://warframe.fandom.com/wiki/Category:Primary_Weapons')
    html = BS(r.text, 'html.parser')

    for el in html.select('.category-page__member > a'):
        s.append(el['title']) if ':'not in el['title'] and ')' not in el['title'] and 'PvP' not in el['title']else 1

    r = requests.get('https://warframe.fandom.com/wiki/Category:Primary_Weapons?from='+s[-1])
    html = BS(r.text, 'html.parser')
    for el in html.select('.category-page__member > a'):
        s.append(el['title']) if ':'not in el['title'] and ')' not in el['title'] and 'PvP' not in el['title']else 1

    for i in s:
        database.insertItem(i,'primary')


    #
    #           SECONDARY
    #
    s = list()

    r = requests.get('https://warframe.fandom.com/wiki/Category:Secondary_Weapons')
    html = BS(r.text, 'html.parser')

    for el in html.select('.category-page__member > a'):
        s.append(el['title']) if ':'not in el['title'] and ')' not in el['title'] and 'PvP' not in el['title']else 1

    r = requests.get('https://warframe.fandom.com/wiki/Category:Secondary_Weapons?from='+s[-1])
    html = BS(r.text, 'html.parser')
    for el in html.select('.category-page__member > a'):
        s.append(el['title']) if ':'not in el['title'] and ')' not in el['title'] and 'PvP' not in el['title']else 1

    for i in s:
        database.insertItem(i,'secondary')

        
    #
    #           MELEE
    #
    s = list()
    r = requests.get('https://warframe.fandom.com/wiki/Category:Melee_Weapons')
    html = BS(r.text, 'html.parser')

    for el in html.select('.category-page__member > a'):
        s.append(el['title']) if ':'not in el['title'] and ')' not in el['title'] and 'PvP' not in el['title']else 1

    r = requests.get('https://warframe.fandom.com/wiki/Category:Melee_Weapons?from='+s[-1])
    html = BS(r.text, 'html.parser')
    for el in html.select('.category-page__member > a'):
        s.append(el['title']) if ':'not in el['title'] and ')' not in el['title'] and 'PvP' not in el['title']else 1

    for i in s:
        database.insertItem(i,'melee')

    #
    #           ARCHWINGS
    # 
    s = ['Amesha','Elytron', 'Itzal', 'Odanato', 'Odanato Prime', 'Railjack']
    r = requests.get('https://warframe.fandom.com/wiki/Category:Archwing_Weapons')
    html = BS(r.text, 'html.parser')

    for el in html.select('.category-page__member > a'):
        s.append(el['title']) if ':'not in el['title'] and ')' not in el['title'] and 'Blueprints' not in el['title']else 1

    for i in s:
        database.insertItem(i,'archwing')

    #
    #           COMPANIONS AND SENTINELS
    #
    s = list()
    r = requests.get('https://warframe.fandom.com/wiki/Category:Robotic_Weapons')
    html = BS(r.text, 'html.parser')

    for el in html.select('.category-page__member > a'):
        s.append(el['title']) if ':'not in el['title'] and ')' not in el['title'] and 'PvP' not in el['title']else 1

    r = requests.get('https://warframe.fandom.com/wiki/Companion')
    html = BS(r.text, 'html.parser')

    table = html.select_one('table')
    for el in table.select('span > a > span'):
        if el.text == 'Prime':
            s.append(s[-1]+ ' ' + el.text)
        else:
            s.append(el.text)

    for i in s:
        database.insertItem(i,'companion')


    # 
    #           AMPS
    # 
    s = ['Mote Amp', 'Sirocco']
    r = requests.get('https://warframe.fandom.com/wiki/Amp')
    html = BS(r.text, 'html.parser')


    table = html.select_one('table')
    for el in table.select('span > a > span'):
        if 'Prism' in el.text:
            s.append(el.text.replace('\xa0', ' '))

    for i in s:
        database.insertItem(i,'amp')
