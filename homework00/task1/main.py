import random

rand_line = [str(random.randint(-10**9, 10**9)) for _ in range(2)]

f = open('input.txt', 'w')
f.write(' '.join(rand_line))
f.close()

f = open('input.txt')
line = f.readline()
summ = sum(map(int, line.split()))
f.close()

out = open('output.txt', 'w')
out.write(str(summ))
out.close()

out2 = open('output2.txt', 'w')
second_res = int(line.split()[1])**2
summary = int(line.split()[0]) + second_res
out2.write(str(summary))
out2.close()



