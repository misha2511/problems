print("linear Search:")
value=int(input("Value to search:"))
arr=[5,4,3,2,8]
n=len(arr)
found=False
for i in range(0,n-1):
    if(arr[i]==value):
      print(value,"Found at",i)
      found = True
      break
else:
  print(value,"not found")
