from bs4 import BeautifulSoup
import requests

url= "https://www.itechdevices.ae/cisco-router-isr-4000-isr4431-k9.html"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

lists=soup.find_all('div', class_="tbl")

stri = str(lists)

print(stri)
#print(len(lists))
print(type(stri))

for i in stri:
    print(i)
