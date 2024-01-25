'''
A file has been intercepted by one of our agents. We know it has been encrypted using a caesar cipher (shift unknown) and that it contains details of a meeting. We need you to write an algorithm that will import the file (ciphertext.txt), decode the message, and save it to another file called plaintext.txt. We have provided you with everything we have... GOOD LUCK!!
'''

def strip_linebreak(string):
  if len(string) > 1:
    if string[-1] == '\n':
      return string [:-1]
  
  return string
  
def txt_to_string(filename):
  file = open(filename)
  txt = ""
  for line in file:
    txt += strip_linebreak(line)
  file.close()
  return txt

def string_to_file(filename, string):
  file = open(filename, 'a')
  file.write(string)
  file.close()
  
def decipher(char_set, cipher_text, shift):
  message = ""
  for a in range(0, len(cipher_text)):
    index = 0
    while cipher_text[a] != char_set[index]:
      index += 1

    index = index + shift
    if index >= len(char_set):
      index = index - len(char_set)
      
    message += char_set[index]
  return message


char_set = txt_to_string('ascii_chars.txt')
cipher_text = txt_to_string('ciphertext.txt')

# for shift in range(215):
#   message = decipher(char_set, cipher_text, shift)
#   print(shift, "|", message, "\n")

message = decipher(char_set, cipher_text, 18)
string_to_file('plaintext.txt', message)
