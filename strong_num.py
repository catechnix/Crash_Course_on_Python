# Python Program to Check if a Number is a Strong Number:

num=(input("Input a number:\n"))

num_list=list(num)
print(num_list)
int(num)
sum_num_factor=0
for i in num_list:
    sum_num_factor += i*i
if sum_num_factor==num:
    print ("The input number is strong number.\n")

