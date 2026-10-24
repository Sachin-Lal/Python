n=int(input("Enter the number of rows:"))

for i in range(n+1):
    for j in range(n+1):
        if j>=i:
            print("* ",end='')
        else:
            print("  ",end='')
    print()