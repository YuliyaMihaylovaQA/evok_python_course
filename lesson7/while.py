i = 0

while i < 5:
    print('hello')
    i += 1

print('The end')

while True:
    user_input = input('Enter something: ')
    if user_input == 'exit':
        break
    elif user_input == 'skip':
        print('skipping.....')
        continue
    elif len(user_input) > 10:
        print('Your input is too long')
    else:
        print('input is ok')

print('Good bye!')

text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris end.'

words = text.split()
fin_words = []
for word in words:
    if word == 'end':
        break
    elif 'o' in word:
        print(word)
        continue
    fin_words.append(word)

print(' '.join(fin_words))

a = 1
b = 5
c = 4
d = 7
y = 0

main_number = 47


def calc(numb):
    if y == 0:
        print(numb)
    else:
        print(numb + main_number)


calc(a)
calc(b)
calc(c)
calc(d)


def print_words(first, second, third, fourth, fifth):
    print(f'The first word is {first}, second word is {second}, {third}, {fourth}, {fifth}')


print_words('one', 'two', 'three', 'four', 'five')
print_words(fifth='five', third='three', fourth='four', first='one', second='two')


def power(number, degree=2):
    return number ** degree


print(power(2))
print(power(2, 3))


def example(e, f, g, ff='one', gg='two'):
    print(e, f, g, ff, gg)


example(2, 3, 6, gg=444)
example(3, 5, 7)


def sum_all(*args):  # позиционные  аргументы
    # print(args)
    # result = 0
    # for x in args:
    #     result += x
    # return result
    return sum(args)


print(sum_all(1, 4, 6, 5, 7))


def price_list(title, price):
    print(f'Product {title} price is {price}')


price_list('iphone', 2500)
price_list('laptop', 1500)


def price_list(**kwargs):       # именнованные аргументы
    for title, price in kwargs.items:
        print(f'Product {title} price is {price}')


price_list(iphone=2700, laptop=1700)
