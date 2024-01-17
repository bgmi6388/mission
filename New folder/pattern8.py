# done
# Replace '-' by a space ' '

n = 5
m = n // 2
for i in range(0, m + 1):
    for j in range(0, n):
        print("_", end=' ')
    for k in range(0, m - i):
        print("_", end=' ')
    for l in range(0, i * 2 + 1):
        print("*", end=' ')
    print()
for i in range(0, m):
    for j in range(0, n):
        print("_", end=' ')
    for k in range(0, n):
        if k == 0 or k == n - 1:
            print("@", end=' ')
        else:
            print("_", end=' ')
    print()
for i in range(0, m + 1):
    for j in range(0, i):
        print("_", end=' ')
    for k in range(0, n - i * 2):
        print("*", end=' ')
    for j in range(0, i):
        print("_", end=' ')

    if i == 0:
        for y in range(0, n):
            if y == 0 or y == n - 1:
                print("@", end=' ')
            else:
                print("_", end=' ')
    elif i > 0:
        for x in range(0, n):
            print("_", end=' ')
    for j in range(0, i):
        print("_", end=' ')
    for k in range(0, n - i * 2):
        print("*", end=' ')
    for j in range(0, i):
        print("_", end=' ')

    print()