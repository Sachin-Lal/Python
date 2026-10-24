d = int(input("Enter the distance covered:"))
if d>30:
    fare=190 + (d-30)*4
elif d>20 and d<=30:
    fare=140 + (d-20)*5
elif d>10 and d<=20:
    fare=80 + (d-10)*6
else:
    fare=80

print(f"Your fare for {d} miles is $ {fare}")