import sys
sys.setrecursionlimit(3000)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n + F(n - 1)

k = 0
for n in range(1, 100 + 1):
    if (F(2023) // F(n)) % 2 == 0:
        k += 1
print(k)
