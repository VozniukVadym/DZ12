import os
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
import time
def factorial(x):
    f=1
    for i in range(1, x+1):
        f*=i
    return f
                                #multiprocessing
if __name__ == '__main__':
    cpu = os.cpu_count()
    with Pool(cpu) as p:
        start_time = time.time()
        print(p.map(factorial, {5, 10, 20, 50}))
        print(time.time() - start_time)

                                #ThreadPoolExecutor
start_time=time.time()
with ThreadPoolExecutor() as executor:
    f1 = executor.submit(factorial, 5)
    f2 = executor.submit(factorial, 10)
    f3 = executor.submit(factorial, 20)
    f4 = executor.submit(factorial, 50)

    print(f1.result())
    print(f2.result())
    print(f3.result())
    print(f4.result())
print(time.time()-start_time)