for a in range(6, 10 ** 6):
    k = 0
    for i in range(1, a // 2 + 1):
        if a % i == 0:
            k += i
    if k == a:
        print(k)

