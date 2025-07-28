n=int(input("Enter number of term in list"))
Number=[]
for i in range(n):
  lst=int(input("List item:"))
  Number.append(lst) 
Number.sort()
print(Number)   
print(Number[len(Number) - 1])
