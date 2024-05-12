n = 0
for i in range(245690, 245756 + 1):
    k = 0
    n += 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            k += 1
    if k == 0:
         print(n, i)
