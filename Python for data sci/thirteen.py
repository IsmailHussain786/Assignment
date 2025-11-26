# 13.Write a Python program to sort a dictionary (ascending /descending) by value

my_dict = {"apple": 10,"banana": 30,"cherry": 20,"mango": 40}

print(my_dict)

my_dict=dict(sorted(my_dict.items(), key=lambda item: item[1],reverse=True))

print("Ascending:", my_dict)