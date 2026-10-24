N=int(input("Enter a number:"))
print("The factors of",N,":",end='1,')
for i in range(2,(N)//2+1):
    if N%i == 0:
        print(i,end=",")
print(N)