a, b = int(input()), int(input())
num = dict()

if b > a:
    for i in reversed(range(a, b + 1)):
        num[i] = i ** i

print(num)