import threading
import datetime
import time

def worker(number,j):
    time.sleep(number)

    print("worker",number,j)
    print("\n")

    time.sleep(number)

j=9

stt_tm=datetime.datetime.now()
for i in range(5):

    t = threading.Thread(target=worker,args=(1,1))

    t.start()
    
end_tm=datetime.datetime.now()

print((end_tm-stt_tm).seconds)
