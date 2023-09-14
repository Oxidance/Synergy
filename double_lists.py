import random

n = int(input()) # запрашиваем количество элементов по горизонтали
m = int(input()) # запрашиваем количество элементов по вертикали

matrix_1 = [[random.randint(0, 100) for i in range(n)] for j in range(m)]
matrix_2 = [[random.randint(0, 100) for k in range(n)] for l in range(m)]
result = [[matrix_1[z][x] + matrix_2[z][x] for x in range(len(matrix_1[0]))] for z in range(len(matrix_1))]

print(matrix_1)
print(matrix_2)
print(result)
