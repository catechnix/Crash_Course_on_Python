#Write a Python Program to Check if a Number is a Perfect Number?

num=int(input("Input a number:\n"))
sum=0

for i in range(1,num):
    if num%i == 0:
        sum +=i

if sum == num:
    print("{0} is perfect number.\n".format(num) )
