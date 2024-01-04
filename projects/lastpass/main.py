import random
import credentials as crd

# >> ====== CLASS Definition: Stores users
class Lastpass:

  def __init__(self):
    self.users = []

  def insert_user(self, user):
    self.users.append(user)

  def get_users(self):
    return self.users


# >> ====== CLASS definition: Stores username & password
class User():

  def __init__(self, username, password):
    self.username = username
    self.password = password

  def get_username(self):
    return self.username

  def get_password(self):
    return self.password

  def set_password(self, password):
    None

## >> ==================== Code starts executing from this point ====================
## >> -------------------------------------------------------------------------------

# 1) Create instance of class Last_pass
# 2) Create instance of class User
# 3) Store new user in lst_pass object
lst_pass = Lastpass()

usr_nme = 'riley@dm.com'
new_pwd = crd.generate_pwd()
new_user = User(usr_nme, new_pwd)

lst_pass.insert_user(new_user)
all_users = lst_pass.get_users()

for i in all_users:
  print(f'Username: {i.get_username()} \nPassword: {i.get_password()}')
