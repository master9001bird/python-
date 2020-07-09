import requests
from bs4 import BeautifulSoup as bs
import os
import re
import csv
import time
import threading



###################################################################################
#新品榜
def steamnew():
    r = requests.get('https://store.steampowered.com/search/?os=win&filter=popularnew')
    r.encoding = r.apparent_encoding
    soup = bs(r.text,"html5lib")
    #先获取需要的页面，然后转化为字符串，然后调用re库的查找以及正则表达式功能
    #名称，发行时间,图标地址，游戏地址
    
    xnamelist = soup.find_all("span",attrs={"class":"title"})
    xtimelist = soup.find_all("div",attrs={"class":"col search_released responsive_secondrow"})
    xphotolist = soup.find_all('div',attrs={"class":"col search_capsule"})
    xaddresslist = soup.find_all('a')
    
    
    xstrnamelist=str(xnamelist)
    xstrtimelist=str(xtimelist)
    xstrphotolist=str(xphotolist)
    xstraddresslist=str(xaddresslist)
    
    xname=[]
    xtime=[]
    xphoto=[]
    xaddress=[]
    
    xname=re.split('[,]',xstrnamelist)
    xtime=re.split("[/]",xstrtimelist)
    xphoto=re.split('["]',xstrphotolist)
    xaddress=re.split('[<]',xstraddresslist)
    
    xfinal_namelist=[]
    xfinal_timelist=[]
    xfinal_photolist=[]
    xfinal_addresslist=[]
    
    for x in xname:
        x=re.findall(">.+<",x)
        xfinal_namelist.append(str(x)[3:-3])
    
    for x in xtime:
        x=re.findall('row">.+<',x)
        xfinal_timelist.append(str(x)[7:-3])
    
    for x in xphoto:
        x=re.findall("http.+[0-9]$",x)
        if(len(str(x))!=2):
            xfinal_photolist.append(str(x)[2:-2])
    
    for xxxx in xaddress:
        xxxxx=re.findall('href="https://store.steampowered.com/app/.+150_1',xxxx)
        if(len(str(xxxxx))>2):
            xfinal_addresslist.append(str(xxxxx)[8:-2])
            '''
    file_path='D:/pycharm/biyeshieji/templates/py-csv/steam-xin.csv'
    with open(file_path,"w",newline='',encoding='UTF-8') as f:
        fieldnames=["新品榜","发行时间","游戏地址","图片地址"]
        f_csv=csv.DictWriter(f,fieldnames=fieldnames)
        f_csv.writeheader()
        for i in range(0,30):
            f_csv.writerow(
                {
                    "新品榜":xfinal_namelist[i],
                    "发行时间":xfinal_timelist[i],
                    "游戏地址":xfinal_addresslist[i],
                    "图片地址":xfinal_photolist[i]
                }
            )
    root='D:\\pycharm\\biyeshieji\\templates\\pic\\'
    for xx in range(0,len(xfinal_photolist)):
        r=requests.get(xfinal_photolist[xx])
        saves = root+str("steamnew"+str(xx))+'.png'
        with open(saves,'wb') as f:
            f.write(r.content)
            
    print("steam新品榜写入完毕")
'''
    for i in range(0,30):
        print(xfinal_namelist[i])
        print(xfinal_timelist[i])
        print(xfinal_photolist[i])
        print(xfinal_addresslist[i])
        print("###########################")



s1=threading.Thread(target=steamnew)

s1.start()
s1.join()







