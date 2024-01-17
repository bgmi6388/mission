# done
# Replace '-' by a space ' '

# this pattern was asked to me

n=5
m=n//2
for i in range(m+1):
    for j in range(m-i):
        print("-",end="")
    for j in range(m+2*i-1):
        print("*",end="")
    print()

for i in range(n+2):
    for j in range(n):
        if(j==n-1):
            print("e",end="")
        else:
            print("-",end="")
    print()

for i in range(m+1):
    for j in range(2*m+i):
        print("-",end="")
    for j in range(2*m-2*i+1):
        print("*",end="")

    print()
    
    