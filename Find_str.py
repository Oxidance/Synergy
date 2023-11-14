str_source = 'Where are you from'
str_find = 're '

index_source = 0
index_find = 0
len_source = len(str_source)
len_find = len(str_find)

while index_source <= (len_source - len_find) and index_find  < len_find:
    if str_source[index_source + index_find] == str_find[index_find]:
        index_find += 1
    else:
        index_source += 1
        index_find = 0

print(str_source)
print(str_find)
if index_find == len_find:
    print('Такая подстрока есть. Индекс её начала {}'.format(index_source))
else:
    print('Такой подстроки в исходной строке нет')
