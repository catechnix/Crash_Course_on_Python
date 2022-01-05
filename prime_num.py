#Write a Python Program to Check if a Number is a Prime Number?

num=int(input("Input a number:\n"))

num_list=[]
for i in range(2, num):
    if num%i == 0:
        num_list.append(i)

if len(num_list) >=1:
    print("{} is not a Prime number".format(num))
else:
    print("{} is a Prime number".format(num))