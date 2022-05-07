# first step install and import the module
# -- pip/pip3 install requests
# -- pip/pip3 install beautifulsoup4
# -- pip/pip3 install lxml

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# 2nd step use requests to fetch thew url
result = requests.get('https://www.wuzzuf.com/jobs/?q=python&l=Egypt')

# 3rd step save page content/markup
src = result.content
print(src)
