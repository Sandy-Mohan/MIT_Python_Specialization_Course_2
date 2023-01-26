from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter -')
count = int(input('Enter count:'))
position = int(input('Enter position:'))
inc = 0

while inc < count:
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position-1].get('href',None)
    #print(url)
    name = tags[position-1].contents[0]
    inc +=1
print(name)
