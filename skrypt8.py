from bs4 import BeautifulSoup
import requests

class House:

    def __init__(self, header_name, price, price_for_m2):
        self.header_name = header_name
        self.price = price
        self.price_for_m2 = price_for_m2

if __name__ == '__main__':

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    URL = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing'
    r = requests.get(URL, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')

    houses_dict = {}
    i = 1

    for house in soup.find_all(class_='css-1ojmxpg e88tro02'):
        
        header_name = house.find('p', class_='css-3czwt4 e1dhq2er0').text
        price = house.find('span', class_='css-1uwck7i e1a3ad6s0').text
        price_for_m2 = house.find_all('dd')[2].text

        offer = House(header_name, price, price_for_m2)

        houses_dict[f'{i}. '] = offer
        i += 1
    
    for key, value in houses_dict.items():
        print(key, ":", f'{value.header_name}, {value.price}, {value.price_for_m2}')
    
    with open(f'home.csv', 'w', encoding="utf-8") as file:

        file.write('Lp. Nazwa oferty, Cena, Cena za m2\n')
        for key, value in houses_dict.items():
            file.write(key + value.header_name + ', ' + value.price + ', ' + value.price_for_m2 + '\n')
    
        
        


