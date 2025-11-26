#5Write a Python program to add 'ing' at the end of a given string
#(length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead 
# If the string length of the given string is less than 3, leave it unchanged

str1="I am playing cricket"
str2=str1.split()
result=[]
for word in str2:
    if len(word)<3:
        result.append(word)
    elif word.endswith("ing"):
        result.append(word+"ly")
    else:
        result.append(word+"ing")

final=" ".join(result)
print(final)






# str2=str1.split()
# str3=[]
# for word in str2:
#     if word.endswith("ing"):
#         str3.append(word+"ly")
#         continue
#     str3.append(word+"ing")

# final=" ".join(str3)
# print(final)