n=int(input("Enter a Number:"))
s=0
for i in range(1,n//2+1):
    if n%i==0:
        s+=i

if s==n:
    print(n," is a Perfect Number.")
else:
    print(n," is NOT a Perfect Number.")