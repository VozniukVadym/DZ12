import concurrent.futures
import time
def factorial(x):
    f=1
    for i in range(1, x+1):
        f*=i
    return f
start_time=time.time()
print(factorial(5))
print(factorial(10))
print(factorial(20))
print(factorial(50))
print(time.time()-start_time)