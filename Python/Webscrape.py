import requests as r
import os
from bs4 import BeautifulSoup

website = "https://apod.nasa.gov/apod/astropix.html"
response = r.get(website, headers=None)

#print(response.text)


html = response.text

soup = BeautifulSoup(html, features="html.parser")
print(soup.findAll("a")[1]['href'])