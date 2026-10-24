n=int(input("enter the Number:"))
k=n
mn=mx=k%10
k//=10
while k>0:
    if k%10 > mx:
        mx=k%10
    if k%10 <mn:
        mn=k%10
    k//=10

print(f"Max Digit in {n}:",mx)
print(f"Min Digit in {n}:",mn)