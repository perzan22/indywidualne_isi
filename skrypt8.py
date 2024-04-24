from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':

    URL = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing'
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html.parser')

    print(soup.text)

    print(soup.find_all(class_='css-1ojmxpg e88tro02'))