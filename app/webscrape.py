import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://eldenring.wiki.fextralife.com/Gravesite+Plain#gsc.tab=0&gsc.q=scadu%20altus&gsc.sort='
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the relevant HTML elements containing the items
items_data = []
items_list = soup.find_all('div', class_='wiki_link')  # Adjust based on actual HTML structure

for item in items_list:
    name = item.find('span', class_='wiki_link-class').text.strip()  # Adjust based on actual HTML structure
    description = item.find('span', class_='wiki_link-class').text.strip()  # Adjust based on actual HTML structure
    items_data.append({
        'name': name,
        'description': description
    })

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(items_data)
print(df.head())
