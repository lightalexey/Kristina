# пользователь вводит натуральное число, вывести на экран все его делители
a = int(input('Введи число ='))
k = 0
for i in range(1, a + 1):
    if a % i == 0:
        print(i)
        k = k + 1
print('Количество делителей равно', k)
