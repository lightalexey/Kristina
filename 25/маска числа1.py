for x1 in range(10):
    for x2 in range(10):
        number = 123450000 + x1 * 1000 + 700 + x2 * 10 + 8
        if number % 23 == 0:
            print(number, number // 23)
print('------------------')
for x1 in '0123456789':
    for x2 in '0123456789':
        number = int('12345' + x1 + '7' + x2 + '8')
        if number % 23 == 0:
            print(number, number // 23)
print('------------------')
for i in range(23, 10 ** 9, 23):
    if i % 10 == 8 and i // 100 % 10 == 7 and i // 10000 == 12345:
        print(i, i // 23)
print('------------------')
for i in range(23, 10 ** 9, 23):
    ii = str(i)
    if ii[-1] == '8' and ii[-3] == '7' and ii[0:5] == '12345':
        print(i, i // 23)