n = int(input())
sets = set()

if 1 <= n <= 10 ** 5:
    for i in range(n):
        k = int(input())
        if abs(k) <= 2 * 10 ** 9:
            sets.add(k)

print(len(sets))
