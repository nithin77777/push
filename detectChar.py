import chardet
import os
os.chdir('/Users/nithinsaikrishna/Downloads/')
file = 'battery.csv'
with open(file, 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
print(result)