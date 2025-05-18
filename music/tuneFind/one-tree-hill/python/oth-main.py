# importing tools
import requests
from urllib.request import Request
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

# saving the beginning of url 
start_of_url = "https://www.tunefind.com"

# asking user for which season they want to download
season_input = input("Which season would you like to download: ")

# looping through each page to grab episode links
url = requests.get("https://www.tunefind.com/show/one-tree-hill/season-" + str(season_input))
soup = BeautifulSoup(url.text, 'html.parser')

print(url)

episode_titles_div = soup.find_all('div', class_='EpisodeListItem_text__CfcaH')

for container in episode_titles_div:
    episode = container.find('a')['href']
    episode_links.append(episode)

# adding beginning of url to partial links
proper_episode_links = [start_of_url + x for x in episode_links]

# creating empty lists to store data
songs = []
artists = []
scene_description = []

# looping through each page
for links in proper_episode_links:
	page = requests.get(links, headers=headers)
	soup = BeautifulSoup(page.text, 'html.parser')
	song_div = soup.find_all('div', class_='SongRow_container__TbgMq')
	sleep(randint(2, 10)) # control loop's rate by pausing between 2 and 10 seconds

	for container in song_div:
		# Songs
		name = container.h4.a.text
		songs.append(name)

		# Artists
		band = container.find('div', class_='SongEventRow_subtitle__Zal_J').text
		artists.append(band)

		# Scene Description
		description = container.find('div', class_='SceneDescription_description__SDFKK').text
		scene_description.append(description)

# building DataFrame with pandas
oth_songs = pd.DataFrame({
	'Song': songs,
	'Artist': artists,
	'Scene Description': scene_description,
	})

# saving data to CSV
oth_songs.to_csv('oth-s01.csv')