'''    
#######热门榜
def steamhot():    
    r = requests.get('https://store.steampowered.com/search/?os=win&filter=topsellers')
    r.encoding = r.apparent_encoding
    soup = bs(r.text,"html5lib")
    #先获取需要的页面，然后转化为字符串，然后调用re库的查找以及正则表达式功能
    #名称，发行时间,图标地址，游戏地址
    
    rnamelist = soup.find_all("span",attrs={"class":"title"})
    rtimelist = soup.find_all("div",attrs={"class":"col search_released responsive_secondrow"})
    rphotolist = soup.find_all('div',attrs={"class":"col search_capsule"})
    raddresslist = soup.find_all('a')
    
    rstrnamelist=str(rnamelist)
    rstrtimelist=str(rtimelist)
    rstrphotolist=str(rphotolist)
    rstraddresslist=str(raddresslist)
    
    rname=[]
    rtime=[]
    rphoto=[]
    raddress=[]
    
    rname=re.split('[,]',rstrnamelist)
    rtime=re.split("[/]",rstrtimelist)
    rphoto=re.split('["]',rstrphotolist)
    raddress=re.split('[<]',rstraddresslist)
    
    rfinal_namelist=[]
    rfinal_timelist=[]
    rfinal_photolist=[]
    rfinal_addresslist=[]
    
    for x in rname:
        x=re.findall(">.+<",x)
        rfinal_namelist.append(str(x)[3:-3])
    
    for x in rtime:
        x=re.findall('row">.+<',x)
        rfinal_timelist.append(str(x)[7:-3])
    
    for x in rphoto:
        x=re.findall("http.+[0-9]$",x)
        if(len(str(x))!=2):
            rfinal_photolist.append(str(x)[2:-2])
    
    for xxxx in raddress:
        xxxxx=re.findall(r'href="https://store.steampowered.com/app/.+150_1',xxxx)
        if(len(str(xxxxx))>2):
            rfinal_addresslist.append(str(xxxxx)[8:-2])
            
    file_path='D:/pycharm/biyeshieji/templates/py-csv/steam-re.csv'
    with open(file_path,"w",newline='',encoding='UTF-8') as f:
        fieldnames=["热门榜","发行时间","游戏地址","图片地址"]
        f_csv=csv.DictWriter(f,fieldnames=fieldnames)
        f_csv.writeheader()
        for i in range(0,30):
            f_csv.writerow(
                {
                    "热门榜":rfinal_namelist[i],
                    "发行时间":rfinal_timelist[i],
                    "游戏地址":rfinal_addresslist[i],
                    "图片地址":rfinal_photolist[i]
                }
            )
    root='D:\\pycharm\\biyeshieji\\templates\\pic\\'
    for xx in range(0,len(rfinal_photolist)):
        r=requests.get(rfinal_photolist[xx])
        saves = root+str("steamhot"+str(xx))+'.png'
        with open(saves,'wb') as f:
            f.write(r.content)
            
    print("steam热门榜写入完毕")
    
#######预约榜
def steamsoon():
    r = requests.get('https://store.steampowered.com/explore/upcoming/')
    r.encoding = r.apparent_encoding
    soup = bs(r.text,"html5lib")
    #先获取需要的页面，然后转化为字符串，然后调用re库的查找以及正则表达式功能
    #名称，发行时间,图标地址，游戏地址
    
    ynamelist = soup.find_all("div",attrs={"class":"tab_item_name"})
    ytimelist = soup.find_all("div",attrs={"class":"release_date"})
    yphotolist = soup.find_all('img',attrs={"class":"tab_item_cap_img"})
    yaddresslist = soup.find_all('a',attrs={"class":"tab_item"})
    
    ystrnamelist=str(ynamelist)
    ystrtimelist=str(ytimelist)
    ystrphotolist=str(yphotolist)
    ystraddresslist=str(yaddresslist)
    
    yname=[]
    ytime=[]
    yphoto=[]
    yaddress=[]
    
    yname=re.split('[,]',ystrnamelist)
    ytime=re.split("[/]",ystrtimelist)
    yphoto=re.split('["]',ystrphotolist)
    yaddress=re.split('["]',ystraddresslist)
    
    yfinal_namelist=[]
    yfinal_timelist=[]
    yfinal_photolist=[]
    yfinal_addresslist=[]
    
    for x in yname:
        x=re.findall(">.+<",x)
        yfinal_namelist.append(str(x)[3:-3])
    
    for x in ytime:
        x=re.findall('ate">.+<',x)
        yfinal_timelist.append(str(x)[7:-3])
    
    for x in yphoto:
        x=re.findall("http.+[0-9]$",x)
        if(len(str(x))!=2):
            yfinal_photolist.append(str(x)[2:-2])
    
    for xxxx in yaddress:
        xxxxx=re.findall(r'https://store.steampowered.com/app/.+170[0-9]$',xxxx)
        if(len(str(xxxxx))>2):
            yfinal_addresslist.append(str(xxxxx)[2:-2])

    file_path='D:/pycharm/biyeshieji/templates/py-csv/steam-yu.csv'
    with open(file_path,"w",newline='',encoding='UTF-8') as f:
        fieldnames=["预约榜","发行时间","游戏地址","图片地址"]
        f_csv=csv.DictWriter(f,fieldnames=fieldnames)
        f_csv.writeheader()
        for i in range(0,30):
            f_csv.writerow(
                {
                    "预约榜":yfinal_namelist[i],
                    "发行时间":yfinal_timelist[i],
                    "游戏地址":yfinal_addresslist[i],
                    "图片地址":yfinal_photolist[i]
                }
            )
    root='D:\\pycharm\\biyeshieji\\templates\\pic\\'
    for xx in range(0,len(yfinal_photolist)):
        r=requests.get(yfinal_photolist[xx])
        saves = root+str("steamsoon"+str(xx))+'.png'
        with open(saves,'wb') as f:
            f.write(r.content)
    print("steam预约榜写入完毕")
  
    for i in range(0,30):
        print(xfinal_namelist[i])
        print(xfinal_timelist[i])
        print(xfinal_photolist[i])
        print(xfinal_addresslist[i])
    print("###########################")
    for i in range(0,30):
        print(rfinal_namelist[i])
        print(rfinal_timelist[i])
        print(rfinal_photolist[i])
        print(rfinal_addresslist[i])
    print("###########################")
    for i in range(0,30):
        print(yfinal_namelist[i],"###")
        print(yfinal_timelist[i],"###")
        print(yfinal_photolist[i],"###")
        print(yfinal_addresslist[i],"###")
    print("###########################")

'''



