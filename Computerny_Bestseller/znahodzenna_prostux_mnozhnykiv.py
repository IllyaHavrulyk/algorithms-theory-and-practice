import math

def findFactors(number):
      factors = set()
      if number % 2 == 0:
            factors.add(2)
            number = number / 2
      i = 3
      max_factor = math.sqrt(number)
      while(i <= max_factor):
            while(number % i == 0):
                  factors.add(i)
                  number = number / i
                  max_factor = math.sqrt(number)
            i = i + 2
      if number > 1:
            factors.add(number)
      return factors


print(str(findFactors(18)))
      