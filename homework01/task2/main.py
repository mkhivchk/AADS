from random import randint, choice


def linear_search(data, guess):
    result = []
    for i in range(len(data)):
        if data[i] == guess:
            result.append(str(i))

    if len(result) == 0:
        return '1'

    return result


with open('input.txt', 'w') as f:
    a = [randint(-10 ** 3, 10 ** 3) for i in range(randint(0, 10 ** 3))]
    f.write(str(len(a)) + '\n')
    f.write(' '.join(list(map(str, a))))

guessnum = randint(-10 ** 3, 10 ** 3)

with open('output.txt', 'w') as res:
    reslist = linear_search(a, guessnum)
    res.write(' '.join(reslist))

