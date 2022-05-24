import pandas as pd
import json

class Scraper():

    def Arrivals(self, code):
        url = f'https://uk.flightaware.com/live/airport/{code}'
        tables = pd.read_html(url)
        print(tables[0], "\n\n")
        data = tables[0]
        Arrivals = data.to_json()
        print(Arrivals)
        

    def Departures(self, code):
        url = f'https://uk.flightaware.com/live/airport/{code}'
        tables = pd.read_html(url)
        print(tables[1], "\n\n")

    def enRoute(self, code):
        url = f'https://uk.flightaware.com/live/airport/{code}'
        tables = pd.read_html(url)
        print(tables[2], "\n\n")

    def scheduledDepartures(self, code):
        url = f'https://uk.flightaware.com/live/airport/{code}'
        tables = pd.read_html(url)
        print(tables[3], "\n\n")
        
airport = Scraper()
airport.Arrivals('yyc')

