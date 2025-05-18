# importing tools
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint

# getting English translated titles
headers = {"Accept-Language": "en-US, en;q=0.5"}

# creating empty lists to store data
episode_links = []
season_links = []

# saving the beginning of url 
start_of_url = "https://www.tunefind.com"

# # looping through each page to grab episode links
# url = requests.get("https://www.tunefind.com/show/one-tree-hill/season-1")
# soup = BeautifulSoup(url.text, 'html.parser')

# episode_titles_div = soup.find_all('div', class_='EpisodeListItem_text__CfcaH')

# for container in episode_titles_div:
#     episode = container.find('a')['href']
#     episode_links.append(episode)

# looping through show page to grab season links
url = requests.get("https://www.tunefind.com/show/one-tree-hill/")
soup = BeautifulSoup(url.text, 'html.parser')

episode_titles_div = soup.find_all('div', class_='EpisodeListItem_text__CfcaH')

for container in episode_titles_div:
    season = container.find('a')['href']
    season_links.append(season)

# adding on beginning of url to partial links
proper_episode_links = [start_of_url + x for x in episode_links]
proper_season_links = [start_of_url + x for x in season_links]

print(proper_season_links)
