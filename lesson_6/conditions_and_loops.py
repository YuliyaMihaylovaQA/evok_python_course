user_input = input('your number: ')

if user_input.isnumeric():
    user_input = int(user_input)
    if user_input == 1:
        print('One')
    elif user_input == 2:
        print('two')
    elif user_input == 3:
        print('three'())
    else:
        print('many')
else:
    print('Enter a number please')


names = ['John', 'Tim', 'James', 'Bob', 'Jim', 'Bill']
for name in names:
    name = name.replace('i', 'I')
    if name.startswith('J'):
        print('Mr.', end=' ')  # убираем перевод строки
    print(name)

persons = {'John': 132, 'Tom': 167, 'James': 180}
for person in persons:
    print(f'{person}: {persons[person]}')


persons = {'John': 132, 'Tom': 167, 'James': 234}
for name, height in persons.items():     # раложили по значениям кортеж
    print(f'{name}: {height}')

# распечатать слова без буквы "о" и убрать из списка все слова без юуквы "o"
text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris.'

words = text.split()
fin_words = [] # строку преобразуем в список
for word in words:
    if 'o' in word:
        print(word)
    else:
        fin_words.append(word) # если в слове нет буквы "о" добавл к финальному списку

print(' '.join(words)) # распечатываем финальный список в виде строки

