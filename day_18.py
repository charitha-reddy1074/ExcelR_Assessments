import requests
from bs4 import BeautifulSoup

# The URL to fetch
url = 'https://example.com'

# Fetch the webpage
response = requests.get(url)

# Parse the webpage content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract and print the title
title = soup.title.string
print(f"Title of the webpage: {title}")