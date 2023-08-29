n = int(input('Введите длину первого списка - '))
set_1 = set()
set_2 = set()

if n <= 10 ** 5:
    for i in range(n):
        k = int(input())
        set_1.add(k)

j = int(input('Введите длину второго списка - '))

if j <= 10 ** 5:
    for z in range(j):
        x = int(input())
        set_2.add(x)

print(len(set_1.union(set_2)))
