import requests
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path

#Getting jobs
URL = "https://999.md/ru/list/work/development"
page = requests.get(URL)

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
jobs = soup.find_all('h5', 'ads-list-work-detail__item__title')
job_list = []
for job in jobs:
    job_list.append(job.get_text())
    print(job.get_text())
print(job_list)

#Saving to csv file
filepath = Path('jobs.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame(job_list).to_csv(filepath)