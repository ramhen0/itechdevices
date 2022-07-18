import requests
import os

url="https://www.itechdevices.ae/media/pdf/TRM240-Datasheet.pdf"

response = requests.get(url)

with open(os.getcwd()+'//metadata.pdf', 'wb') as f:
    f.write(response.content)
