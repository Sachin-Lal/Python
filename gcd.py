a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
mn=min(a,b)
hcf=1
for i in range(1,mn//2+1):
    if a%i==0 and b%i==0:
        hcf=i

lcm=(a*b)//hcf

print("HCF:",hcf)
print("LCM:",lcm)