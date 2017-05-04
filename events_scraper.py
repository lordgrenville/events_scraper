import requests
from bs4 import BeautifulSoup

a = "https://www.secrettelaviv.com/tickets/"

page = requests.get(a)
c= page.content
soup = BeautifulSoup(c, 'html.parser')

# table = soup.find_all('table')
events = list()
for row in soup.find_all("tr"):
    events.append(row)

print(events[14])

