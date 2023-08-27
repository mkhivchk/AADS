import random


def merge_sort(array: list):
    # Делим массив пополам
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

    # Рекурсивно вызываем тот же самый мердж сорт, делим разделенный масив еще раз
        merge_sort(left)
        merge_sort(right)

    # Заканчиваем делить на моменте, когда массив будет <= 1

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1

            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


with open('input.txt', 'w') as inp:
    n = random.randint(1, 200000)
    inp.write(str(n) + '\n')
    massive = [random.randint(-1000000000, 1000000000) for _ in range(n)]
    for el in massive:
        inp.write(str(el) + ' ')

with open('input.txt', 'r') as ini, open('output.txt', 'w') as out:
    data: list = ini.readlines()[1].split(' ')
    merge_sort(data)
    for nums in data:
        out.write(nums + ' ')
