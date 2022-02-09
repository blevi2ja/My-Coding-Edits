from cmath import inf
import math


def calculate_pi(desired_error):

    """This functions takes in the desired error and estimates pi until the desired error is reached

    Args:
        desired_error (float): the desired error is the difference between actual pi and estimated pi

    Returns:
        pie(the estimation of pi): Once the desired error is reached it returns the estimated value of pi
    """
    a = 1
    b = 1/(2**(1/2))
    t = 1/4
    p = 1
    i = 1
    while i <= inf:
        an = (a + b)/2
        bn = (a*b)**(1/2)
        tn = t - p * ((a - an)**2)
        pn = 2*p
        pie = ((an + bn)**2)/(4*tn)
        a = an
        b = bn
        p = pn
        t = tn
        i += 1
        if (math.pi - pie) < desired_error:
            print('number of times pie estimated '+str(i))
            return pie

# main (body) here to call your function. Do not modify below this line
desired_error = 1E-10

approximation = calculate_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")