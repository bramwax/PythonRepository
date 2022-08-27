bit = 8                 # >> Bit length...
mag = 2**(bit -1)-1     # >> Integer range...
cnv = ""                # >> Binary conversion...

# >> Validate integer entered by user...
int_in = int(input(f"Enter an integer between {mag * -1} and {mag}: "))
while int_in > mag or int_in < mag * -1:
    print("-" * 60)
    int_in = int(input(f"Integer must be between {mag * -1} and {mag}: "))    

# >> Create positive copy of integer input...
if int_in < 0:
    int_cp = int_in * -1
else:
    int_cp = int_in

# >> Convert to binary...
while int_cp > 0:
    cnv = str(int_cp % 2) + cnv
    int_cp //= 2

# >> pad with zeros
while len(cnv) < bit:
    cnv = "0" + cnv

# >> If integer entered was positive print binary number, else convert to 2s compliment and print
if int_in < 0:
    # >> Convert to 1s compliment (flip digits)
    one_cmp = ""
    for digit in cnv:
        if digit == '1':
            one_cmp += '0'
        else:
            one_cmp += '1'
    # >> Convert to 2s compliment by adding 1 >> cnv = format(int(one_cmp, 2) + 1, 'b')
    add = '0' * (bit - 1) + '1'
    car = 0
    two_cmp = ''
    for i in range(len(cnv)-1, -1, -1):
        tmp_tot = car + int(add[i]) + int(one_cmp[i])
        if tmp_tot == 3:
            two_cmp = '1' + two_cmp
            car = 1
        elif tmp_tot == 2:
            two_cmp = '0' + two_cmp
            car = 1
        elif tmp_tot == 1:
            two_cmp = '1' + two_cmp
            car = 0
        else:
            two_cmp = '0' + two_cmp
            car = 0
    cnv = two_cmp

print('=' * 60)
print('The integer', int_in, 'in binary 2s compliment is', cnv)
