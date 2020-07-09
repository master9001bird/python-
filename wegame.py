import requests
from bs4 import BeautifulSoup as bs
import os
import re
import time
import threading

def wegame1():
    r = requests.get('https://www.wegame.com.cn/store/games/mars_vars/sort-3')
    r.encoding = r.apparent_encoding
    soup = bs(r.text,"html5lib")
    
    #先获取需要的页面，然后转化为字符串，然后调用re库的查找以及正则表达式功能
    #名字 原价 现价 地址 图片地址
    
    namelist = soup.find_all("div",attrs={"class":"gamecard-item"})
    pricelist = soup.find_all("div",attrs={"class":"gamecard-item"})
    pricenowlist = soup.find_all("div",attrs={"class":"gamecard-item"})
    addresslist = soup.find_all("div",attrs={"class":"gamecard-item"})
    photolist = soup.find_all("div",attrs={"class":"gamecard-item"})
    
    strname=str(namelist)
    strprice=str(pricelist)
    strpricenow=str(pricenowlist)
    straddress=str(addresslist)
    strphoto=str(photolist)
    
    name_all = re.findall('img alt=".+" class="pic"',strname)
    price_all = re.findall(r'<del>.+</del>',strprice)
    pricenow_all = re.findall('price-new.+',strpricenow)
    photo_all = re.findall(r'src=.+"/></a',strphoto)
    address_all = re.findall(r'href=".+"><img',straddress)

    
    #名称，发行日期,游戏地址，图片地址
    final_name = []
    final_price = []
    final_pricenow = []
    final_photo = []
    final_address = []
    
    #截取所需数据所在的字符串并存入对应的列表中                     
    for x in name_all:
    	final_name.append(str(x)[9:-13])
    
    for x in price_all:
    	final_price.append(str(x)[5:-6])
    
    for x in pricenow_all:
    	final_pricenow.append(str(x)[19:])
    	
    for x in address_all:
    	final_address.append('https://www.wegame.com.cn'+str(x)[6:-6])
    
    for photo_a in photo_all:
    	final_photo.append(photo_a[7:-6])
'''
    for y in range(0,len(final_name)):
        print("名称",final_name[y])
        print("原价",final_price[y])
        print("现价",final_pricenow[y])
        print("图片地址",final_photo[y])
        print("游戏地址",final_address[y])
'''
    file_path='D:/pycharm/biyeshieji/templates/py-csv/wegamesale1.csv'
    with open(file_path,"w",newline='',encoding='UTF-8') as f:
        fieldnames=["游戏名","原价","现价","游戏地址","图标地址"]
        f_csv=csv.DictWriter(f,fieldnames=fieldnames)
        f_csv.writeheader()
        for i in range(0,min(len(final_name),len(final_price),len(final_pricenow),len(final_photo),len(final_address))):
            f_csv.writerow(
                {
                    "游戏名":final_name[i],
                     "原价":final_price[i],
                    "现价":final_pricenow[i],
                    "游戏地址":final_address[i],
                    "图标地址":final_photo[i]
                }
            )

    root='D:\\pycharm\\biyeshieji\\templates\\pic\\'
    for xx in range(0,min(len(final_name),len(final_price),len(final_pricenow),len(final_photo),len(final_address))):
        r=requests.get(final_photo[xx])
        saves = root+str("wegamesale1."+str(xx))+'.png'
        with open(saves,'wb') as f:
            f.write(r.content)

    print("wegame折扣1写入完毕")


def wegame2():
    r = requests.get('https://www.wegame.com.cn/store/games/mars_vars/sort-3/page-1')
    r.encoding = r.apparent_encoding
    soup = bs(r.text,"html5lib")
    
    #先获取需要的页面，然后转化为字符串，然后调用re库的查找以及正则表达式功能
    #名字 原价 现价 地址 图片地址
    
    namelist = soup.find_all("div",attrs={"class":"gamecard-item"})
    pricelist = soup.find_all("div",attrs={"class":"gamecard-item"})
    pricenowlist = soup.find_all("div",attrs={"class":"gamecard-item"})
    addresslist = soup.find_all("div",attrs={"class":"gamecard-item"})
    photolist = soup.find_all("div",attrs={"class":"gamecard-item"})
    
    strname=str(namelist)
    strprice=str(pricelist)
    strpricenow=str(pricenowlist)
    straddress=str(addresslist)
    strphoto=str(photolist)
    
    name_all = re.findall('img alt=".+" class="pic"',strname)
    price_all = re.findall(r'<del>.+</del>',strprice)
    pricenow_all = re.findall('price-new.+',strpricenow)
    photo_all = re.findall(r'src=.+"/></a',strphoto)
    address_all = re.findall(r'href=".+"><img',straddress)

    
    #名称，发行日期,游戏地址，图片地址
    final_name = []
    final_price = []
    final_pricenow = []
    final_photo = []
    final_address = []
    
    #截取所需数据所在的字符串并存入对应的列表中                     
    for x in name_all:
    	final_name.append(str(x)[9:-13])
    
    for x in price_all:
    	final_price.append(str(x)[5:-6])
    
    for x in pricenow_all:
    	final_pricenow.append(str(x)[19:])
    	
    for x in address_all:
    	final_address.append('https://www.wegame.com.cn'+str(x)[6:-6])
    
    for photo_a in photo_all:
    	final_photo.append(photo_a[7:-6])
