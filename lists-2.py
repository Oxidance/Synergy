n = int(input())
new_list = []
if 1 <= n <= 10 ** 5:
    for i in range(n):
        k = int(input())
        if 1 <= k <= 10 ** 9:
            new_list.append(k)

new_list.insert(0, new_list[-1])
new_list.pop()
print(new_list)
