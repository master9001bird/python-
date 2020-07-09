from bs4 import BeautifulSoup
import requests
import os
import time
import re

def ceshi():
    url = "https://www.meitulu.com/t/aiss/"
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    return r.text

x = ceshi()

#print(x.title)

soup = BeautifulSoup(x,"html5lib")
soup.prettify()

lis = soup.find_all('p',"p_title")
xx=[]
for i in lis:
    print(type(i))
    x =re.findall(r'\d+',str(i))
    xx.append(x)

print(xx)
