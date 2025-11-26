# Program to find Greatest Common Divisor of two numbers.
# For example, theGCD of 20 and 28 is 4 and the GCD of 98 and 56 is 14.

def GreatestCommonDivisor(a,b):
    first=[]
    second=[]

    for i in range(1,b+1):
        if b%i==0:
            second.append(i)
    print(second)
    
    for i in range(1,a+1):
        if a%i==0:
            first.append(i)
    print(first)

    common = list(set(first) & set(second))   # logic
    gcd = max(common)
    print("Common divisors:", common)
    print("GCD of", a, "and", b, "is:", gcd)


GreatestCommonDivisor(98,56)



def GCD(a,b):
    while b!=0:
        a,b=b,a%b   #logic This is the heart of the Euclidean Algorithm for finding the GCD
        return a
    print(a)

    