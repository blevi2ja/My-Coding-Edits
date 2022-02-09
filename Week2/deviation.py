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
max_length = 1000; upper_bound=1000000
A = generate_random_int_list(max_length, upper_bound)

B = generate_random_int_list(max_length, upper_bound)

numintA = len(A)
numintB = len(B)
averageA = 0
averageB = 0
totalA = 0
totalB = 0
i = 0
j = 0
sumA = 0
sumB = 0
standarddevA = 0
standarddevB = 0
for val in A:
    totalA += val
    averageA = totalA/numintA
    while i < len(A):
        sumA += (A[i] - averageA)*(A[i] - averageA)
        i += 1
        standarddevA = (sumA/numintA)** (1/2)

for val in B:
    totalB += val
    averageB = totalB/numintB
    while j < len(B):
        sumB += (B[j] - averageB)*(B[j] - averageB)
        j += 1
        standarddevB = (sumB/numintB)** (1/2)
print('The standard deviation of A is ' + str(standarddevA))
print('The standard deviation of B is ' + str(standarddevB))
if standarddevA > standarddevB:
    print('The standard deviation in list A is greater than B')
else:
    print('The standard deviation in list B is greater than A')