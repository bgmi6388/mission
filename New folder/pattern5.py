# done
# Replace '-' by a space ' '

n=5

for i in range(n//2+2):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i+1):
        print("@",end="")
    print()

for i in range(n//2+1):
    for j in range(n//2-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(n):
        if (i==n//2):
            print("@",end="")
        else:
            print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(n//2):
    for j in range(i+1):
        print(" ",end="")
    for j in range(n//2-i):
        print("*",end="")
    for j in range(n):
        print(" ",end="")
    for j in range(n//2-i):
        print("*",end="")
    print()



