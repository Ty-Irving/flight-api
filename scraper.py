from bs4 import BeautifulSoup
from requests_html import HTMLSession
import time

class Scraper():
    def scrapedata(self, code):
        url = f'https://uk.flightaware.com/live/airport/{code}'
        s = HTMLSession()
        r = s.get(url)
        soup = BeautifulSoup(r.html.html, 'html.parser')
        table = soup.find('div', {'class': 'large-2 medium-4 small-4 columns bottomShadowBackground thinGrayBorder no-padding-ad'})
        print(table.prettify)
        
airport = Scraper()
airport.scrapedata('cyyc')

