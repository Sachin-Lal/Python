n=int(input("Enter a number:"))

for i in range(-1*(n-1),n):
    for j in range(n-1,-1,-1):
        if abs(i)==j or j==n-1 or j==0:
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()