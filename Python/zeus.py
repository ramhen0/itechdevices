from bs4 import BeautifulSoup
import requests
import math
import csv
from selenium import webdriver
from time import sleep
import os
import glob

#Change the link based on location of the installed chrome driver on your computer
chrome_link= "C:\\Users\\Mehra\\Desktop\\Python\\chromedriver_here\\chromedriver.exe"
landing_page="https://www.itechdevices.ae/"

path = "**\parent.py"

zeus_all_files=[]
for file in glob.glob(path,recursive=True):
    zeus_all_files.append(file)

for zeus_file in zeus_all_files:
    #This if statment is just for the purpose of
    exec(open(zeus_file).read())
