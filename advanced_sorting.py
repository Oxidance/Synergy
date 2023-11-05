def decimal(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * (decimal(n // 2))

def multiply(a, b):
    if a < b:
        return multiply(b, a)
    elif b != 0:
        return a + multiply(a, b - 1)
    else:
        return 0

def raised(c, d):
    if d <= 1:
        return c
    else:
        return c * raised(c, d - 1)

n = 13
decimal = decimal(n)
print(decimal)

a = 5
b = 3
multiply = multiply(a, b)
print(multiply)

c = 5
d = 2
raised = raised(c, d)
print(raised)


