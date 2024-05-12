for i in range(110203, 110245 + 1):
    k = 0
    for j in range(2, i + 1):
        if i % j == 0 and j % 2 == 0:
            k += 1
    if k == 4:
        for j in range(2, i + 1):
            if i % j == 0 and j % 2 == 0:
                print(j, end=' ')
        print()

