for i in range(2023, 10 ** 10, 2023):
    ii = str(i)
    if ii[0] == '1' and ii[2:6] == '2139' and ii[-1] == '4':
        print(i, i // 2023)
print('------------------')
for i in range(3127, 10 ** 9, 3127):
    ii = str(i)
    if ii[-2] == '1' and ii[-4] == '3' and ii[-5] == '9' and ii[0:2] == '12':
        print(i)
print('------------------')


