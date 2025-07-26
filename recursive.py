import time
num=int(input("Enter any number :"))
start_time=time.time()
def factorial(n):
  factorial=1
  for i in range(2,n+1):
    factorial*=i
    return factorial
factorial=factorial(num)
print("Factorial of",num,"is",factorial)
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
