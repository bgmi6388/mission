n=int(input())
for i in range(0,n):
    print(' ' *(n-i-1), end='')
    for j in range (2*i+1):
     print ('*',end='')
    print(' ')
 
    
for i in range(n+2):
    for j in range(n):
        if(j==n-1):
            print("e",end=" ")
        else:
            print("-",end=" ")
    print()

for i in range(0,n):
    print(' ' *(2*n-i-1), end='')
    for j in range (2*i+1):
     print ('*',end='')
    print(' ')    

    