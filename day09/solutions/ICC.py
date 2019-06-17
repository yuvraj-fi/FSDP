from bs4 import BeautifulSoup
import pandas as pd
import requests

lnk = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
pg = requests.get(lnk).text
sp = BeautifulSoup(pg,"lxml")

my_tab = sp.find('table',class_="table")


A=[]
B=[]
C=[]
D=[]
E=[]


for bdy in my_tab.find_all("tbody"):
    for row in bdy.find_all("tr"):
        cel = row.find_all('td')
        A.append(cel[0].text.strip())
        B.append(cel[1].text.strip())
        C.append(cel[2].text.strip())
        D.append(cel[3].text.strip())
        E.append(cel[4].text.strip())

df = pd.DataFrame()
df["Position"]=A
df["Team"]=B
df["Matches"]=C
df["Points"]=D
df["Rating"]=E


  

import sqlite3
#from pandas import DataFrame
 
conn = sqlite3.connect ( 'icc.db' )
c = conn.cursor()
c.execute ("""CREATE TABLE COUNTRYPOS(
          no integer,
          country TEXT,
          matchweight INTEGER,
          points integer,
          rank integer
          )""")



for i in range(36):
    c.execute("INSERT INTO COUNTRYPOS VALUES ()")

c.execute("SELECT * FROM COUNTRYPOS")

print ( c.fetchall() )

conn.commit()

conn.close()
