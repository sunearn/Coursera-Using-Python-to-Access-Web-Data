import json
import urllib

url = raw_input('Insert URL: ')
f = urllib.urlopen(url)
data = f.read()
data = json.loads(data)

comments = data['comments']
count = 0

for item in comments:
    count += item['count']

print count
