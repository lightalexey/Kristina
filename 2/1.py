# print('x y z')
for x in range(2):  # True False
    for y in range(2):
        for z in range(2):
            # if ((x == z) or (x <= (y and z))) == False:
            if not((x == z) or (x <= (y and z))):
                print(x, y, z)
