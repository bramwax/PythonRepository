
import math

# Helper functions...
# ========================================
def to_base(number, num_base):
    
    lookup = "0123456789ABCDEF"
    tmp_num = ""
    while number > 0:
        tmp_num = lookup[number % num_base] + tmp_num
        number = number // num_base
    return tmp_num


# 001 | Enter a number...
# ========================================
def get_number():

    """
    Parameters: None
    Returns: A number (float or Integer)

    Description:
        1) Outputs message to command line asking user to enter a number.
        2) User enters a number as a string.
        3) An attempt is made to convert number to a float...

           IF successful: Float value is cast to integer and compared (1.0 == 0)...
                          >> If they are the same an integer returned
                          >> If not, a float is returned
           If unsuccesful: An error message is displayed and the user is asked to enter a number.
           
           N.B. A WHILE loop ensures that this process continues until the user eneters the correct value.
    """
    
    while True:
        userInput = input("\n001 | Enter number: ")
        try:
            n = float(userInput)
            if int(n) == n:
                return int(n)
            else:
                return n
        except:
            print("Not a number! Try again.")

### Basic Properties of Numbers (Introductory Level)
# --------------------------------------------------
# 002 | Is it an integer number? A whole number that can be positive, negative, or zero, and does not include fractions or decimals.
def is_integer(number):
    if number % 1 == 0:
        return True
    return False

# 003 | Is it a floating-point number? A number that includes a decimal point, representing a fractional or whole value.
def is_float(number):
    if number % 1 > 0:
        return True
    return False

# 004 | What is the scale of the number? The number of digits to the right of the decimal point.
def scale(number):
    if is_float(number):
        return len(str(number).split(".")[1])
    return 0

# 005 | What is the sign of the number? Whether a number is positive (+), negative (-), or neutral (0).
def sign(number):
    if number == 0:
        return "Neutral (0)"
    elif number > 0:
        return "Positive (+)"
    else:
        return "Negative (-)"

# 006 | Is it zero? A neutral number that represents the absence of quantity or value.
def is_zero(number):
    if number == 0:
        return True
    return False

# 007 | Is it a positive number? A number greater than zero
def is_positive(number):
    if number > 0:
        return True
    return False

# 008 | Is it a negative number? A number less than zero
def is_negative(number):
    if number < 0:
        return True
    return False

### Simple Mathematical Properties (Intermediate Level)
# -----------------------------------------------------
# 009 | Is it an even number? An integer number divisible by 2
def is_even(number):
    if number % 2 == 0:
        return True
    return False

# 010 | Is it an odd number? An integer not divisible by 2
def is_odd(number):
    if is_integer(number) and number % 2 > 0:
        return True
    return False

# 011 | Is it a prime number? A natural number that can only be divided evenly by 1 and itself
""" 
    Parameter: number (integer or float)
    Return: Boolean (True or False)
    Description:
        Step 1: If the number is less than 2, a decimal, or an even number (greater than 2), return False (not prime).
        Step 2: Test all numbers from 2 to one less than the input number. If any of them divide the input number without a remainder, return False (not prime).
        Step 3: If no divisors are found, return True (the number is prime).

    Pseudocode (OCR):
        function is_prime(number)
            if number < 2 OR (number % 2 == 0 AND number != 2) OR number % 1 != 0 then
                return false
            endif
            divisor = 2
            while divsor < number
                if number mod divsor == 0 then
                    return false
                endif
                divisor = divsor + 1
            endwhile
            return true
        end function
"""
def is_prime(number):
    if number < 2 or is_float(number) or (number > 2 and is_even(number)):
        return False
    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

# 012 | Is it a square number? A number that is the product of an integer multiplied by itself (2 x 2 = 4)
def is_square(number):
    if number < 0 or is_float(number):
        return False
    count = 0
    while count <= number:
        if count ** 2 == number:
            return True
        count += 1
    return False

# 013 | Is it a cube number? The result of multiplying a number by itself twice
def is_cube(number):
    if number < 0 or is_float(number):
        return False
    count = 1
    while count <= number:
        if count ** 3 == number:
            return True
        count += 1
    return False

# 014 | Is it a power of 2?
def is_power_two(number):
    if number < 0 or is_float(number):
        return False
    count = 1
    while count <= number:
        if 2 ** count == number:
            return True
        count += 1
    return False

# 015 | What is its binary representation?
def to_bin(number):
    if not is_integer(number):
        return None
    binary = "-0b"
    if not is_negative(number):
        binary = binary[1:]
    return binary + to_base(abs(number),2)

# 016 | What is its octal representation?
def to_oct(number):
    if not is_integer(number):
        return None
    oct = "-0o"
    if not is_negative(number):
        oct = oct[1:]
    return oct + to_base(abs(number),8)

