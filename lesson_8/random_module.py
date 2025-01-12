import random

print(random.randint(1, 10))


print(random.random())
print(f'Your price is {int(random.random() * 100)}')
print(random.randint(0, 1)) # обе границы вкл
print(random.randrange(0, 10, 2))
users = ['user11', 'user12', 'user100']
print(random.choice(users))
# pypi.org - проверка для установки внешних модулей