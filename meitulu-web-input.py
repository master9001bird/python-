import requests
from bs4 import BeautifulSoup as BS
import os
import re

'''
爬取编号为1-100的网页图片
若编号为0，则url不带后缀，若编号不为0,后面的url需要添加_2开始的后缀
'''



urlstart=(str(input("请输入组图编号")))
root="E://assis/精选单组/meitulu/"+str(urlstart)+"//"

for i in range(0,100):
    if(i==0):
        url = requests.get("http://meitulu.92demo.com/item/"+urlstart+".html")
        url.encoding=url.apparent_encoding
        web_text=BS(url.text,"html5lib")
        photo_web=web_text.find("img",attrs={"class":"content_img"})
        photo_address=re.findall(r'http:.+.jpg',str(photo_web))
        path = root + str(i)+".jpg"
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            x = requests.get(str(photo_address)[2:-2])
        if(x.status_code==200):
            with open(path,'wb') as f:
                f.write(x.content)
            f.close()
            print(i+1,",ok")
        else:
            print(i+1,'error')
            break
    else:
        url = requests.get("http://meitulu.92demo.com/item/"+urlstart+"_"+str(i+1)+".html")
        url.encoding=url.apparent_encoding
        web_text=BS(url.text,"html5lib")
        photo_web=web_text.find("img",attrs={"class":"content_img"})
        photo_address=re.findall(r'http:.+.jpg',str(photo_web))
        path = root + str(i)+".jpg"
        if not os.path.exists(path):
            r = requests.get(str(photo_address)[2:-2])
        if(r.status_code==200):
            with open(path,'wb') as f:
                f.write(r.content)
            f.close()
            print(i+1,",ok")
        else:
            print(i+1,'error')
            break
