from random import randint

n = 33
arr = list()
for i in range(n):
    num = randint(1, 100)
    arr.append(num)

to_search = randint(1, 100)
answer = -1

arr.sort()
left = 0
right = len(arr) - 1
while left <= right and arr[left] <= to_search <= arr[right]:
    part_1 = float(right - left) / (arr[right] - arr[left])
    part_2 = to_search - arr[left]
    index = left + int(part_1 * part_2)

    if arr[index] == to_search:
        answer = index
        break

    else:
        right = index - 1

print(arr)
print(to_search)
print('*' * 20)

if answer != -1:
    print('Элемент {} в списке был, его индекс {}.'.format(to_search, answer))
else:
    print('Элемента {} в списке не было'.format(to_search))
