# bring in randomness cause we need it in our lives
import random


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars


# generate two random lists of integers
max_length = 100; upper_bound=1000000
nums = generate_random_int_list(max_length, upper_bound)

# see how long this list is
print("The list contains "+str(len(nums))+" values total.")

odd = 0
even = 0
i = 0
while i < len(nums):
    val = nums[i]
    val = val % 2
    i += 1
    if val == 0:
        even += 1
    else:
        odd += 1
percentodd = round((odd/i)*100)
percenteven = round((even/i)*100)
print('The number of odd numbers in the list is ' +str(odd))
print('The number of even numbers in the list is ' +str(even))
print('The percent of odd numbers in the list is ' +str(percentodd)+'%')
print('The percent of even numbers in the list is ' +str(percenteven)+'%')
