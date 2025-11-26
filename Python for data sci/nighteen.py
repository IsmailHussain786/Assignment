#18. Python Program to Find Factorial of Number Using Recursion

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)
    
print (factorial(7))