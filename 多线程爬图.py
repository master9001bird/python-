import time
import threading
import os
def xianlu1():
	urlstart=2999
	start=1200
    while(urlstart>2499):
        i=1
        while(i<70):
            try:
	            root = 'D://intersting//'+str(start)+'//'
                url = "https://img1.mm131.me/pic/"+str(j)+"/"+str(i)+".jpg"
                http = 'https://m.mm131.net/xinggan/'+str(j)+'.html'
                headers={'Referer':http}
                path = root + url.split('/')[-1]
                if not os.root.exists(root):
                    os.mkdir(root)
                if not os.path.exists(path):
                    r = requests.get(url,headers=headers,timeout = 10)
                    if(r.status!=200):
                        break
                    r.encoding = ' '
                    with open(path,'wb') as f:
                        f.write(r.content)
                    f.close()
                print("第{}组第{}张完成".format(urlstart,i))
                else:
                    print("图片已存在")
            except:
                print("第"+urlstart+"套"+"第"+i+"张抓取失败！")
            i=i+1
        urlstart = urlstart - 1
        start = start - 1
'''
def xianlu3():
	urlstart = 2999
    start = 1200
    while(urlstart>2499):
        i=1
        while(i<70):
            try:
                root = 'D://intersting//'+str(start)+'//'
                url =
                path =
                if not os.root.exists(root):
                    os.mkdir(root)
                if not os.path.exists(path):
                    r = requests.get(url,headers=headers,timeout = 10)
                    if(r.status!=200):
                        break
                    r.encoding = ' '
                    with open(path,'wb') as f:
                        f.write(r.content)
                    f.close()
                print("第{}组第{}张完成".format(urlstart,i))
                else:
                    print("图片已存在")
            except:
                print("第"+urlstart+"套"+"第"+i+"张抓取失败！")
            i=i+1
        urlstart = urlstart - 1
        start = start - 1

def xianlu3():
	urlstart = 2999
    start = 1200
    while(urlstart>2499):
        i=1
        while(i<70):
            try:
                root = 'D://intersting//'+str(start)+'//'
                url =
                path =
                if not os.root.exists(root):
                    os.mkdir(root)
                if not os.path.exists(path):
                    r = requests.get(url,headers=headers,timeout = 10)
                    if(r.status!=200):
                        break
                    r.encoding = ' '
                    with open(path,'wb') as f:
                        f.write(r.content)
                    f.close()
                print("第{}组第{}张完成".format(urlstart,i))
                else:
                    print("图片已存在")
            except:
                print("第"+urlstart+"套"+"第"+i+"张抓取失败！")
            i=i+1
        urlstart = urlstart - 1
        start = start - 1

'''
t1=threading.Thread(target=xianlu1,args=())
'''
t2=threading.Thread(target=xianlu2,args=())
t2=threading.Thread(target=xianlu3,args=())
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("over")
'''
