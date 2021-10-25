# Write a Python Program to Find the Second Largest Number in a List

l1=list(input("input a list of number:\n"))
print(l1)

largest_num=max(l1)
print(largest_num)

l1.remove(largest_num)
second_largest_num=max(l1)
print(second_largest_num)

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
b=int(input("Enter element:"))
a.append(b)
a.sort()
print("Second largest element is:",a[n-2])
