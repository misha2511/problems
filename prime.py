n = int(input("Enter how many prime numbers you want: "))
count = 0
num = 2

print("First", n, "prime numbers are:")

while count < n:
    is_prime = True
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

    if is_prime:
        print(num, end=" ")
        count += 1

    num += 1
