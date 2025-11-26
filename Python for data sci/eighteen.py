# 17.Write a python program using function to find the sum of odd series and even series

import math

def odd_series_sum(n):
    total = 0
    for i in range(1, 2*n, 2): 
        total += (i**2) / math.factorial(i)
    return total

def even_series_sum(n):
    total = 0
    for i in range(2, 2*n+1, 2):
        total += (i**2) / math.factorial(i)
    return total

terms = int(input("Enter the number of terms: "))

odd_sum = odd_series_sum(terms)
even_sum = even_series_sum(terms)

print(f"Sum of Odd Series: {odd_sum}")
print(f"Sum of Even Series: {even_sum}")