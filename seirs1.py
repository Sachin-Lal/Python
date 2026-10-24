n=int(input("Enter the number of terms:"))
d=0
n=n*2
for i in range(2,n+1,2):
    d=d*10
    d=d+i
    print(d,end=", ")