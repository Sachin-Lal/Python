a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
mx=max(a,b)

while True:
    if mx%a==0 and mx%b==0:
        lcm=mx
        break
    mx+=max(a,b)
print(f"LCM of {a} and {b}:",lcm)