import collections

pets = dict()
pets_name = dict()
own_info = dict()
num_id = 0
def create():
   # last = collections.deque(pets, maxlen=1)
    global num_id
    num_id += 1
    pets[num_id] = pets_name
    name = input('Введите кличку животного: ')
    pets_name[name] = own_info
    type_pet = input('Введите вид животного: ')
    age = int(input('Введите возраст животного: '))
    owner = input('Введите имя владельца животного: ')
    own_info['type_pet'] = type_pet
    own_info['age'] = age
    own_info['owner'] = owner

    print(pets)

def get_pet():
    id_req = int(input())
    if id_req in pets.keys():
        return pets_name[id_req]
    else:
        return False

#
# def get_suffix(age):
#
# def pets_list():
#
# def read():
#
# def update():
#
# def delete():

command = ''
while command != 'stop':
    command = input()
    if command == 'create':
        create()
    elif command == 'get_pet':
        get_pet()