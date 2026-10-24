n=int(input("Enter the number:"))
k=n
s=0
while k>0:
    d=k%10
    p=1
    for i in range(1,d+1):
        p*=i
    s+=p
    k//=10

if s==n:
    print("Special Number")
else:
    print("Not a Special Number")