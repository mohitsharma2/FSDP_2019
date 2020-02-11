"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect("icccricket_sqlite.db")
data = conn.cursor()

data.execute("""CREATE TABLE icccricket(
        Pos INTEGER,
        Team TEXT,
        Weighted Matches INTEGER,
        Points INTEGER,
        Rating INTEGER
        )"""
        )
conn.commit()

df= pd.read_csv('C:/Users/mohit/Desktop/Python/odi.csv')
print(df)
df.to_sql('icccricket', conn, if_exists='replace',index=False) # to store in data base

read=data.execute('SELECT * FROM icccricket') # read from data base

read.fetchall() # to read all data from your data base(icccricket_sqlite)


data.execute('DROP TABLE icccricket') # Delete table from data base
conn.commit() 



"""
output=============================================================



[(0, 1, 'England', 54, '6,745', 125),
 (1, 2, 'India', 64, '7,748', 121),
 (2, 3, 'New Zealand', 43, '4,837', 112),
 (3, 4, 'South Africa', 47, '5,193', 110),
 (4, 5, 'Australia', 53, '5,854', 110),
 (5, 6, 'Pakistan', 51, '5,019', 98),
 (6, 7, 'Bangladesh', 46, '3,963', 86),
 (7, 8, 'Sri Lanka', 56, '4,520', 81),
 (8, 9, 'West Indies', 57, '4,573', 80),
 (9, 10, 'Afghanistan', 43, '2,440', 57),
 (10, 11, 'Ireland', 31, '1,525', 49),
 (11, 12, 'Zimbabwe', 35, '1,538', 44),
 (12, 13, 'Netherlands', 6, '222', 37),
 (13, 14, 'Scotland', 18, '537', 30),
 (14, 15, 'United States', 12, '299', 25),
 (15, 16, 'Oman', 10, '199', 20),
 (16, 17, 'Nepal', 8, '152', 19),
 (17, 18, 'Namibia', 11, '177', 16),
 (18, 19, 'UAE', 21, '285', 14),
 (19, 20, 'Papua New Guinea', 17, '0', 0)]

"""
