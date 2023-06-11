import random

# >> ============================== CLASS: Stores users; generate/validate 12-digit passwords
class Lastpass:

  # >> ---- When an instance is created, this function/code is executed
  def __init__(self):
    self.users = [] # class variable that stores objects of class User

  # >> ---- Returns valid 12-digit pwd (1 upper, 1 lower, 1 number, 1 symbol)
  def new_password(self):

    # -- Characters loaded from  external file... call class method
    file = open('chars.txt')
    all_chars = []
    for i in file:
      all_chars.append(i.replace("\n","")) # replace() enables invisble EOL character to be removed
    file.close()

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
      count -= 1
      avl_pos.remove(tmp_pos)
      iterator -= 1

    return ''.join(new_pwd)

  # >> ---- Returns true if pwd valid (12-dig, 1 upp, 1 low, 1 num, 1 sym), False otherwise
  def valdidate_pwd(self, password):
    # TBC
    None



# >> ============================== CLASS: Stores username & password
class User(Lastpass):

  def __init__(self, username, password):
    self.username = username
    self.password = password

  def get_username(self):
    return self.username

  def get_password(self):
    return

## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Code starts executing from this point @@
## ----------------------------------------------------------------------------------------------
lst_pass = Lastpass() # Creates instance of class Last_pass and places in variable
new_user = User('riley@dm.com','bl@ck1sbe5t')
print(new_user.new_password()) # Calls the class method, which returns a valid password
