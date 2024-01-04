def to_bin(arg):
    try:
        int_num = int(arg)                                      # Convert number parameter to integer and assign to variable 'int_num'
        bin_num = ''                                            # Create empty string and assign to variable 'bin_num'
        while int_num > 0:                                      # Continue to repeat conversion process until 'int_num' reaches zero
            bin_num = str(int_num % 2) + bin_num                # >> Calculate binary bit (modulo integer by 2) and concatenate to 'bin_num'
            int_num //= 2                                       # >> Recalulate 'int_num' (integer division by 2)
        return bin_num
    except ValueError:
        pass


def to_base(arg1, arg2):
    try:
        int_num = int(arg1)                                     # Convert number parameter to integer and assign to variable 'int_num'
        int_base = int(arg2)                                    # Convert base parameter to integer and assign to variable 'int_base'

        lookup = '0123456789ABCDEF'                             # Create string of characters (up to base 16) and assign to variable lookup
        new_num = ''                                            # Create empty string and assign to variable 'new_num'
        while int_num > 0:                                      # Continue to repeat conversion process until 'int_num' reaches zero
            new_num = lookup[int_num % int_base] + new_num      #   >> Calculate index of character in 'lookup' (modulo integer by 'int_base') and concatenate to 'new_num'
            int_num //= int_base                                #   >> Recalulate 'int_num' (integer division by 'int_base')
        return new_num
    except ValueError:
        pass


def base_base(arg1, arg2, arg3):
    try:
        ba_fr = int(arg1)                                       # Convert arg1 (base from) to INTEGER and assign to variable 'ba_fr'
        nu_in = int(arg2, ba_fr)                                # Convert arg2 (number to be converted) to INTEGER, using 'ba_fr', and assign to variable 'nu_in'
        ba_to = int(arg3)                                       # Convert arg3 (base to) to INTEGER and assign to variable 'ba_to'

        if ba_to == 10:                                         # IF converting to base-10
            return nu_in                                        #   >> Return converted integer stored in variable 'nu_in'
        
        else:                                                   # ELSE begin conversion process
            ba_lk = '0123456789ABCDEF'                          #   >> Create string containing lookup characters (up to base-16) and assign to variable 'ba_lk'
            nw_nu = ''                                          #   >> Create empty string and assign to variable 'nw_nu'
            while nu_in > 0:                                    #   >> REPEAT UNTIL 'nu_in' reaches zero
                nw_nu = ba_lk[nu_in % ba_to] + nw_nu            #       >> Calculate index of character in 'ba_lk' (modulo 'nu_in' by 'ba_to') and concatenate to 'nw_nu'
                nu_in //= ba_to                                 #       >> Recalulate 'int_num' (integer division by 'int_base_to')
            return nw_nu                                        #       >> Return converted integer stored in variable 'nu_in'
    except ValueError:    
        pass


##print(to_bin('29'))
##print(to_base('29','16'))
##print(base_base('16','1D','10'))
