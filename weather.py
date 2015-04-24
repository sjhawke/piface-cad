#!/usr/bin/env python3


# . ./venv/bin/activate
# pip install -r requirements.txt
# pip freeze > requirements.txt
# ./venv/bin/deactivate

# http://www.crummy.com/software/BeautifulSoup/bs4/doc/
# http://kochi-coders.com/2011/05/30/lets-scrape-the-page-using-python-beautifulsoup/

from bs4 import BeautifulSoup
from urllib import request

# Basingstoke
url = "http://www.bbc.co.uk/weather/2656192"

page = request.urlopen(url)

soup = BeautifulSoup(page.read())

uvDomSection = soup.findAll('div',{'class' : 'environmental-index uv-index'}) 

uv = soup.findAll('span', { 'class' : 'value' })[0].contents[0]
pollution = soup.findAll('span', { 'class' : 'value' })[1].contents[0]
pollen = soup.findAll('span', { 'class' : 'value' })[2].contents[0]

# [<span class="value">4</span>, <span class="value">Low</span>, <span class="value">High</span>]

print("UV Index is:" + uv + " [1-7]")
print("pollution is: " + pollution)
print("pollen count is: " + pollen)
