

""" check common letters in two input strings"""
common_letters=[]

s1=input("Input string one:")

s2=input("Input string two:")

l1=set(s1)
print(l1)
l2=set(s2)
print(l2)
for l in l1: 
    if l in l2:
        common_letters.append(l)
print (common_letters)

# sample from book

s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)