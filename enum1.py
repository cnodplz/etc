#!/usr/bin/python3

import sys

def verify(guess):
  vals = [ 
		130,
		154,
		136,
		252,
		131,
		157,
		155,
		137,
		252,
		227,
		226,
		228,
		233
  ] 

  if len(guess) != 13:
    return False

  for flagplz in vals:
    aa = flagplz ^ 209
    print("{}".format(chr(aa)), end='')
  print("")

  for i, c in enumerate(guess):
    if (ord(c) ^ 209) != vals[i]:
      return False 
  return True


if len(sys.argv) != 1:
  print('Usage: python check.pyc')
  exit(1)

#guess = input("Enter your guess for the flag: ");
guess = "NOT-GONA-8888"

if verify(guess):
  print("That's the correct flag!")
else:
  print("Wrong flag.")
