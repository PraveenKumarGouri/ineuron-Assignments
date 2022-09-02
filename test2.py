n=l=int(input("enter a number :  "))
m=n*2
for i in range(m):
    if i <= m/2:
        for j in range(n,0,-1):
            print("   ",end=" ")
        for j in range(-1,i):
            print("praveen", end=" ")
        print("\r")
        n=n-1
else:
    for k in range(l):
        for j in range(0,k+1):
            print("    ",end="")
        for j in range(l,0,-1):
            print("praveen",end=" ")
        l = l-1
        print("\r")