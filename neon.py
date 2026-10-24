n=int(input("Enter a Number:"))
s=n*n
k=0

while s!=0:
    k+=s%10
    s//=10

if k==n:
    print(n,"is a Neon Number.")
else:
    print(n,"is NOT a Neon Number.")