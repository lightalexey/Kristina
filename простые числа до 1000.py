for a in range(2, 1000 + 1):
    s = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            s += i  # k = k + 1
    if s == 0:
        print(a, end=' ')
