from bs4 import BeautifulSoup
import requests

url=requests.get("https://www.workopolis.com/jobsearch/online-jobs/windsor-ontario?job=GVkqAELiwmRqkyqQBVs5qCLjCKDPUHrfelAhljG4rTfyn3AL4AvVSg").text

soup = BeautifulSoup(url,'lxml')

jobs=soup.find_all('article', class_="JobCard")

print("")

for job in jobs:
    title=job.h2.text
    company=job.find("div", class_="JobCard-property JobCard-company").text
    detail=job.find("div", class_="JobCard-snippet").text
    if job.find("span", class_="Salary") is None:
        salary="Not mentioned"
    else:
        salary=job.find("span", class_="Salary").text
    if job.find("time", class_="JobCard-property JobCard-age") is None:
        time="Not mentioned"
    elif len(job.find("time", class_="JobCard-property JobCard-age")) == 0 :
        time="Not mentioned"
    else:
        time=job.find("time", class_="JobCard-property JobCard-age").text

    print(f'Title: {title.strip()}')
    print(f'Company Name: {company.strip()}')
    print(f'Job Details: {detail.strip()}')
    print(f'Salary: {salary.strip()}')
    print(f'Time Since Post: {time.strip()}')


    print("")
