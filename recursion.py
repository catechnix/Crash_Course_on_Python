def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

def count_users(group):
  count = 0
  for member in get_members(group):
    #count +=1
    if is_group(member):
      count += count_users(member)
    else:
      count +=1

  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18

def sum_positive_numbers(n):
  
  if n>0:
    n +=sum_positive_numbers(n-1)
  return n
print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15