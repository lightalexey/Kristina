
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 5 * F(n - 1) + 3 * n
print(F(4))