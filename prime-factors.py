def get_factors(x):
    factors = []
    for num in range(2, x + 1):
        if num == 0: continue
        if x % num == 0:
            factors.append(num)
    
    return factors

def is_prime(x):
    for num in range(2, x):
        print 
        if x % num == 0:
            return False
    
    return True

def prime_factors(x):
    prime_factors = []
    factors = get_factors(x)
    for factor in factors:
        if is_prime(factor):
            prime_factors.append(factor)
    
    return prime_factors

print("""Prime Factors:
What is your number?""")
num = int(input())

print(prime_factors(num))
        