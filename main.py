

# import pymongo
import pymysql
pymysql.install_as_MySQLdb()
# import psycopg2 as ps
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
import os
import chardet


os.chdir('/Users/nithinsaikrishna/Downloads/')


file = 'battery.csv'
with open(file, 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
print(result)


dataset = pd.read_csv('new_updated.csv',encoding='utf-8') #encoding='unicode_escape'
# dataset.replace(to_replace=' ',value='NULL',inplace=True)
print(dataset)

db = create_engine("mysql://root:mnsk1315@127.0.0.1:3306/capnxt", echo=True)
connection = db.connect()
dataset.to_sql(name='battery_and_diesel',con=connection, if_exists='replace',index=False)
connection.close()
