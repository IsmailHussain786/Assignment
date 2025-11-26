# 14.Write a Python program to find the highest 3 values in a dictionary.


my_dict = {"apple": 10,"banana": 30,"cherry": 20,"mango": 40}

my_dict=dict(sorted(my_dict.items(),key=lambda item:item[1], reverse=True))

print(my_dict)

sliced=dict(list(my_dict.items())[0:3])
print(sliced)
