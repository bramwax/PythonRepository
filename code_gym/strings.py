# 001 | Enter/load a string...
# ========================================
def get_string(filename=False):
    inp = input("\n001 | Enter text or filename (.txt): ")
    if inp[-4:] == ".txt":
        try:
            with open(inp, 'r') as file:
                return file.read()
        except IOError:
            return ""
    else:
        return inp


### Basic String Properties (Introductory Level)
# ----------------------------------------------
# 002 | Is it an empty string?
def is_empty(string):
    """Returns True if length of string parameter is zero, False otherwise"""
    return len(string) == 0

# 003 | What is the length of the string?
def get_length(string):
    count = 0
    for i in string:
        count += 1
    return count

# 004 | What is the first character of the string?
def first_char(string):
    if not is_empty(string):
        return string[0]
    return None

# 005 | What is the last character of the string?
def last_char(string):
    if not is_empty(string):
        return string[-1]
    return None

# 006 | Is the string alphabetic?
def is_alphabetic(string):
    if is_empty(string):
        return None
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string = string.upper()
    for char in string:
        valid = False
        for glyph in alphabet:
            if char == glyph:
                valid = True
                break
        if not valid:
            return False
    return True       

    # if string.isalpha():
    #     return True
    # return False

# 007 | Is the string numeric?
def is_numeric(string):
    try:
        strFloat = float(string)
        return True
    except:
        return False

# 008 | Is the string alphanumeric?
def is_alphanumeric(string):
    if is_empty(string):
        return None
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string = string.upper()
    for char in string:
        valid = False
        for glyph in alphabet:
            if char == glyph:
                valid = True
                break
        if not valid:
            return False
    return True

    # if string.isalnum():
    #     return True
    # return False

# 009 | Is the string lowercase?
def is_lower(string):
    if is_empty(string):
        return None
    length = get_length(string)
    lwr = "abcdefghijklmnopqrstuvwxyz"
    for char in string:
        for glyph in lwr:
            if char == glyph:
                length -= 1
    if length == 0:
        return True
    return False

# 010 | Is the string uppercase?
def is_upper(string):
    if is_empty(string):
        return None
    length = get_length(string)
    upr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in string:
        for glyph in upr:
            if char == glyph:
                length -= 1
    if length == 0:
        return True
    return False

# 011 | Is the string a palindrome?
def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False


### String Modifications (Intermediate Level)
# -------------------------------------------
# 012 | Convert the string to lowercase.
# 013 | Convert the string to uppercase.
# 014 | Capitalize the first letter of the string.
# 015 | Reverse the string.
# 016 | Remove leading and trailing whitespace.
# 017 | Replace all occurrences of a substring.
# 018 | Remove all occurrences of a substring.
# 019 | Split the string into a list based on a delimiter.
# 020 | Join a list of strings into a single string.
# 021 | Check if the string starts with a specific substring.
# 022 | Check if the string ends with a specific substring.
# 023 | Check if the string contains a specific substring.

### Advanced String Properties and Patterns (Advanced Level)
# ----------------------------------------------------------
# 024 | Is the string a valid email address?
# 025 | Is the string a valid URL?
# 026 | Does the string match a regular expression pattern?
# 027 | Extract all numbers from the string.
# 028 | Count the number of occurrences of a specific character.
# 029 | Count the number of occurrences of a specific substring.
# 030 | Find the index of the first occurrence of a substring.
# 031 | Find the index of the last occurrence of a substring.

### String Comparisons (Advanced Level)
# -------------------------------------
# 032 | Compare two strings for equality.
# 033 | Compare two strings lexicographically.
# 034 | Check if the string is lexicographically smaller than another.
# 035 | Check if the string is lexicographically greater than another.
# 036 | Check if the string matches a case-insensitive version of another string.

### String Encoding and Decoding (Expert Level)
# ---------------------------------------------
# 037 | Convert the string to its ASCII values.
# 038 | Convert ASCII values back to the string.
# 039 | Encode the string in base64.
# 040 | Decode a base64 encoded string.
# 041 | Encode the string in URL format.
# 042 | Decode a URL encoded string.