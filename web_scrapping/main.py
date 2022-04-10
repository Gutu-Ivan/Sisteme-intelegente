import requests
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path

# Getting jobs
URL = "https://999.md/ru/list/work/development"
page = requests.get(URL)

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
jobs = soup.find_all('h5', 'ads-list-work-detail__item__title')
job_list = []
job_link_list = []
description_list = []

for job in jobs:
    job_list.append(job.get_text())
    children = job.findChildren("a", recursive=False)
    for child in children:
        job_link_list.append('https://999.md' + child['href'])

for job_link in job_link_list:
    response = requests.get(job_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    description = soup.find("div", class_="adPage__content__description grid_18")
    description_list.append(description.string)

print(job_list)
print(job_link_list)
print(description_list)

# Saving to csv file
filepath = Path('jobs.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df = pd.DataFrame({'Job': job_list,
                   'Description': description_list,
                   'Job link': job_link_list})
df.to_csv(filepath)
