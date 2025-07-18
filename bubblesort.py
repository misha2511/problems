print("BUBBLE SORT ALGORITHM")
arr=[5,4,3,2,8]
n=len(arr)
for i in range (0,n-1):
  for j in range(0,n-i-1):
    if(arr[j]>=arr[j+1]):
      (arr[j],arr[j+1])=(arr[j+1],arr[j])
      print(arr)
    else:
      break
print("Sorted Arr:",arr)    
