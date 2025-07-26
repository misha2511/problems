import time
print("Binary Search:")
arr=[5,4,3,2,8]
arr.sort()
print(arr)
value=int(input("Value to search:"))
n=len(arr)
left,right=0,n-1
start_time = time.time()
while left<= right:
  mid=(left+right)//2
  if arr[mid]==value:
    print(value,"found at index",mid)
    break
  elif arr[mid]<value:
    left=mid+1
  else:
    right=mid-1
else:
  print("value not found")
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
