def is_prime(number):
    """
        Parameter: number (integer or float)
        Return: Boolean (True or False)
        Description: 
            1) Return False if parameter is (below 2, non-integers, even numbers other than
            2) Loop through every odd number below the parameter (3, 5, 7, etc):
                 Return False if: parameter mod(number) == 0
            3) Return True if parameter is not rejected by steps 1 and 2...
        Pseudocode: 
    
    """
    if number < 2 or (number % 2 == 0 and number != 2) or number % 1 != 0:
        return False
    else:
        divisor = 3
        while count < number:
            if number % count == 0:
                return False
            count += 2
    return True

for i in range(-5,100):
    if is_prime(i):
        print(i, "is Prime!")