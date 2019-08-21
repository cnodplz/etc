#!/usr/bin/env python
from string import ascii_uppercase
import subprocess

def main():

    a=0000
    b=9999
    c='AAAA'
    d='ZZZZ'
    e = [chr(i) for i in range(ord('A'),ord('Z')+1)]

    for y in range(0,26):
        for y1 in range(0,26):
            for y2 in range(0,26):
                for y3 in range(0,26):
                    for x in range(a,b):
                        f = "SKY-{}{}{}{}-{:04}".format(e[y],e[y1],e[y2],e[y3],x)
                        print(f)
                        #print("SKY-{}{}{}{}-{:04}".format(e[y],e[y1],e[y2],e[y3],x))
                        #var1 = subprocess.check_output(("root-x32", "key"))

main()
