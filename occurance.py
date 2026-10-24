l=eval(input("Enter a list of Nummbers:"))
n=eval(input("Enter the number to be counted:"))
c=0
for i in l:
    if i==n:
        c+=1

print("Number of Appearence of",n,":",c)