from flask import Flask

from scraper import Scraper
airport = Scraper()
app = Flask(__name__)


@app.route('/arrivals/<code>')
def arrivals(code):
    return airport.Arrivals(code)

@app.route('/departures/<code>')
def departures(code):
    return airport.Departures(code)

@app.route('/enroute/<code>')
def enroute(code):
    return airport.enRoute(code)

@app.route('/scheduled/<code>')
def scheduled(code):
    return airport.scheduledDepartures(code)