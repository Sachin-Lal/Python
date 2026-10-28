n=int(input("Enter n:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2 == 0:
            print("#",end=' ')
        else:
            print("*", end=' ')
    print()

for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2==0:
            print("0",end=' ')
        else:
            print("1", end=' ')
    print()

for i in range(1, n+1):
    for j in range(1,i+1):
        if j%2==0:
            print("b",end=' ')
        else:
            print("a",end=' ')
    print()