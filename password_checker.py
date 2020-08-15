import sys
import requests
from utils import hash_password


def check_pawned(password: str) -> int:
  '''
    Input:\n
      \tpassword - str a password to check in pawned password api \n
    Outputs:\n
      \t returns int of how many times the password is pawned and 0 if none \n
  '''
  hashed_pass = hash_password(password)
  first_five_char = hashed_pass[:5]
  remaining_char = hashed_pass[5:]
  try:
    res = requests.get(f'https://api.pwnedpasswords.com/range/{first_five_char}').text.splitlines()
    split_res = (line.split(':') for line in res)

    for h, count in split_res:
      if h == remaining_char:
        return count
    return 0
  except:
    return 'error'

def main(args):
  for password in args:
    count = check_pawned(password)
    if count == 'error':
      print('An error occurred check your network connection')
    if int(count) > 0:
      print(f'The passord "{password}" has been pawned {count} times. May be you should try another password')
    elif int(count) == 0:
      print(f'This is a good password to use. Carry On !!!')
  return 'Done!'

main(sys.argv[1:])
