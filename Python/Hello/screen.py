from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from time import sleep

#this is the URL to go to individual page
url=requests.get("https://www.itechdevices.ae/ws-c2960x-24ps-l-cisco-catalyst-2960x-24-ports-10-100-1000-4-x-gigabit-sfp-managed-stackable-1u-rack-mountable-switch.html").text
soup = BeautifulSoup(url,'lxml')
links= soup.find("div", class_="product-img-column grid12-4")
#for link in links:
##    print(slink)
link=links.a["href"]

driver=webdriver.Chrome("C:\\Users\\Mehra\\Downloads\\chromedriver_here\\chromedriver.exe")
driver.get(link)
sleep(1)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end")
