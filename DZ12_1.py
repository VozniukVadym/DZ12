import threading
import time
def factorial(x):
    f=1
    for i in range(1, x+1):
        f*=i
    return f

a = threading.Thread(target=factorial, args={5})
start_time=time.time()
a.start()
a.join()
print(time.time()-start_time)