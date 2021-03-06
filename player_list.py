# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas

# Empty list to store data
id_list = []

# Fetching URL
request = requests.get(
    "https://www.fifa.com/worldcup/players/_libraries/byposition/[id]/_players-list")
soup = BeautifulSoup(request.content, "html.parser")
all = soup.find_all("a", "fi-p--link", "data-player-id")

# Check list count
print(len(all))  # 736

# Iterate to find all IDs
for ids in range(0, 736):
    all = soup.find_all("a", "fi-p--link")[ids]
    id_list.append(all['data-player-id'])

# # Data Fram to store scrapped data
df = pandas.DataFrame({
    "Ids": id_list
})
df.to_csv('player_ids.csv', index=False)
print(df, "\n Success")
