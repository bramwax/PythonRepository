'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
Answer: 142913828922
'''

# Brute force... 10 hours
'''
prm_lmt = 2000000
sum_prm = 0
num = 2
while num < prm_lmt:
  is_prm = True
  for i in range(2, num - 1):
    if num % i == 0:
      is_prm = False
      break
  if is_prm:
    sum_prm += num
  num += 1
print(sum_prm)
'''

# Remove evens above 2... still running
'''
prm_lmt = 2000000
sum_prm = 2
num = 3
while num < prm_lmt:
  is_prm = True
  for i in range(2, num - 1):
    if num % i == 0:
      is_prm = False
      break
  if is_prm:
    sum_prm += num
  num += 2
print(sum_prm)
'''
  
# Sieve of Eratosthenes... seconds
'''
def sumPrimes(n):
    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum

print(sumPrimes(2000000))
'''
