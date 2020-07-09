import time
import threading
import os
import requests
def xianlu1():
    urlstart=4500
    start=4500
    while(urlstart<4700):
        i=1
        while(i<70):
            try:
                root='E://'+'图'+str(start)+"//"
                url = "https://img1.mm131.me/pic/"+str(urlstart)+"/"+str(i)+".jpg"
                http = 'https://m.mm131.net/xinggan/'+str(urlstart)+'.html'
                headers={'Referer':http}
                path = root + url.split('/')[-1]
                if not os.path.exists(root):
                    os.mkdir(root)
                if not os.path.exists(path):
                    r = requests.get(url,headers=headers,timeout = 15)
                    if(r.status_code!=200):
                        break
                    r.encoding = ' '
                    with open(path,'wb') as f:
                        f.write(r.content)
                    f.close()
                print("第{}组第{}张完成".format(urlstart,i))
            except:
                print("第",urlstart,"套"+"第",i,"张抓取失败！")
            i=i+1
        urlstart = urlstart + 1
        start = start + 1

def xianlu2():
    urlstart=4700
    start=4700
    while(urlstart<4900):
        i=1
        while(i<70):
            try:
                root='E://'+'图'+str(start)+"//"
                url = "https://img1.mm131.me/pic/"+str(urlstart)+"/"+str(i)+".jpg"
                http = 'https://m.mm131.net/xinggan/'+str(urlstart)+'.html'
                headers={'Referer':http}
                path = root + url.split('/')[-1]
                if not os.path.exists(root):
                    os.mkdir(root)
                if not os.path.exists(path):
                    r = requests.get(url,headers=headers,timeout = 15)
                    if(r.status_code!=200):
                        break
                    r.encoding = ' '
                    with open(path,'wb') as f:
                        f.write(r.content)
                    f.close()
                print("第{}组第{}张完成".format(urlstart,i))
            except:
                print("第",urlstart,"套"+"第",i,"张抓取失败！")
            i=i+1
        urlstart = urlstart + 1
        start = start + 1

def xianlu3():
    urlstart=4900
    start=4900
    while(urlstart<5101):
        i=1
        while(i<70):
            try:
                root='E://'+'图'+str(start)+"//"
                url = "https://img1.mm131.me/pic/"+str(urlstart)+"/"+str(i)+".jpg"
                http = 'https://m.mm131.net/xinggan/'+str(urlstart)+'.html'
                headers={'Referer':http}
                path = root + url.split('/')[-1]
                if not os.path.exists(root):
                    os.mkdir(root)
                if not os.path.exists(path):
                    r = requests.get(url,headers=headers,timeout = 15)
                    if(r.status_code!=200):
                        break
                    r.encoding = ' '
                    with open(path,'wb') as f:
                        f.write(r.content)
                    f.close()
                print("第{}组第{}张完成".format(urlstart,i))
            except:
                print("第",urlstart,"套"+"第",i,"张抓取失败！")
            i=i+1
        urlstart = urlstart + 1
        start = start + 1

t1=threading.Thread(target=xianlu1,args=())
t2=threading.Thread(target=xianlu2,args=())
t3=threading.Thread(target=xianlu3,args=())
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("over")
