# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
position = int(raw_input('Enter position: '))
count = int(raw_input('Enter count: '))

for i in range(count):
    links = []
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    for tag in tags:
        links.append(tag.get('href', None))
    print links
    url = links[int(position)-1]
    print (url)