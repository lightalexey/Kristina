k = 0
for x in range(1, 9):
    for y in range(1, 16):
        if x/(3 ** 0.5) < y < x/(3 ** 0.5) + 10:
            k = k + 1
print(k)