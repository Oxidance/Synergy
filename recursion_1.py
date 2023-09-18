def tmp(x):
    if x < 0:
        return 0
    tmp(x - 1)
    print(x)

n = int(input())
tmp(n)
print('Конец списка')
