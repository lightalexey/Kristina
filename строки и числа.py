n = 12340
print(n % 10)
print(str(n)[-1])
# а первая цифра?
print(str(n)[0])
nn = n
while nn > 0:
    n1 = nn % 10
    nn = nn // 10
print(n1)
# найти количество четных цифр
nn = n
k = 0
while nn > 0:
    if nn % 2 ==0:
        k += 1
    nn = nn // 10
print(k)
s = str(n)
k = 0
for i in s:
    if int(i) % 2 == 0:
        k += 1
print(k)

s = str(n)
k = 0
for i in s:
    if i in '02468':
        k += 1
print(k)
print(s.count('0') + s.count('2') + s.count('4') + s.count('6') + s.count('8'))