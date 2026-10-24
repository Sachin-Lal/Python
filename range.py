mn=int(input("Enter the lower range:"))
mx=int(input("Enter the higher range:"))

print(f"All Prime Numbers from {mn} to {mx} are:")
for i in range(mn,mx+1):
    flag=True
    for j in range(2,i//2+1):
        if i%j==0:
            flag=False
            break
    if flag:
        print(i,end=', ')
        