'''Write a Python program to find the first appearance of the substring 
'not' and'poor' from a given string, if 'not' follows the 'poor',
replace the whole 'not'...'poor' substring with 'good'. Return the resulting string'''

str="The movie started off well, but the acting was not very poor and the storyline dragged on for hours, making it hard to stay focused on the screen."

print(str.find("abc"))
index_not=str.find("not")
index_poor=str.find("poor")

if index_not != -1 and index_poor != -1 and index_not<index_poor:
    text=str[:index_not] + "good" + str[index_poor+4:]

print(text)
# if str.find("not"):
#     while str!="poor":
