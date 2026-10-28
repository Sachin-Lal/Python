n=int(input("Enter n:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()