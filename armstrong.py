n=int(input("Enter a Number:"))
s=0
k=n
d=0
while n!=0:
    d+=1
    n//=10
n=k
while n!=0:
    s=s+pow(n%10, d)
    n//=10

if s==k:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")