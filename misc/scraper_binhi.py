import requests
from bs4 import BeautifulSoup
import csv
import os

url = 'https://binhi.ph/trees-results/?search-trees= '

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
soup

# Get table from webpage
com_name = [x.text for x in soup.find_all('p', {"class": "common_name"})]
sci_name = [x.text for x in soup.find_all('p', {"class": "sci_name"})]

species = [list(tree) for tree in zip(com_name, sci_name)]

fields = ['Common name', 'Scientific name']

with open('files/binhi_priority_trees.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(species)