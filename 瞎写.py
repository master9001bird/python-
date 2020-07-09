import time
import os
'''此函数为选择练习'''
def exercise_bank():
    return 

'''此函数为知识点复习'''
def knowledge_bank():
    x = 0
    while(1):
        if(x==0):
            zifu='0在补码以及移码中表示一样，所以补码表示的范围比原码反码多一,表示范围为-2^n到+2^n-1'
            print(zifu.center(50))
            time.sleep(6)
            os.system('clear')
            x=x+1
        elif(x==1):
            zifu='浮点数表示分为符号位，位数位以及位数为，从左至右为abc,最后的结果为(a)c*2^b，a为符号位'
            print(zifu.center(50))
            time.sleep(6)
            os.system('clear')
            x=x+1
        elif(x==2):
            zifu='溢出包括上溢出以及下溢出'
            print(zifu.center(60))
            time.sleep(6)
            os.system('clear')
            x=x+1
        else:
            continue

        if(x%3==0):
            panduan="是否停止学习？是请输入1，否请输入0"
            print(panduan.center(50))
            exit_num=eval(input())
            if(exit_num==0):
                os.system('clear')
                continue
            elif(exit_num==1):
                shuchu='byebye'
                print(shuchu.center(50))
                time.sleep(1)
                os.system('clear')
                return
            else:
                continue
            
    return 
def main():
    zifu1='欢迎练习软考中级证书——软件设计师习题'
    zifu2='输入1进行习题练习，输入0进入知识点复习'
    print(zifu1.center(50))
    time.sleep(2)
    print(zifu2.center(50))
    
    exit_num = 0 #这是判断练习是否停止的标识
    
    while(1):
        
        point = eval(input())

        if(point==0):
            os.system('clear')
            knowledge_bank()
            print("是否继续复习另一题库，是请输入1，否请输入0")
            exit_num=eval(input())
            if(exit_num==0):
                break;
            elif(exit_num==1):
                exer
        
        elif(point==1):
            exercise_bank()
            print("是否继续复习另一题库，是请输入1，否请输入0")
            exit_num=eval(input())
            if(exit_num==0):
                break;
        else:
            print("指令有误，请重新输入")

        

    print("复习完成，欢迎下次回来")

if __name__ == '__main__':
    main()
