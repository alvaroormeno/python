import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE





looptimes = 0
name = None
url = 'http://py4e-data.dr-chuck.net/known_by_Anastasija.html'

while looptimes < 7:
    # url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    anchorTags = soup('a')
    position3Tag = anchorTags[17]
    print(position3Tag)
    url = position3Tag.get('href')
    print(url)

    name = position3Tag.text
    print(name)

    looptimes = looptimes + 1



