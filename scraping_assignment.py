from urllib.request import urlopen
from bs4 import BeautifulSoup
#import ssl
import re

# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
total = 0
for tag in tags:
    # Look at the parts of a tag
    content = re.findall('[0-9]+', tag.contents[0])
    total += int(content[0])
print(total)