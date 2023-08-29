n = int(input())
sets = set()

for i in range(n):
    k = int(input())
    if k in sets:
        print('yes')
    else:
        print('no')
        sets.add(k)