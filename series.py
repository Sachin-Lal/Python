n=int(input("Enter the number of terms:"))
print("The Series:",end='')
for i in range(1,n+1):
    print(i**3 +1,end=", ")