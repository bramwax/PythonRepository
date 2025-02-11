from nums import *
from strings import *

def main():

    string = get_string()
    print("002 | Empty:", is_empty(string))
    print("003 | Length:", get_length(string))
    print("004 | First character:", first_char(string))
    print("005 | Last character:", last_char(string))
    print("006 | Alphabetic:", is_alphabetic(string))
    print("007 | Numeric:", is_numeric(string))
    print("008 | Alphanumeric:", is_alphanumeric(string))
    print("009 | Lowercase:", is_lower(string))
    print("010 | Uppercase:", is_upper(string))
    print("011 | Palindrome:", is_palindrome(string))

    help(is_empty)

    number = get_number()
    # print("002 | Integer:", is_integer(number))
    # print("003 | Float:", is_float(number))
    # print("004 | Scale:", scale(number))
    # print("005 | Sign:", sign(number))
    # print("006 | Zero:", is_zero(number))
    # print("007 | Positive:", is_positive(number))
    # print("008 | Negative:", is_negative(number))
    # print("009 | Even:", is_even(number))
    # print("010 | Odd:", is_odd(number))
    print("011 | Prime:", is_prime(number))
    # print("012 | Square:", is_square(number))
    # print("013 | Cube:", is_cube(number))
    # print("014 | Power of 2:", is_power_two(number))
    # print("015 | Binary:", to_bin(number))
    # print("016 | Octal:", to_oct(number))    
    # print("017 | Hexadecimal:", to_hex(number))
    # print("018 | Roman numerals:", to_roman(number))
    # print("019 | Fibonacci:", is_fibonacci(number))
    # print("020 | Triagular:", is_triangular(number))
    # print("021 | Palindrome:", is_palindrome(number))
    # print("022 | Happy:", is_happy(number))
    # print("023 | Pythagorean triple:", is_triple(number))
    # print("024 | Geometric sequence:", is_geometric(number))   
    # print("025 | Factors:", factors(number))
    # print("026 | Prime factors:", prime_factors(number))

    print("\n")

if __name__ == "__main__":
    main()