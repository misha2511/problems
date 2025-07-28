n=int(input("Enter number of term in list"))
ab=[]
for j in range(n):
  lst=int(input("List item:"))
  ab.append(lst) 
sum=0
if(ab[0]!=13):
  sum=ab[0]
for i in range (1,n):
  if(ab[i]!=13):
    if(ab[i-1]!=13):
      sum=sum+ab[i]
print(sum)
