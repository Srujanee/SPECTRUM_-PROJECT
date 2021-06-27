n=5
no_space=0
for i in range(n,0,-1):
    for j in range(no_space):
        print(" ",end="")
    for j in range(0,i):
        print("*",end=" ")
    print()
    no_space+=1
no_space-=2
for i in range(2,n+1):
    for j in range(no_space):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()
    no_space-=1
