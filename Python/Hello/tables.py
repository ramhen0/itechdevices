# This code can be used to extract the tables
from bs4 import BeautifulSoup
import requests

url=requests.get("https://www.itechdevices.ae/cisco-cf-ie3000-memory-flash-for-1900-2900-3900-router.html").text

soup = BeautifulSoup(url,'lxml')

code=soup.find("table", class_='data-table')

stringnow=str(code)

print(stringnow)
onestring=[]
final_string=[]

onestring.append(stringnow)

print(onestring)
#print(stringnow.replace('\n'," "))

#print(len(stringnow))
#print(type(stringnow))
'''


newlist=onestring.append(code)
print(type(onestring))
print(newlist)
'''
# I need to take the code and placed inside as one string. so that I can store that string into a row as additional info
