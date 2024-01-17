
# Online IDE - Code Editor, Compiler, Interpreter

# print("Hello world")
n=int(input())
# for i in range (0,n):
#     for j in range(n-i-1):
#         print("_",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     for j in range(n-i-1):
#         print("_",end="")
#     print()

# for i in range (0,n):
#     for j in range(0,i):
#         print("_",end="")
#     for j in range(0,2*n-2*i-1):
#         print("*",end="")
#     for j in range(0,i):
#         print("_",end="")
#     print()

# for i in range(0,n):
#     for j in range(0,n):
#         if (i==0 or i==n-1 or j==0 or j==n-1):
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()


for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    for j in range(2*n-2*i-2):
        print("_",end="")
    for j in range(0,i+1):
        print("*",end="")
    print()

for i in range(n-2,0,-1):
    for j in range(0,i+1):
        print("*",end="")
    for j in range(2*n-2*i-2):
        print("_",end="")
    for j in range(0,i+1):
        print("*",end="")
    print()

