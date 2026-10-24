# 0,1,1,2,3,5,8,13,21,34,55,89,144...
n=int(input("Enter the number of terms to be displayed(at least 3):"))
a=0
b=1
n=n-2
print("0, 1 ,",end='')
while n>0:
    c=a+b
    a,b=b,c
    print(c,",",end='')
    n-=1