'''
    for y in range(0,len(final_name)):
        print("名称",final_name[y])
        print("原价",final_price[y])
        print("现价",final_pricenow[y])
        print("图片地址",final_photo[y])
        print("游戏地址",final_address[y])
'''
    file_path='D:/pycharm/biyeshieji/templates/py-csv/wegamesale2.csv'
    with open(file_path,"w",newline='',encoding='UTF-8') as f:
        fieldnames=["游戏名","原价","现价","游戏地址","图标地址"]
        f_csv=csv.DictWriter(f,fieldnames=fieldnames)
        f_csv.writeheader()
        for i in range(0,min(len(final_name),len(final_price),len(final_pricenow),len(final_photo),len(final_address))):
            f_csv.writerow(
                {
                    "游戏名":final_name[i],
                     "原价":final_price[i],
                    "现价":final_pricenow[i],
                    "游戏地址":final_address[i],
                    "图标地址":final_photo[i]
                }
            )

    root='D:\\pycharm\\biyeshieji\\templates\\pic\\'
    for xx in range(0,min(len(final_name),len(final_price),len(final_pricenow),len(final_photo),len(final_address))):
        r=requests.get(final_photo[xx])
        saves = root+str("wegamesale2."+str(xx))+'.png'
        with open(saves,'wb') as f:
            f.write(r.content)

    print("wegame折扣2写入完毕")

def wegame3():
    r = requests.get('https://www.wegame.com.cn/store/games/mars_vars/sort-3/page-2')
    r.encoding = r.apparent_encoding
    soup = bs(r.text,"html5lib")
    
    #先获取需要的页面，然后转化为字符串，然后调用re库的查找以及正则表达式功能
    #名字 原价 现价 地址 图片地址
    
    namelist = soup.find_all("div",attrs={"class":"gamecard-item"})
    pricelist = soup.find_all("div",attrs={"class":"gamecard-item"})
    pricenowlist = soup.find_all("div",attrs={"class":"gamecard-item"})
    addresslist = soup.find_all("div",attrs={"class":"gamecard-item"})
    photolist = soup.find_all("div",attrs={"class":"gamecard-item"})
    
    strname=str(namelist)
    strprice=str(pricelist)
    strpricenow=str(pricenowlist)
    straddress=str(addresslist)
    strphoto=str(photolist)
    
    name_all = re.findall('img alt=".+" class="pic"',strname)
    price_all = re.findall(r'<del>.+</del>',strprice)
    pricenow_all = re.findall('price-new.+',strpricenow)
    photo_all = re.findall(r'src=.+"/></a',strphoto)
    address_all = re.findall(r'href=".+"><img',straddress)

    #名称，发行日期,游戏地址，图片地址
    final_name = []
    final_price = []
    final_pricenow = []
    final_photo = []
    final_address = []
    
    #截取所需数据所在的字符串并存入对应的列表中                     
    for x in name_all:
    	final_name.append(str(x)[9:-13])
    
    for x in price_all:
    	final_price.append(str(x)[5:-6])
    
    for x in pricenow_all:
    	final_pricenow.append(str(x)[19:])
    	
    for x in address_all:
    	final_address.append('https://www.wegame.com.cn'+str(x)[6:-6])
    
    for photo_a in photo_all:
    	final_photo.append(photo_a[7:-6])
