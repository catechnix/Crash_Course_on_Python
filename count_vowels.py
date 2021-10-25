# Write a Python Program to Count the Number of Vowels in a String?

#vowels=["a","e","i","o","u"]

s=input("Input a string:")

d_v={"a":0,"e":0,"i":0,"o":0,"u":0}  #init dict's key and value
print(d_v)


for c in s:
    if c in d_v.keys():
        d_v[c] +=1
    
print (d_v)
