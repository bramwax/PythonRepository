# The sum of the squares of the first ten natural numbers is 385.
# The square of the sum of the first ten natural numbers is 3025.
# Difference between the sum of the squares and the square of the sum is 2640.
# ----------------------------------------------------------------------------
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sums.

rge = 100
sum_squ = 0
squ_sum = 0
for i in range(1, rge + 1):
  sum_squ += i ** 2
  squ_sum += i
squ_sum = squ_sum ** 2

print(squ_sum - sum_squ)