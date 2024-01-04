# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder. What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

div_limit = 20
number = div_limit

while number > 1:
  count = 0
  for i in range(1, div_limit + 1):
    if number % i != 0:
      break
    else:
      count += 1
  if count == div_limit:
    break
  else:
    number += 1
print(number)
