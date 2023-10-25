def fact(a):
    fact_1 = 1
    for i in range(1, a + 1):
        fact_1 *= i
    return fact_1

n = int(input())
fact(n)
fact_2 = 1
fact_sum = list()

for j in range(1, fact(n)):
    fact_2 *= j
    fact_sum.append(fact_2)

fact_sum.reverse()
print(fact_sum)

