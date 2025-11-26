# 11.Write a Python program to unzip a list of tuples into individual lists.

lists=[(1, 'a'), (2, 'b'), (3, 'c')]
list1,list2=zip(*lists)
# * is use for unziping

list1=list(list1)
list2=list(list2)

print("First list is ", list1)
print("Second list is ",list2)

