import random

def import_data(filename):
    file = open(filename, encoding="utf8")
    dta = []
    for i in file:
      dta.append(i.replace("\n","")) # replace() enables invisble EOL character to be removed
    file.close()
    return dta

def validate_pwd(password):

    # -- Check if password is the correct length
    if len(password) != 12:
        return False

    # -- Assess digit distribution
    up, lw, nm, sy = 0, 0, 0, 0
    for i in password:
        if i.isupper():
            up += 1
        elif i.islower():
            lw += 1
        elif i.isdigit():
            nm += 1
        else:
            sy += 1

    # -- Check digit distribution
    if (nm > 0 and lw > 0 and up > 0 and sy > 0):
        return True
    else:
        return False

def generate_pwd():

    # -- Characters imported from external file...
    all_chars = import_data('chars.txt')

    # -- Pots are created enabling selection of first four symbols, one from each pot
    num_pot =    all_chars[:10]
    chr_pot_up = all_chars[10:36]
    chr_pot_lw = all_chars[36:62]
    chr_pot_gr = all_chars[len(all_chars)-62:] # Len function used to locatre start position
    avl_pos =    [0,1,2,3,4,5,6,7,8,9,10,11]
    new_pwd = ['','','','','','','','','','','','']

    iterator = len(avl_pos) - 1
    count = 4 # Count is used to control the first 4 symbols selected
    while iterator >= 0:
      tmp_pos = avl_pos[random.randint(0, iterator)]
      if count == 4:
        new_pwd[tmp_pos] = num_pot[random.randint(0,len(num_pot)-1)]
      elif count == 3:
        new_pwd[tmp_pos] = chr_pot_up[random.randint(0,len(chr_pot_up)-1)]
      elif count == 2:
        new_pwd[tmp_pos] = chr_pot_lw[random.randint(0,len(chr_pot_lw)-1)]
      elif count == 1:
        new_pwd[tmp_pos] = chr_pot_gr[random.randint(0,len(chr_pot_gr)-1)]
      else:
        new_pwd[tmp_pos] = all_chars[random.randint(0,len(all_chars)-1)]

##      match count:
##        case 4:
##            new_pwd[tmp_pos] = num_pot[random.randint(0,len(num_pot)-1)]
##        case 3:
##            new_pwd[tmp_pos] = chr_pot_up[random.randint(0,len(chr_pot_up)-1)]
##        case 2:
##            new_pwd[tmp_pos] = chr_pot_lw[random.randint(0,len(chr_pot_lw)-1)]
##        case 1:
##            new_pwd[tmp_pos] = chr_pot_gr[random.randint(0,len(chr_pot_gr)-1)]
##        case _:
##            new_pwd[tmp_pos] = all_chars[random.randint(0,len(all_chars)-1)]

      count -= 1
      avl_pos.remove(tmp_pos)
      iterator -= 1

    return ''.join(new_pwd)


def validate_eml(email):
    
    # --------------------------------------------------------------------- >> base data <<
    # Break email parameter into chunks: recipient; sub_domain; top_level domain 
    rcp = email[0:email.find('@')]
    sdm = email[email.find('@')+1:email.find('.')]
    tpd = email.replace(rcp + '@' + sdm, '')
    
    # Import domains from file: https://tld-list.com/tlds-from-a-z)
    dms = import_data('domains.txt')

    # Valid characters: https://www.w3resource.com/javascript/form/email-validation.php
    rcp_vch = "!#$%&'*+-/=?^_`{|}~"

    # ---------------------------------------------------------------------- >> validate <<
    vld = True
    err = ''

    # -- >> Test top_level domain exists
    if tpd not in dms:
        err = 'Top_level domain not recognised'
        vld = False

    #-- >> Test sub_domain length
    if len(sdm) > 253:
        err = 'Sub_domain exceeds 253 characters'
        vld = False

    #-- >> Test sub_domain only contains dash character
    for c in sdm:
        if not(c.islower() or c.isupper() or c.isdigit() or c == '-'):
            err = 'Sub_domain contains invalid characters'
            vld = False
            
    #-- >> Test recipient length and start and end characters
    if len(rcp) > 64:
        err = 'Recipient exceeds 64 characters'
        vld = False
    elif not(rcp[0].islower() or rcp[0].isupper() or rcp[0].isdigit()) or \
         not(rcp[-1].islower() or rcp[-1].isupper() or rcp[-1].isdigit()):
        err = 'Recipient cannot begin or end with a symbol'
        vld = False

    # -- >> Test recipient contains correct characters, which do not appear consecutively
    lst_chr = ''
    for c in rcp:
        if not(c.islower() or c.isupper() or c.isdigit() or c in rcp_vch):
            err = 'Recipient contains invalid characters'
            vld = False
        elif c in rcp_vch and c == lst_chr:
            err = 'Recipient cannot contain consecutive characters'
            vld = False            
        lst_chr = c

    return {vld, err}
