from math import sqrt

class Character:
  def __init__(self):
    self.xpos = 0
    self.ypos = 0

  # ------------------------ << set x & y position based on coordinates fed in
  def set_pos(self, coords):
    self.x_pos = coords[0]
    self.y_pos = coords[1]
    
  # ---------------------- << return tuple containing current x and y position
  def get_pos(self):
    return (self.x_pos, self.y_pos)


class Player(Character):
  def __init__(self):
    Character.__init__(self)
    self.set_pos((8,11))
    self.pts = 0


class Enemy(Character):
  def __init__(self, x_coord, y_coord):
    self.set_pos((x_coord,y_coord))
    self.l_mov = ''

  # ------------------------------------------------------ << calculate & move
  def nxt_mov(self, pl_pos):
    # -- << calculate moves based on the maze and no reversing
    safe_moves = ['a','-']
    moves = []
    if self.y_pos > 0 and mz[self.y_pos - 1][self.x_pos] in safe_moves and self.l_mov != 'S':
      moves.append(['N', self.x_pos, self.y_pos - 1])
    if self.x_pos < 28 and mz[self.y_pos][self.x_pos + 1] in safe_moves and self.l_mov != 'W':
      moves.append(['E', self.x_pos + 1, self.y_pos])
    if self.y_pos < 19 and mz[self.y_pos + 1][self.x_pos] in safe_moves and self.l_mov != 'N':
      moves.append(['S', self.x_pos, self.y_pos + 1])
    if self.x_pos > 0 and mz[self.y_pos][self.x_pos - 1] in safe_moves and self.l_mov != 'E':
      moves.append(['W', self.x_pos - 1, self.y_pos])
      
    # -- << if no moves are possible move back the way it came
    if len(moves) == 0:
      if   self.l_mov == 'S': moves.append(['N', self.x_pos, self.y_pos - 1])
      elif self.l_mov == 'W': moves.append(['E', self.x_pos + 1, self.y_pos])
      elif self.l_mov == 'N': moves.append(['S', self.x_pos, self.y_pos + 1])
      elif self.l_mov == 'E': moves.append(['W', self.x_pos - 1, self.y_pos])

    # -- << calculate the best mov using pythagorus theorum
    sht_dis = 999
    nxt_mov = ''
    
    for i in range(len(moves)):
      a = moves[i][1] - pl_pos[0]
      b = moves[i][2] - pl_pos[1]
      dis = round(sqrt(a**2 + b**2),2)
      
      if dis < sht_dis:
        sht_dis = dis
        nxt_mov = moves[i][0]

    if nxt_mov == 'N':
      self.l_mov = 'N'
      self.y_pos -= 1
    elif nxt_mov == 'E':
      self.l_mov = 'E'
      self.x_pos += 1
    elif nxt_mov == 'S':
      self.l_mov = 'S'
      self.y_pos += 1
    else:
      self.x_pos -= 1
      self.l_mov = 'W'

    print(nxt_mov, self.get_pos())
    

def load_maze(filename):
    file = open(filename)
    maze = []
    for x in file:
      tmp_array = []
      for char in x:
        if char != '\n':
          tmp_array.append(char)
      maze.append(tmp_array)
    return maze


# ========================================== >> main code starts here << ==
mz = load_maze("maze.txt")
pl = Player()
en = Enemy(22,3)
for i in range(30):
  en.nxt_mov(pl.get_pos())