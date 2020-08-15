import hashlib


def hash_password(string: str) -> str:
  '''
    Inputs:
      password -> str a string to be hashed
    Output:
      returns a hashed string (using sha1 algorithm) in uppercase
  '''
  password_hashed = hashlib.sha1(string.encode('utf-8')).hexdigest()
  return password_hashed.upper()
