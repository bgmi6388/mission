n=3

for i in range(n):
    for j in range(2*n+2):
        if j==0 or (j==n+1 and i>0) or (j==2*n+2 and i>1):
            print("*",end="")
        if (i==n-1 and (j>=0 and j<=n+1)) or (i==n-1 and (j>=n+1 and j<=2*n+2)):
            print("e",end='')
        else:
            print("-",end="")
    print()

for i in range(n-1):
    for j in range(2*n+3):
        if j==0 or (j==n+1 and i<n//2+1) or (j==2*n+2 and i<n//2):
            print("*",end='')
        else:
            print("-",end='')
    print()