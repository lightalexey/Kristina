for a in range(1, 1000000000 + 1):
    k = 0
    for i in range(1, a // 2 + 1):
        if a % i == 0:
            k += i  # k = k + 1
    if k == a:
        print(a, end=' ')
