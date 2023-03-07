def prime_num_generator():
    """
    This function is a generator that yields prime numbers one by one on each iteration.
    """
    primes = []  # list to store the prime numbers found so far
    n = 2        # start checking for primes from 2
    
    while True:
        is_prime = True
        
        # check if n is divisible by any of the primes found so far
        for p in primes:
            if n % p == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(n)  # n is a prime, add it to the list
            yield n          # yield the prime number
            
        n += 1   # check the next number for primality
        # create a generator object
gen = prime_num_generator()

# print the first 10 prime numbers
for i in range(10):
    print(next(gen))