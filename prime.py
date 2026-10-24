N=int(input("Enter a number:"))
flag=True
for i in range(2,N):
    if N%i == 0:
        flag=False
        break
if flag==True:
    print("The number is Prime.")
else:
    print("The number is Composite")