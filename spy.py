n=int(input("Enter a Number:"))
s=0
p=1
k=n
while k!=0:
    s=s+(k%10)
    p=p*(k%10)
    k=k//10
if s==p:
    print(n," is a Spy Number.")
else:
    print(n," is not a Spy Number.")