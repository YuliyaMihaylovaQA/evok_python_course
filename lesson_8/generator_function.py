def generate_text(text1, text2):
    return f'Text consists on the words:{text1} and {text2}'


print(generate_text('Yulia', 'Mikhaylova'))


def progression(limit=100):
    n = 2
    num = 1
    count = 1
    while count < limit:
        yield num
        num += n
        count += 1


count = 1
for number in progression(10000000000000000000000000000000000000000):
    if count == 1000000:
        print(number)
        break
    count += 1
