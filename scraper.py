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


page = requests.get('https://yugioh.fandom.com'+cardLinks[0], headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

links = [4,5,24];
texts = [0,6,8,10,11,13,19,23]

tableCardDetails = soup.find_all(class_='smw-table smwfacttable')
tableRow = tableCardDetails[0].find_all(class_='smw-table-row')

rowData = []

# for cardDetails in tableCardDetails:

for index, row in enumerate(tableRow):
    if index in links:
        data = row.find(class_='smw-table-cell smwprops')
        rowData.append(data.find('a').text)
        # print(index)
    elif index in texts:
        data = row.find(class_='smw-table-cell smwprops')
        text = (data.text).replace('  +', '').replace('\xa0', '').replace(' and', '/').replace(',', '.')

        if "/" in text:
            guardians = text.split('/')
            rowData.append(guardians[0])
            rowData.append(guardians[1])
        else:
            rowData.append(text)
        # print(index)

    # if()
    # link = row.find('a', href=True)
    # cardLinks.append(link['href'])



print(rowData)