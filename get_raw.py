import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep

round_url = 'https://www.eia.gov/petroleum/gasdiesel'
page = requests.get(round_url)
soup=BeautifulSoup(page.text,'html.parser')
dfs =pd.read_html(page.text,converters={
                  'region': str,
                  'date1 price':float,
                  'date2 price': float,
                  'date3 price': float,
                  'week ago': float,
                  'year ago': float,})
raw  = dfs[0]
print (raw.columns)
l=len(raw)
for i in range(0,1):
    row=raw.loc[i]
    print('this the ith row'+str(i))
    for j in range(0,i):
        print(row[j])
print(dfs[0])
