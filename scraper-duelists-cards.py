import requests
from bs4 import BeautifulSoup
import csv
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get('https://www.yugiohfm.com/p/drops-onde-ganhar-cada-carta_43.html', headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

s_duelist = soup.find(id='saa')
s_duelists_links = s_duelist.find_all('a', href=True)

s_links = [];

for link in s_duelists_links:
    s_links.append(link['href'])

os.remove('duelists_cards.csv')

for link in s_links:
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    duelist = soup.find(class_='post-title entry-title').text

    with open('duelists_cards.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([duelist])

    tableCards = soup.find_all(class_='post-body entry-content float-container')
    tableItem = tableCards[0].find_all(class_='area_yfmpro')
    # foreach
    for item in tableItem:

        # print(item)
        card_number = item.find(class_='num_yfmpro').text

        chance = item.find(class_='chan_yfmpro').text.replace(',', '.').replace('%', '')

        with open('duelists_cards.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([card_number, chance])