from bs4 import BeautifulSoup
import requests

# url = 'http://www.espncricinfo.com/ci/engine/series/index.html?view=season'

source = requests.get('http://www.espncricinfo.com/ci/engine/series/index.html?view=month').text

soup = BeautifulSoup(source, 'lxml')

for match in soup.find_all('teams'):
    headline = match.a.text
    print(headline)

    # summary = article.find('div', class_='entry-content').p.text
    # print(summary)

    print()
