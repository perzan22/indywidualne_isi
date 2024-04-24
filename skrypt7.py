from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':

    URL = 'https://www.wp.pl/'
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html.parser')

    links = []

    for link in soup.find_all('a'):
        links.append(link.get('href'))

    print(links)