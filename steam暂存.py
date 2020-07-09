import requests
from bs4 import BeautifulSoup as bs
import os
import re
import csv
import time
import threading

def steamsale0():
    r = requests.get('https://store.steampowered.com/search/?specials=1&page=1')
    r.encoding = r.apparent_encoding
    soup = bs(r.text,"html5lib")
    #先获取需要的页面，然后转化为字符串，然后调用re库的查找以及正则表达式功能
    #名称，原价，现价，地址,图片
    
    xnamelist = soup.find_all("span",attrs={"class":"title"})
    xpricelist = soup.find_all("div",attrs={"class":"col search_price discounted responsive_secondrow"})
    xpricenowlist = soup.find_all("div",attrs={"class":"col search_price discounted responsive_secondrow"})
    xaddresslist = soup.find_all('a',attrs={"class":"search_result_row ds_collapse_flag"})
    xphotolist = soup.find_all('div',attrs={"class":"col search_capsule"})



    for x in xpricelist:













    xstrnamelist=str(xnamelist)
    xstrpricelist=str(xpricelist)
    xstrpricenowlist=str(xpricenowlist)
    xstraddresslist=str(xaddresslist)
    xstrphotolist=str(xphotolist)

    xname=[]
    xprice=[]
    xpricenow=[]
    xaddress=[]
    xphoto=[]
    
    xname=re.split('[>]',xstrnamelist)
    xprice=re.split("[>]",xstrpricelist)
    xpricenow=re.split('[>]',xstrpricenowlist)
    xaddress=re.split('["]',xstraddresslist)
    xphoto=re.split('["]',xstrphotolist)
    
    xfinal_namelist=[]
    xfinal_pricelist=[]
    xfinal_pricenowlist=[]
    xfinal_addresslist=[]
    xfinal_photo=[]
      
    for x in xname:
        x=re.findall(r'.+</',x)
        if(len(str(x))!=2):
            xfinal_namelist.append(str(x)[2:-4])
            
    for x in xprice:
        x=re.findall('¥ .+</s',x)
        if(len(str(x))!=2):
            xfinal_pricelist.append(str(x)[4:-5])

    for x in xpricenow:
        x=re.findall("¥ [0-9]+.+</div$",x)
        xx=re.findall("[0-9]+",str(x))
        if(len(str(xx))!=2):
            xfinal_pricenowlist.append(str(xx)[2:-2])
    
    for xxxx in xaddress:
        xxxxx=re.findall(r'https://store.steampowered.com/app/.+150_[0-9]$|https://store.steampowered.com/bundle/.+150_[0-9]$|https://store.steampowered.com/sub/.+150_[0-9]$',xxxx)
        if(len(str(xxxxx))>2):
            xfinal_addresslist.append(str(xxxxx)[2:-2])
            
    for x in xphoto:
        xxxxx=re.findall(r'https://.+[0-9]$',x)
        if(len(str(xxxxx))>2):
            xfinal_photo.append(str(xxxxx)[2:-2])
    '''
    for i in range(0,len(xfinal_namelist)):
        print(i)
        print(xfinal_namelist[i])
        print(xfinal_pricelist[i])
        print(xfinal_pricenowlist[i])
        print(xfinal_addresslist[i])
        print(xfinal_photo[i])
        print("")
  '''
    if(1==1):
        file_path='D:/pycharm/biyeshieji/templates/py-csv/steam-zhe0.csv'
        with open(file_path,"w",newline='',encoding='UTF-8') as f:
            fieldnames=["折扣榜","原价","现价","游戏地址","图标地址"]
            f_csv=csv.DictWriter(f,fieldnames=fieldnames)
            f_csv.writeheader()
            for i in range(0,min(25,len(xfinal_namelist))):
                if(len(xfinal_namelist[i])==0):
                   continue
                else:
                    f_csv.writerow(
                    {
                        "折扣榜":xfinal_namelist[i],
                        "原价":xfinal_pricelist[i],
                        "现价":xfinal_pricenowlist[i],
                        "游戏地址":xfinal_addresslist[i],
                        "图标地址":xfinal_photo[i]
                    }
                    )
        root='D:\\pycharm\\biyeshieji\\templates\\pic\\'
        for xx in range(0,len(xfinal_namelist)):
            r=requests.get(xfinal_photo[xx])
            saves = root+str("steamsale0."+str(xx))+'.png'
            with open(saves,'wb') as f:
                f.write(r.content)        
        print("steam折扣0.csv写入完毕")
    else:
        print("当前页面数据出现问题，停止爬取")



sale1=threading.Thread(target=steamsale0)

sale1.start()

sale1.join()


