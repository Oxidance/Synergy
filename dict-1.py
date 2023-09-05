pets = dict()
own_info = dict()

name = input('Введите кличку животного: ')
pets[name] = own_info
type_pet = input('Введите вид животного: ')
age = int(input('Введите возраст животного: '))
owner = input('Введите имя владельца животного: ')
own_info['type_pet'] = type_pet
own_info['age'] = age
own_info['owner'] = owner

print('Это {} по кличке "{}". Возраст питомца: {} года. Имя владельца: {}'.format(own_info['type_pet'], \
                                                                                  ''.join(pets.keys()), own_info['age'], \
                                                                                  own_info['owner']))


