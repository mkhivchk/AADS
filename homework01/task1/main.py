import random


def insertion_sort(data):
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if data[j] < data[j - 1]:
                data[j - 1], data[j] = data[j], data[j - 1]
            else:
                break
    return data


with open('input.txt', 'w') as enter:
    N = random.randint(1, 10 ** 3)
    enter.write(str(N) + '\n')
    array = []
    for _ in range(N):
        array.append(random.randint(-10 ** 9, 10 ** 9))

    for elem in array:
        enter.write(str(elem) + ' ')


with open('output.txt', 'w') as res:
    with open('input.txt') as input:
        s = input.readlines()
        solid = s[1].split(' ')

    res.write(str(insertion_sort(solid)))
