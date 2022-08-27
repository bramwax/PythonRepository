# Listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10,001st prime number?

p_count = 0
p_target = 2
p_high = 2

while p_count < 10001:
  prime = True
  for i in range(2, p_target):
    if p_target % i == 0:
      prime = False
      break
  if prime:
    p_count += 1
    p_high = p_target
  
  p_target += 1

print(p_high)