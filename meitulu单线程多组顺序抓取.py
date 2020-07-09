import time
import threading
import os
import requests
def xianlu1():
    urlstart = start = 10834
    while(urlstart<11000):
        i=1
        while(i<99):
            try:
                root='E://assis//'+'图'+str(start)+"//"
                url = "https://mtl.gzhuibei.com/images/img/"+str(urlstart)+"/"+str(i)+".jpg"
                http = 'https://www.meitulu.com/item/'+str(urlstart)+'.html'
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

t1.start()

t1.join()

print("over")
