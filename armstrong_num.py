# Write a Python Program to Check if a Number is an Armstrong Number?

from typing import List


num=(input("Input a number:\n"))
sum_num=0


num_list=[int(x) for x in num ]
print(num_list)

num=int(num)
for i in num_list:
    sum_num += i*i*i

if sum_num == num:
    print("{} is a Armstrong Number".format(num))

n=int(input("Enter any number: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
print("The number is an armstrong number. ")
else:
print("The number isn't an arsmtrong number. ")