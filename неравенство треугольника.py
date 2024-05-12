a = int(input('Введи a='))
b = int(input('Введи b='))
c = int(input('Введи c='))
# print (a < b + c and b < a + c and c < a + b )
if a < b + c and b < a + c and c < a + b:
    # print('Треугольник существует')
    if a == b == c:
        print('Треугольник равносторонний')
    else:
        if a == b or a == c or b == c:

            print('Треугольник равнобедренный')
        else:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print('Треугольник прямоугольный')
            else:
                print('Произвольный')

else:
    print('нет')



