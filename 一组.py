import time
import threading
import os
import requests
#看到一组图的话，替换掉urlstart跟start，如果不是美图录的话，替换掉url跟http
def xianlu1():
    print("图片地址为url + urlstart + i.jpg")
    time.sleep(1)
    urlstart=start=eval(input("请输入urlstart\n"))
    urladdress = str(input("请输入url\n"))
    i=1
    header = {"user-agent":"Mozilla/5"}
    while(i<99):
        try:
            root='E://assis//精选单组//'+'图'+str(start)+"//"
            url = urladdress + str(urlstart)+"/"+str(i)+".jpg"
            path = root + url.split('/')[-1]
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(url,headers=header,timeout = 15)
                if(r.status_code!=200):
                    print("error!连接错误")
                    break
                r.encoding = ' '
                with open(path,'wb') as f:
                    f.write(r.content)
                f.close()
            print("第{}组第{}张完成".format(urlstart,i))
        except:
            print("第",urlstart,"套"+"第",i,"张抓取失败！")
            break
        i=i+1


t1=threading.Thread(target=xianlu1,args=())

t1.start()

t1.join()

print("over")
