min, mike, ivan = map(int, input().split())

if mike >= min and ivan >= min:
    print(2)
elif mike >= min and ivan < min:
    print('Mike')
elif ivan >= min and mike < min:
    print('Ivan')
elif ivan + mike >= min:
    print(1)
else:
    print(0)