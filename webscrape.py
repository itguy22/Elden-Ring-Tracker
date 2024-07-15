import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://eldenring.wiki.fextralife.com/Gravesite+Plain'
response = requests.get(url)

# Check response status
if response.status_code == 200:
    print("Successfully fetched the webpage.")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

# Print the HTML content for inspection
print(soup.prettify())

# Adjust the selector based on the actual HTML structure
items_list = soup.find_all('div', class_='wiki_link')

if not items_list:
    print("No items found. Check the selector.")
else:
    print(f"Found {len(items_list)} items.")

items_data = []
for item in items_list:
    # Adjust these selectors based on the actual structure
    name_tag = item.find('span', class_='wiki_link-class')
    description_tag = item.find('span', class_='wiki_link-class')
    
    if name_tag and description_tag:
        name = name_tag.text.strip()
        description = description_tag.text.strip()
        print(f"Name: {name}, Description: {description}")
        items_data.append({
            'name': name,
            'description': description
        })
    else:
        print("Name or description not found for an item.")

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(items_data)
print(df.head())
