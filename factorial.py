def factorial(n):
    if(n == 1):
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter the number : "))
print(f"factorial of the {n} is {factorial(n)}")