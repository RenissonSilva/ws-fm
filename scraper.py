import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get('https://yugioh.fandom.com/wiki/List_of_Yu-Gi-Oh!_Forbidden_Memories_cards', headers=headers)
                    
soup = BeautifulSoup(page.text, 'html.parser')

allCards = soup.find_all(class_='Card smwtype_txt')
cardLinks = [];

for card in allCards:
    link = card.find('a', href=True)
    cardLinks.append(link['href'])

# for cardLink in cardLinks:
#     page = requests.get('https://yugioh.fandom.com'+cardLinks, headers=headers)
page = requests.get('https://yugioh.fandom.com'+cardLinks[0], headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

linksDefault = [4, 5, 24]; #card type, card type short, type
textsDefault = [0, 6, 8, 10, 11, 13, 19, 23] #atk, def, englishname, fmr number, guardian star, level, passcode, starchip

links26 = [4, 5, 26];
texts26 = [0, 6, 8, 10, 11, 13, 19, 25]


tableCardDetails = soup.find_all(class_='smw-table smwfacttable')
tableRow = tableCardDetails[0].find_all(class_='smw-table-row')

rowData = []

for index, row in enumerate(tableRow):
    if len(tableRow) == 24 | len(tableRow) == 25:
        links = linksDefault
        texts = textsDefault
    elif len(tableRow) == 26:
        links = links26
        texts = texts26

    if index in links:
        data = row.find(class_='smw-table-cell smwprops')
        rowData.append(data.find('a').text)
    elif index in texts:
        data = row.find(class_='smw-table-cell smwprops')
        text = (data.text).replace('  +', '').replace(' +', '').replace('\xa0', '').replace(' and', '/').replace(',', '.')
        # text = data.text

        if "/" in text:
            guardians = text.split('/')
            rowData.append(guardians[0])
            rowData.append(guardians[1])
        else:
            rowData.append(text)



print(rowData)