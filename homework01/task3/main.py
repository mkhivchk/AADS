import random


with open('input.txt', 'w') as gen:
    N = random.randint(3, 5000)
    gen.write(str(N) + '\n')
    array = [str(random.randint(-10 ** 9, 10 ** 9)) for _ in range(N)]
    gen.write(str(' '.join(array)))


with open('input.txt') as lst:
    data = lst.readlines()[1].split(' ')
    with open('output.txt', 'w') as result:
        for i in range(1, len(data)):
            for j in range(i, 0, -1):
                if data[j] < data[j - 1]:
                    data[j - 1], data[j] = data[j], data[j - 1]
                    result.write(f'Swap elements at indicies {j} and {j + 1}\n')
                else:
                    break
        result.write('no more swaps needed\n')
        result.write(' '.join(data))