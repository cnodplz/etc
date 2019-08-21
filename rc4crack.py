#!/usr/bin/python
import base64

data = base64.b64decode("6fce38f8836e82d446c3af46eb3a945a97bb8088256751e47f73a02943883165")
# key = "<rc4 key>"

e = [chr(i) for i in range(ord('A'),ord('Z')+1)]
S = range(256)
j = 0
out = []

for y in range(0,26):
    for y1 in range(0,26):
        for y2 in range(0,26):
            for y3 in range(0,26):
                key = "{}{}{}{}".format(e[y],e[y1],e[y2],e[y3])
                #KSA Phase
                for i in range(256):
                    j = (j + S[i] + ord( key[i % len(key)] )) % 256
                    S[i] , S[j] = S[j] , S[i]
                #PRGA Phase
                i = j = 0
                for char in data:
                    i = ( i + 1 ) % 256
                    j = ( j + S[i] ) % 256
                    S[i] , S[j] = S[j] , S[i]
                    out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))
                print ''.join(out)
