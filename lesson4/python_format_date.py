my_list = [1, 3, 6, 7, None, 'text', False, 2.42, 'sdsdf', 'last', 'last2'] # список
print(my_list)
print(my_list[2]) # вывод значения по индексу
print(my_list[0])
print(my_list[9])
print(my_list[-1]) # вывод последнего значения в списке
print(my_list[-3]) # вывод последнего с конца
my_list[2] = 42 # изменение значения в списке в определенном индексе
print(my_list)


my_second_list = []
my_second_list = list()
my_second_list.append(42)   # добавление элемента в конец списка
my_second_list.append('yukka')
print(my_second_list)
print(len(my_second_list))  # посчитать количество элементов в списке
print(my_second_list.index('yukka'))
poped = my_second_list.pop(0)  # удалить элемент из списка и также записать значение уд переменной
print(my_second_list)
print(poped)

print('y' in my_second_list) # проверить элемент есть в списке


my_tuple = (1, 3, 6, 7, None, 'text', False, 2.42)
print(my_tuple[2])  # вывод значения по индексу
print(my_tuple[-1]) # вывод последнего элемента в кортеже

my_tuple = ()  # пустой кортеж
my_tuple = tuple()
my_tuple = (1, 5, 2, 6, 1)
print(my_tuple)
print(my_tuple.count(1)) # посчитает сколько 1 в кортеже
print(my_tuple.index(5)) # выводит номер индекса для элемента 5

llist = [56]
print(llist)
ttuple = (56,) # чтобы появились скобки ставим запятую в случае одного элемента в кортеже
print(ttuple)
print(type(ttuple))

my_set = {1, 3, 6, 7, None, 'text', False, 2.42, 3, 7}
# print(my_set[2])
my_set.add(42) # set содержит только уникальные значения
my_set.add('text') # при доб элемента python проверит уникален элемент или нет
print(my_set)

list1 = list(set([1, 2, 5, 6, 2, 1, 8])) # как вывести из списка только уникальные
# значения перевести в set и обратно преобразовать
# list1 = set(list1)
# list1 = list(list1)

print(list1)


my_set = {} # Это словарь
print(type(my_set))
my_set = set() #  Пустой set можно создать только так
print(type(my_set))


my_dict = {'one': 'value', 'two': 'value2'} # словарь содержит пары кл значение
print(my_dict['one'])
print(len(my_dict))
my_dict['one'] = 'myvalue' # можно изменить значение для опр существующего ключа
my_dict['three'] = 'value3' # можно добавить новую пару кл значение
my_dict['four'] = False
my_dict['five'] = [1, 5, 8]
my_dict['six'] = {1, 6, 9}
my_dict[2] = 'skldjflskdf'
my_dict[False] = 'skdjhskdjf'
my_dict[2.42] = 'werwerw'
my_dict[(1, 2)] = 'ieruyieurtert'
my_dict[5] = {1: 2}



print(my_dict)
print(type(my_dict))

print(my_dict.keys())  # посмотреть все ключи
print(my_dict.values()) # посмотреть значения
print(my_dict.items()) # посмотреть все ключи значения