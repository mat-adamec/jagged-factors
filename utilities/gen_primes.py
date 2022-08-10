import json
import itertools
from primefac import primefac

def unique(lst):
    ''' Returns only the unique values of a provided list. '''
    ulst = []
    for val in lst:
        if val not in ulst:
            ulst.append(val)
    return ulst

def factorizer(number):
    ''' Returns the prime factors of an input number. Uses an efficient library to do so. '''
    return list(primefac(number))

def higher_factors(number):
    ''' Returns other factors of an input number by using its prime factors. No repeats. '''
    # Catch base case of 0; everything is a divisor of it, but we return an empty array.
    if number == 0:
        return []
    primes = factorizer(number)
    # Generate all possible combinations of primes. Multiply them together. These are the divisors.
    divisors = [1]
    for i in range(1, len(primes)+1):
        # Get all combinations of length i.
        combos = list(itertools.combinations(primes, i))
        for combo in combos:
            multiple = 1
            for val in combo:
                multiple *= val
            combos[combos.index(combo)] = multiple
        divisors += combos
    return sorted(unique(divisors))
            
def writer(n, dir=''):
    ''' This function will write a json file of prime factors for the first n integers. '''
    # Catch invalid input
    if n < 2:
        return None
    else:
        results = {'prime_factors': [], 'unique_divisors': []}
        for i in range(n+1):
            results['prime_factors'].append(factorizer(i))
            results['unique_divisors'].append(higher_factors(i))
        with open(dir+'/prime_factors.json', 'w', encoding='utf-8') as file:
            json.dump(results, file, ensure_ascii=False, indent=4)