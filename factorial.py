import time
num=int(input("Enter any number :"))
start_time=time.time()
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n* factorial(n-1)
factorial=factorial(num)
print("Factorial of",num,"is",factorial)
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
