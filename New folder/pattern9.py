n = 3
x = n + 4
for i in range(x):
    for j in range(n + 1):
        if j == 0:
            print("*", end='')
        elif i == x // 2 and (j > 0 and j <= n):
            print("e", end='')
        else:
            print("-", end='')
    for j in range(n + 1):
        if i == 0 and j == 0:
            print("-", end='')
        elif (i > 0 and i <= n + 2) and (j == 0):
            print("*", end='')
        elif i == x // 2 and (j > 0 and j <= n):
            print("e", end='')
        else:
            print("-", end='')

    if i > 1 and i < x - 2:
        print("*", end='')
    else:
        print("-", end='')

    print()