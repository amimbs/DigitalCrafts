# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math


def prime_fact(x):
    prime_factors = []
    divisor = 2
    #as soon as the advisor exceeds x, prime factorization is complete
    while divisor <= x:
        # any number divided by it's factor will have a remainder of 0
        if x % divisor == 0:
            # if we find the divisor is a factor of x, we want to add it to our list of prime_factors
            prime_factors.append(divisor)
            # update the value of x to x / it's factor
            x = x / divisor 
        else:
            divisor += 1 # divisior =  divisor + 1
    return prime_factors


(prime_fact(4))

largest_prime_factor = None
for n in  prime_factors:
    if n >largest_prime_factor: largest_prime_factor = n

print(n)
