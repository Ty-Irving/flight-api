from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pandas as pd
import time

class Scraper():
    def scrapedata(self, code):
        url = f'https://uk.flightaware.com/live/airport/{code}'
        tables = pd.read_html(url)
        print(tables[0])
        print(tables[1])
        
airport = Scraper()
airport.scrapedata('cyyc')

