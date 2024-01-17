# done
# Replace '-' by a space ' '


n=5
for i in range(n):
    for j in range(n):
        if j==0:
            print("@",end='')
    print()
if n%2==0:
    for i in range(n):
        for j in range(3*i+1):
            if i==0 and j==0:
                print("@",end='')
            else:
                print("-",end='')
        for j in range(n):
            print("*",end='')
        print()


else:
    for i in range(n):
        for j in range(2 * i + 1):
            if i == 0 and j == 0:
                print("@", end='')
            else:
                print("-", end='')
        for j in range(n):
            print("*", end='')
        print()
