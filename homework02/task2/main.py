import random as rd


def writer(file, var):
    file.write(str(var) + '\n')
    massive = [rd.randint(1, 100) for _ in range(var)]
    for el in massive:
        file.write(str(el) + ' ')
    file.write('\n')


def find_pos(array: list, num: int) -> int:
    first = 0
    last = len(array) - 1

    while first <= last:
        middle = first + (last - first) // 2

        if array[middle] == num:
            return middle
        elif array[middle] < num:
            first = middle + 1
        else:
            last = middle - 1
    return -1


with open('input.txt', 'w') as inp:
    n = rd.randint(1, 100000)
    writer(inp, n)

    k = rd.randint(1, 100000)
    writer(inp, k)

with open('output.txt', 'w') as out, open('input.txt', 'r') as data:
    lines = data.readlines()
    dat = [int(it) for it in lines[1].strip('\n ').split(' ')]
    find = [int(ip) for ip in lines[3].strip('\n ').split(' ')]

    for fi in find:
        out.write(str(find_pos(dat, fi)) + ' ')


