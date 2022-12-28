import time
import threading
start=time.perf_counter()
def caluculateTime(a):
    print("sleep for 5 second \n")
    time.sleep(a)
    print("completed sleep\n")
threds =[]
for i in range(5):
    thred=threading.Thread(target=caluculateTime,args=[i*5])
    thred.start()
    threds.append(thred)
#for t in threds:
   # print(t)
 #   t.join()

finish=time.perf_counter()
print(finish-start)