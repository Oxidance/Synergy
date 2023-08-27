n = int(input())
new_list = []

for i in range(n):
    k = int(input())
    if 1 <= k <= 10000 and abs(k) <= 10 ** 5:
        newlist.append(k)

newlist.reverse()
print(newlist)
