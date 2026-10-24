# 0,0,1,1,2,4,7,13,24...
n=int(input("Enter the Number of terms to be displayed(at least 4):"))
n=n-3
a=0
b=0
c=1
print("0 ,0 ,1 ,",end='')
while n>0:
    d=a+b+c
    a,b,c=b,c,d
    print(d,",",end='')
    n=n-1