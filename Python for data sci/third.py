#3. Write a Python program to count the occurrences of each word in a given sentence.
str1="My name is hussain and my hobby is coding"
str2=str1.split()
words={}

for word in str2:
    word.lower()
    words[word]=words.get(word,0)+1

print("Word occurrences :")
for word,count in words.items():
    print(word, ":", count)

