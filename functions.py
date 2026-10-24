arr=[1,3,5,8,9,6,5,2]
la=arr[:arr.index(max(arr))]
ra=arr[arr.index(max(arr))+1:]

f=-1
for i in ra:
    if i in la:
        f=i
        break

print(f)