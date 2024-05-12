#s = input()
s = 'Мама мыла раму'
k = len(s)
print('количество символов в строке равно', k)
print(len(s))
print(s[0], s[k-1], s[-1])
print(s[0:4])
k_a = 0
for i in range(len(s)):
    if s[i] == 'а':
        k_a += 1

k = 0
for i in s:
    if i == ' ':
        k += 1

print(k, k_a, s.count('а'))

print(s.count('раму'))
s += '!'
s = 'м' + s[1:]
print(s)
print(s.replace('м', 'М', 1))
print(s)
s = s.replace('м', 'М', 1)
print(s)