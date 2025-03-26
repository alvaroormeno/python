import urllib.request
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_2196242.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
# print('Retrieved',len(data),'characters')
print(data.decode())
tree = ET.fromstring(data)
# print(tree)

totalSum = 0
totalCounts = 0

counts = tree.findall('.comments/comment/count')
print(counts)
nums = list()
for result in counts:
    # Debug print the data :)
    print(result.text)
    totalSum = totalSum + int(result.text)
    totalCounts = totalCounts + 1

print('Count:', totalCounts)
print('Sum:', totalSum)
