#9. Write a Python program to find the second smallest number in a list.

def secondsmall(list1):
    unique_numbers = sorted(set(list1))
    if len(list1)<2:
        print("There is no second smallest number")
    else:
        print(unique_numbers[1])

list1=[12,25,56,4,23,50]
secondsmall(list1)