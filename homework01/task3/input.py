import random

with open('input.txt', 'w') as gen:
    N = random.randint(3, 5000)
    gen.write(str(N) + '\n')
    array = [str(random.randint(-10 ** 9, 10 ** 9)) for _ in range(N)]
    gen.write(str(' '.join(array)))
