## When to use Multi Processing

# CPU-Bound Task: Tasks that are heavy on CPU usage
# Parallel execution

import multiprocessing
import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"Square:{i*i}")

def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube:{i*i*i}")

if __name__=="__main__":
        
    # create 2 processes
    p1=multiprocessing.Process(target=square_number)
    p2=multiprocessing.Process(target=cube_number)

    t=time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)