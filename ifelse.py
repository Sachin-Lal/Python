age = int(input("Enter your age: "))
print("Do you have an legal ID?")
id = int(input("Enter 1 for Yes and 0 for No:"))
if age>=18 or id == 1 :
    print("You can vote.")
else:
    print("You can't vote.")