import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/comments_2196240.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


spanTags = soup('span')
# print(spanTags)

totalSum = 0
for span in spanTags:
    # print(span.text)
    totalSum = totalSum + int(span.text)


print(totalSum)