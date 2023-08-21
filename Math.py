n = int(input())

# Find a digit of the number
tens_of_thousands = n % 10 ** 5 // 10 ** 4
thousands = n % 10 ** 4 // 10 ** 3
hundreds = n % 10 ** 3 // 10 ** 2
dozens = n % 100 // 10
units = n % 10

print(((dozens ** units) * hundreds) / (tens_of_thousands - thousands))