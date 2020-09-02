import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup


count = 0                               # Initialize variables
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('p')
for tag in tags:
    count += 1                          # Counter
print(count)
