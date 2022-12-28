import concurrent.futures
import time
import threading
start=time.perf_counter()
def caluculateTime(a):
    print("sleep for 5 second\n")
    time.sleep(a)
    return "completed sleep"
with concurrent.futures.ThreadPoolExecutor() as exexuter:
    result=[exexuter.submit(caluculateTime,i*5) for  i in range(4)]
for i in concurrent.futures.as_completed(result):
    print(i)
    print(i.result())