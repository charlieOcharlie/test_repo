
# List given
nums = [12,345,2,6,7896,67,45,3,1,23,33,34,56]

# Print the even numbers
def find_even(list_given):
    print(len([n for n in nums if n%2==0]))

#find the odd numbers
def find_odd(list_given):
    print(len([n for n in nums if n%2==1]))

find_even(nums)

find_odd(nums)