for i in range(0, 10): # 0..9
    print(i, end=' ')
print()
for i in range(10): # 0..9
    print(i, end=' ')
print()
for i in range(10+1): # 0..10
    print(i, end=' ')
print()
for i in range(-5, 6): # -5..5
    print(i, end=' ')
print()
for i in range(0, 11, 2): # 0 2 4 6 8 10
    print(i, end=' ')
print()
for i in range(10, 0, -3): # 10 7 4 1
    print(i, end=' ')
print()
summa = 0
for i in range(10):
    summa = summa + i
print(summa)