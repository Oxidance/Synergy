s = input()

str_a = 0
str_e = 0
str_i = 0
str_o = 0
str_u = 0

if 'a' in s:
    str_a += 1
if 'e' in s:
    str_e += 1
if 'i' in s:
    str_i += 1
if 'o' in s:
    str_o += 1
if 'u' in s:
    str_u += 1

print(str_a, str_e, str_o, str_u, str_i)
