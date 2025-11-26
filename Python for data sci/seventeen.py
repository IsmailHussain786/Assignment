# Counting the frequencies in a list using a dictionary in Python. Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
# # Expected output : 1 : 5 , 2 

import random
list1=[random.randint(1,10) for _ in range(7)]
print(list1)

def counting(arr):
    dic={}
    runs=len(arr)
    for i in arr:
        dic[i]=dic.get(i,0)+1
    return dic

print(counting(list1))