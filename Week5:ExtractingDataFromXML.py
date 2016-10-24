import urllib
import xml.etree.ElementTree as ET

nums = []

url = raw_input('Enter URL: ')
f = urllib.urlopen(url)
data = f.read()
tree = ET.fromstring(data)

counts = tree.findall('comments/comment')

for item in counts:
    count = int(item.find('count').text)
    nums.append(count)
print nums
print sum(nums)
