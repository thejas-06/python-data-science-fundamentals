# Real world example: Factorial calculation

import multiprocessing
import time
import sys
import math

sys.set_int_max_str_digits(100000)

def compute_factorial(num):
    print(f"Computing factorial of {num}")
    result=math.factorial(num)
    return result

if __name__=="__main__":
    numbers=[5000,6000,7000,8000]

    start_time=time.time()

    #create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)

    print(f"Results: {results}")

    end_time=time.time() - start_time
    print(end_time)