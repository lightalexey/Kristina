k = k2 = k5 = k10 = 0
for i in range(100, 999+1):
    k += 1
    if i % 2 == 0:
        k2 = k2 + 1
    if i % 5 == 0:
        k5 = k5 + 1
    if i % 10 == 0:
        k10 = k10 + 1
print(k, k2, k5, k10)
