n = input()

if ' ' not in n:
    if n == n[::-1]:
        print('yes')
    else:
        print('no')
