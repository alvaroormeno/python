import json
import urllib.request


url = 'http://py4e-data.dr-chuck.net/comments_2196243.json'

uh = urllib.request.urlopen(url)
data = uh.read()


info = json.loads(data.decode())
# print(info['comments'])

usersArray = info['comments']

totalSum = 0
for user in usersArray:
    count = user['count']
    totalSum = totalSum + count

print('Count:', totalSum)
