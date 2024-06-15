import pandas as pd
import oracledb
import requests
from bs4 import BeautifulSoup
from time import sleep
round_url='https://www.eia.gov/dnav/pet/hist/leafhandler.ashx?n=pet&s=emm_epmr_pte_nus_dpg&f=w'
page=requests.get(round_url)
soup = BeautifulSoup(page.text,'html.parser')
#dfs =pd.read_html(page.text,converters ={
 #                 'year-month': str,
  #                 'week 1 date': str,
   #                 'week 1 price': str,
    #                'week 2 date': str,
     #               'week 2 price': str,     
      #              'week 3 date': str,
       #             'week 4 price': str,
        #            'week 5 date': str,
         #           'week 5 price': str,    
          #          'week ago': str,
           #         'year ago': str,      
            #      })
print(page)
#raw=dfs[4].where(pd.notnull(dfs[4]),'')
#print(raw.columns)