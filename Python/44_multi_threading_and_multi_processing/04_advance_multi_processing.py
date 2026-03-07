# MultiProcessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def sq_num(num):
    time.sleep(1)
    return f"Square: {num*num}"

num=[1,2,3,4,5,6,7,8]

if __name__ == "__main__":
    t=time.time()

    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(sq_num,num)

        for result in results:
            print(result)

    finished_time=time.time()-t
    print(finished_time)