# 017 | What is its hexadecimal representation?
def to_hex(number):
    if not is_integer(number):
        return None
    hex = "-0x"
    if not is_negative(number):
        hex = hex[1:]
    return hex + to_base(abs(number),16)

    # lookup = "0123456789ABCDEF"
    # bin = list(number)
    # hex = []
    # while len(bin) % 4 != 0:
    #     bin.insert(0,0)
    # two_power = 1
    # sum = 0
    # for index in range(len(bin)-1,-1,-1):
    #     if bin[index] == 1:
    #         sum += two_power
    #     two_power *= 2
    #     if two_power > 8:
    #         hex.insert(0,lookup[sum])
    #         two_power = 1
    #         sum = 0


# 018 | What is its Roman numeral equivalent?
def to_roman(number):
    glyphs = [['I','II','III','IV','V','VI','VII','VIII','IX'],       # one
              ['X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],       # ten
              ['C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],       # hun
              ['M','MM','MMM','IV̅','V̅','V̅I̅','V̅I̅I̅','V̅I̅I̅I̅','I̅X̅'],       # tho
              ['X̅','X̅X̅','X̅X̅X̅','X̅L̅','L̅','L̅X̅','L̅X̅X̅','L̅X̅X̅X̅','X̅C̅'],       # tth
              ['C̅','C̅C̅','C̅C̅C̅','C̅D̅','D̅','D̅C̅','D̅C̅C̅','D̅C̅C̅C̅','C̅M̅'],       # hth
              ['M̅','M̅M̅','M̅M̅M̅','M̅I̅V̅','M̅V̅','M̅V̅I̅','M̅V̅I̅I̅','M̅V̅I̅I̅I̅','M̅I̅X̅'], # mth
              ['I̿','I̿I̿','I̿I̿I̿','I̿V̿','V̿','V̿I̿','V̿I̿I̿','V̿I̿I̿I̿','I̿X̿']]       # bth
    roman =  ""
    for i in range(len(str(number))):
        dgt = number % 10
        if number % 10 > 0:
            roman = glyphs[i][dgt - 1] + roman
        number //= 10
    return roman

### Advanced Number Sequences and Patterns (Advanced Intermediate Level)
# ----------------------------------------------------------------------
# 019 | Is it a number in the Fibonacci sequence? A number in the sequence where each number is the sum of the two preceding ones, starting with 0 and 1
def is_fibonacci(number):
    if number < 0 or is_float(number):
        return False
    a,b = 0,1
    while a + b <= number:
        nxt = a + b
        if nxt == number:
            return True
        a,b = b,nxt
    return False

# 020 | Is it a triangular number?
def is_triangular(number):
    if number < 0 or is_float(number):
        return False
    count = 1
    sum = 0
    while count <= number:
        sum += count
        if sum == number:
            return True
        count += 1
    return False

# 021 | Is it a palindromic Number?
def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    return False

# 022 | Is it a happy number? ⚠️
def is_happy(number):
    newNums = []
    newNum = number
    while True:
        sum = 0
        while newNum > 0:
            sum += (newNum % 10) ** 2
            newNum //= 10
        newNum = sum
        if newNum == 1:
            return True
        elif newNum in newNums:
            return False
        newNums.append(newNum)

# 023 | Is it a Pythagorean triple? ⚠️
def is_triple(number):

    for a in range(2, number + 1):
        for b in range(a + 1, number + 1):

            # ---------- >> My first version... works but is slow
            # c = b + 1
            # while c < number ** 2:
            #     if a ** 2 + b ** 2 == c ** 2:
            #         print(a,b,c)
            #         if a == number or b == number or c == number:
            #             return True
            #     c += 1

            # ---------- >> ChatGPT: calculates c only for valid combinations of a and b
            c_sqd = a ** 2 + b ** 2
            c = int(math.sqrt(c_sqd))
            if c ** 2 == c_sqd:
                if a == number or b == number or c == number:
                    return True
    return False

# 024 | Is it part of a geometric sequence? ⚠️
def is_geometric(number):
    return "🚧"

### Factorization and Divisor Properties (Advanced Level)
# -------------------------------------------------------
# 025 | What are its factors? Numbers that divide into a given integer (whole) number exactly, leaving no remainder
def factors(number):
    tmp_array = []
    negative = 1
    if is_integer(number):
        if is_negative(number):
            negative = -1
        number *= negative
        divisor = 1
        while divisor <= number:
            if number % divisor == 0:
                tmp_array.append(divisor * negative)
            divisor += 1
    return tmp_array

# 026 | What are its prime factors? Prime numbers that divide a given number exactly without leaving a remainder
def prime_factors(number):
    tmp_factors = factors(number)
    tmp_prime_factors = []
    for factor in tmp_factors:
        if is_prime(factor):
            tmp_prime_factors.append(factor)
    return tmp_prime_factors

# 027 | What is the GCD of this number and another?
# 028 | What is its LCM with another number?
# 029 | Is it deficient, abundant, or perfect?
# 030 | Is it a highly composite number?

### Special Numbers and Complex Properties (Expert Level)
# ----------------------------------------
# 031 | Is it a perfect number?
# 032 | Is it an amicable number?
# 033 | Is it a Kaprekar number?
# 034 | Is it a factorial number?
# 035 | What is its digit sum?
# 036 | What is its multiplicative persistence?
