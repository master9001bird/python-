x=1234
length = len(str(x))
i = 0
a=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
for i in range(length):
    if(i==0):
        a[i]=x%10
        print(a[i],"位数")
    else:
        x1=x%(10^(i+1))
        print(x1)
        
        x2=a[i-1]*(10^(i-1))
        print(x2)
        
        x3=10^i
        print(x3)
        
        a[i]=(x1-x2)/x3
        #a[i]=( (x%(10^(i+1)) - (a[i-1])*(10^(i-1)) ) / (10^(i)))
        print(a[i],"各个位数")
        x=x-a[i-1]*(10^(i-1))   
    i=i+1


'''
print(i)
i=i-1
num=0

while(i>=0):
    if(a[i]!=-1):
        num = num + a[i]*(10^(length-i))
        print(a[i],"各个位数")
        print(num)
    i=i-1
'''
