from bs4 import BeautifulSoup as bs
import requests

# url = 'http://www.espncricinfo.com/ci/engine/series/index.html?view=season'

source = requests.get('https://www.premiershiprugby.com/aviva-premiership-rugby-fixtures/').text
soup = bs(source, 'lxml')

for div in soup.find_all('div', class_='fixture-entry'):
    print(div.text)
