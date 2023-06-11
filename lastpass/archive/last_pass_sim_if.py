import random

def import_data(filename):
  file = open(filename)
  tmp_container = []
  for i in file:
    tmp_container.append(i.replace("\n",""))
  file.close()
  return tmp_container

# >> ------------------------ Main program starts here
all_chars = import_data('chars.txt')

# >> ------ create pots
num_pot =    all_chars[:10]
chr_pot_up = all_chars[10:36]
chr_pot_lw = all_chars[36:62]
chr_pot_gr =    all_chars[len(all_chars)-62:]
avl_pos =    [0,1,2,3,4,5,6,7,8,9,10,11]

new_pwd = ['','','','','','','','','','','','']
iterator = len(avl_pos) - 1
count = 4
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

print(''.join(new_pwd))
