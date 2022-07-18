from bs4 import BeautifulSoup
import requests

url=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text

soup = BeautifulSoup(url, 'lxml')



codes = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
print("")
for code in codes:
    date_posted=code.find("span", class_="sim-posted").text
    if not "few" in date_posted:
        company_name=code.h3.text.replace(" ", "")
        skills= code.find("span", class_="srp-skills").text.replace(" ", "")
        link_job=code.header.h2.a['href']

        print(f"Job Link: {link_job.strip()}")
        print(f"Company Name: {company_name.strip()}")
        print(f"Skills: {skills.strip()}")
        print("\n")
