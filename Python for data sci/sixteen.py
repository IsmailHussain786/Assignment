# 15.Given a number n, write a python program to make and print the list of Fibonacci
# series up to n. Input : n=7 Hint : first 7 numbers in the series Expected output :
# First few Fibonacci numbers are 0, 1, 1, 2, 

a=int(input("Enter the number :"))
print(a)

def fibonacci(a):
    if a < 2:
        print("Invalid Number of Terms ")
        return
    first,second=0,1
    print(first,second,end=" ")
    for i in range(2, a):
        next_num=first+second
        print(next_num, end=" ")
        first,second=second,next_num

fibonacci(a)
