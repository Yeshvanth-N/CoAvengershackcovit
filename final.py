import pycountry
import plotly.express as px
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
 
df1 = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')

rose =requests.get("https://www.worldometers.info/coronavirus/")
bat = BeautifulSoup(rose.content,"lxml")
toy = bat.find_all('table')[0]
pad= pd.read_html(str(toy))
ipad = (tabulate(pad[0],headers='coronavirus',tablefmt='qsl'))

print (df1.head(100))  # Get first () entries in the dataframe
print (df1.tail(50))  # Get last () entries in the dataframe
print (ipad)

# recovered = pd.read_csv(‘https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv’)

# confirmed = pd.read_csv(‘https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv’)

# deaths = pd.read_csv(‘https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv') 
