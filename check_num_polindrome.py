#Write a Python Program to Check if a Number is a Palindrome or not?

num=input("Input a number:\n")

if len((num))%2 !=0:
    num_list=[int(x) for x in num]
    print(num_list)

    i=0
    tn=len(num)
    mp=tn//2
    l=list()
    for i in range(0,mp):
        if num_list[i] == num_list[-(i+1)]:
            l.append("true")
            

    if len(l) == mp:
        print ("{} is palindrome number".format(num))
    else:
        print ("{} is not palindrome number".format(num))


def is_pal(n):
    try:
        val=int(n)
        print("{} is a number\n".format(val))

    except ValueError:
        print("{} is a not number\n".format(n))

    n_l=[int(x) for x in str(n)]
    print(n_l)
    new_n_l=n_l
    new_n_l.reverse()
    print(new_n_l)

    for i in n_l:
        for j in new_n_l:
            if i == j:
                i +=1
                j +=1
            else:
                print("{} is not palindrome".format(n))
    print("{} is palindrome".format(n))

is_pal(13841)

