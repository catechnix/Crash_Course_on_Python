#Write a Python Program to Count the Number of Digits in a Number?

num=input("Input a number:\n")

list_num=[int(x) for x in num]
print(list_num)

#count_num=sum(list_num)
#print(count_num)
count_num=len(list_num)
print(count_num)

