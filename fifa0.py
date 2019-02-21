# Import libraries
import requests
from bs4 import BeautifulSoup

# Request URL

# Request URL
page = requests.get(
    "https://www.fifa.com/worldcup/players/player/201200/profile.html")

# Feach webpage
soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())

# Scraping Data
# NMame # Country #Role #Age #height #International #Caps #International #Goal
player_name = soup.find(
    "div", {"class": "fi-p__name"}).text.replace("\n", "").strip()
player_country = soup.find(
    "div", {"class": "fi-p__country"}).text.replace("\n", "").strip()
player_role = soup.find(
    "div", {"class": "fi-p__role"}).text.replace("\n", "").strip()
player_age = soup.find(
    "div", {"class": "fi-p__profile-number__number"}).text.replace("\n", "").strip()
player_height = soup.find_all(
    "div", {"class": "fi-p__profile-number__number"})[1].text.replace("\n", "").strip()
player_int_caps = soup.find_all(
    "div", {"class": "fi-p__profile-number__number"})[2].text.replace("\n", "").strip()
player_int_goals = soup.find_all(
    "div", {"class": "fi-p__profile-number__number"})[3].text.replace("\n", "").strip()

print(player_name, "\n", player_country, "\n", player_role, "\n", player_age,
      "\n", player_height, "\n", player_int_caps, "\n", player_int_goals)
