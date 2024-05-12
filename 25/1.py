for i in range(174457, 174505 + 1):
    k = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            k = k + 1
    if k == 2:
        # print(i)
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                print(j, end=' ')
        print()