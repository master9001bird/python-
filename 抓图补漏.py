import requests
import os
def getImages(url,headers,root,path,i):
    try:

        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url, headers=headers,timeout=10)
            print(r.status_code)
            print(i)
            r.encoding = r.apparent_encoding
            with open(path,'wb') as f:
                f.write(r.content)
            f.close()
        else:
            print("图片已存在")
    except:
        print("出现异常")

        
j = 4958
a = 143
while(j>4957):
    for i in range(1,66):
        url = "https://img1.mm131.me/pic/"+str(j)+"/"+str(i)+".jpg"
        http = 'https://m.mm131.net/xinggan/'+str(j)+'.html'
        headers={
        'Referer':http}
        roots = 'E://intersting//图'+str(a)+'//'
        root = roots
        path = root + url.split('/')[-1]
        getImages(url,headers,root,path,i)
    print(j,"组完成")
    a=a+1
    j=j-1
    








        
