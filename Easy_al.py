from random import randint

n = int(input())
list_1 = list()
s = 0

for i in range(n):
    num = randint(1, 100)
    list_1.append(num)

print('Несортированный список: ', list_1, sep='\n')

for i in range(n):
    for j in range(n - 1):
        if list_1[j] > list_1[j + 1]:
            list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]
            s += 1
            print(s, list_1)
    if s == 0:
        continue

print('Сортированный список: ', list_1, sep='\n')