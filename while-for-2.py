x = int(input())
count = 0

if x <= 2 * 10 ** 9:
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    print(count)
