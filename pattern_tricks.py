# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     print("   "*(n+1-i)+"* "*i)

# n=input("Enter your name:")
# for i in range(len(n),-1,-1):
#     print(n[:i])

n=int(input("Enter the number of rows:"))

for i in range(n):
    print(" ".join("*" if (i+j)%2 == 0 else "#" for j in range(n)))