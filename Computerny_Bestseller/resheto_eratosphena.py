import math

def findPrimes(max_number):
      is_composite = list(range(max_number + 1))
      for i in range(4, max_number, 2):
            is_composite[i] = True
      next_prime = int(3)
      stop_at =  int(math.sqrt(max_number))
      while(next_prime <= stop_at):
            for i in range(next_prime * 2, max_number, next_prime):
                  is_composite[next_prime] = True
            next_prime = next_prime + 2
            while(next_prime <= max_number and is_composite[next_prime] == True):
                  next_prime = next_prime + 2
      primes = []
      for i in range(2, max_number):
            if is_composite[i] == False:
                  primes.append(i)
      return primes

print(str(findPrimes(167)))