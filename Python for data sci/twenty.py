# 19.Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

list1=[1,2,3,4,5,6,1,2]
def uniquee(arr):
    lists=list(set(arr))
    return lists

print(uniquee(list1))