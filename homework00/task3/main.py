import random as rd
import time


def fib_func_for(nums):
    f1 = f2 = 1
    for _ in range(2, nums):
        f1, f2 = f2, f1 + f2
    return f2


start_time = time.time()

with open('input.txt', 'w') as start:
    start.write(str(rd.randint(0, 10 ** 7)))

with open('output.txt', 'w') as result:
    with open('input.txt') as num:
        result.write(str(fib_func_for(int(num.read()) % 10)))

print(f'---- {time.time() - start_time} seconds ----')