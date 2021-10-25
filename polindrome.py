#  Write a Python Program to Check if a String is a Palindrome or Not?

s=input("Input a string:")
l=list()
if len(s)%2 !=0:
    i=1
    for c in s:

        if i<=len(s)//2 and c == s[-i]:
            i +=1
            l.append("true")
if len(l)==len(s)//2:
    print("Yes, the string is Palindrome\n")
else:
    print("No, the input string is not a Palindrome.\n")

string=input("Enter string:")
if(string==string[::-1]):
    print("The string is a palindrome")
else:
    print("The string isn't a palindrome")
    