'''
    for y in range(0,len(final_name)):
        print("名称",final_name[y])
        print("原价",final_price[y])
        print("现价",final_pricenow[y])
        print("图片地址",final_photo[y])
        print("游戏地址",final_address[y])
'''
    file_path='D:/pycharm/biyeshieji/templates/py-csv/wegamesale3.csv'
    with open(file_path,"w",newline='',encoding='UTF-8') as f:
        fieldnames=["游戏名","原价","现价","游戏地址","图标地址"]
        f_csv=csv.DictWriter(f,fieldnames=fieldnames)
        f_csv.writeheader()
        for i in range(0,min(len(final_name),len(final_price),len(final_pricenow),len(final_photo),len(final_address))):
            f_csv.writerow(
                {
                    "游戏名":final_name[i],
                     "原价":final_price[i],
                    "现价":final_pricenow[i],
                    "游戏地址":final_address[i],
                    "图标地址":final_photo[i]
                }
            )

    root='D:\\pycharm\\biyeshieji\\templates\\pic\\'
    for xx in range(0,min(len(final_name),len(final_price),len(final_pricenow),len(final_photo),len(final_address))):
        r=requests.get(final_photo[xx])
        saves = root+str("wegamesale3."+str(xx))+'.png'
        with open(saves,'wb') as f:
            f.write(r.content)

    print("wegame折扣3写入完毕")



def wegame4():
    r = requests.get('https://www.wegame.com.cn/store/games/mars_vars/sort-3/page-3')
    r.encoding = r.apparent_encoding
    soup = bs(r.text,"html5lib")

    #先获取需要的页面，然后转化为字符串，然后调用re库的查找以及正则表达式功能
    #名字 原价 现价 地址 图片地址
    
    namelist = soup.find_all("div",attrs={"class":"gamecard-item"})
    pricelist = soup.find_all("div",attrs={"class":"gamecard-item"})
    pricenowlist = soup.find_all("div",attrs={"class":"gamecard-item"})
    addresslist = soup.find_all("div",attrs={"class":"gamecard-item"})
    photolist = soup.find_all("div",attrs={"class":"gamecard-item"})
    
    strname=str(namelist)
    strprice=str(pricelist)
    strpricenow=str(pricenowlist)
    straddress=str(addresslist)
    strphoto=str(photolist)
    
    name_all = re.findall('img alt=".+" class="pic"',strname)
    price_all = re.findall(r'<del>.+</del>',strprice)
    pricenow_all = re.findall('price-new.+',strpricenow)
    photo_all = re.findall(r'src=.+"/></a',strphoto)
    address_all = re.findall(r'href=".+"><img',straddress)

    
    #名称，发行日期,游戏地址，图片地址
    final_name = []
    final_price = []
    final_pricenow = []
    final_photo = []
    final_address = []
    
    #截取所需数据所在的字符串并存入对应的列表中                     
    for x in name_all:
    	final_name.append(str(x)[9:-13])
    
    for x in price_all:
    	final_price.append(str(x)[5:-6])
    
    for x in pricenow_all:
    	final_pricenow.append(str(x)[19:])

    for x in address_all:
    	final_address.append('https://www.wegame.com.cn'+str(x)[6:-6])
    
    for photo_a in photo_all:
    	final_photo.append(photo_a[7:-6])
'''
    for y in range(0,min(len(final_name),len(final_price),len(final_pricenow),len(final_photo),len(final_address))):
        print("名称",final_name[y])
        print("原价",final_price[y])
        print("现价",final_pricenow[y])
        print("图片地址",final_photo[y])
        print("游戏地址",final_address[y])

'''
    file_path='D:/pycharm/biyeshieji/templates/py-csv/wegamesale4.csv'
    with open(file_path,"w",newline='',encoding='UTF-8') as f:
        fieldnames=["游戏名","原价","现价","游戏地址","图标地址"]
        f_csv=csv.DictWriter(f,fieldnames=fieldnames)
        f_csv.writeheader()
        for i in range(0,min(len(final_name),len(final_price),len(final_pricenow),len(final_photo),len(final_address))):
            f_csv.writerow(
                {
                    "游戏名":final_name[i],
                     "原价":final_price[i],
                    "现价":final_pricenow[i],
                    "游戏地址":final_address[i],
                    "图标地址":final_photo[i]
                }
            )

    root='D:\\pycharm\\biyeshieji\\templates\\pic\\'
    for xx in range(0,min(len(final_name),len(final_price),len(final_pricenow),len(final_photo),len(final_address))):
        r=requests.get(final_photo[xx])
        saves = root+str("wegamesale4."+str(xx))+'.png'
        with open(saves,'wb') as f:
            f.write(r.content)

    print("wegame折扣4写入完毕")


    
w1=threading.Thread(target=wegame1)
w2=threading.Thread(target=wegame2)
w3=threading.Thread(target=wegame3)
w4=threading.Thread(target=wegame4)

w1.start()
w2.start()
w3.start()
w4.start()

w1.join()
w2.join()
w3.join()
w4.join()




        
