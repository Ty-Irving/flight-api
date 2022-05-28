import pandas as pd
import json

class Scraper():

    def Arrivals(self, code):
        url = f'https://uk.flightaware.com/live/airport/{code}'
        tables = pd.read_html(url)
        data = tables[0]["Arrivals (More)"]
        data = data.drop("Unnamed: 4_level_1", 1)
        arrivals = data.to_json()
        return arrivals
        

    def Departures(self, code):
        url = f'https://uk.flightaware.com/live/airport/{code}'
        tables = pd.read_html(url)
        data = tables[1]["Departures (More)"]
        data = data.drop("Unnamed: 4_level_1", 1)
        departures = data.to_json()
        return departures

    def enRoute(self, code):
        url = f'https://uk.flightaware.com/live/airport/{code}'
        tables = pd.read_html(url)
        data = tables[2][f'En Route/Scheduled to {code} (More)']
        data = data.drop("Unnamed: 4_level_1", 1)
        enRoute = data.to_json()
        return enRoute

    def scheduledDepartures(self, code):
        url = f'https://uk.flightaware.com/live/airport/{code}'
        tables = pd.read_html(url)
        data = tables[3]["Scheduled Departures (More)"]
        data = data.drop("Unnamed: 4_level_1", 1)
        scheduledDepartures = data.to_json()
        return scheduledDepartures
    

