n=int(input("Enter the number of rows:"))
for i in range(-1*(n-1),n):
    for j in range(-1*(n-1),n):
        if abs(i)+abs(j)<=(n-1):
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()