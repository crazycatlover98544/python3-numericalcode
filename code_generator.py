#!/usr/bin/env python3
'''
Copyright (c) 2026 crazycatlover98544

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

You may also read these terms at the following website: https://opensource.org/license/mit

My GitHub account is located at https://github.com/crazycatlover98544
My MistWarp account is located at https://mistwarp.org/users/crazycatlover98544

Please note that this code is not written by an expert.
I am not responsible if this harms your computer.
I am also not responsible if you put something in here and it is decoded by someone else.

THIS PROGRAM HAS NOT BEEN FULLY TESTED WITH MANY STRINGS. AS THUS, SOME CODES MAY NOT WORK. IF YOU FIND SOMETHING THAT DOES NOT WORK, YOU MAY REPORT IT IN THE ISSUES PAGE OF THE GITHUB REPOSITORY YOU DOWNLOADED THIS FROM.
THE GENERATED STRINGS MAY NOT BE FULLY SECURE. I DO NOT KNOW; I AM NOT AN ENCRYPTION EXPERT.
'''

import ascii_json
import time
import sys

_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
             'o','p','q','r','s','t','u','v','w','x','y','z',' ','0',
             '1','2','3','4','5','6','7','8','9','0','.',',','!','@',
             '#','$','%','^','&','*','(',')','-','_','+','=','/','?'] # Used for the Caesar cipher

version = '0.0.1-alpha'
version_list = [0,0,1,'alpha'] # Allow you to compare stuff like major versions easily, without the string

def _caesarcipher(caestring,distance):
    pushed = []
    generated_alphabet = []
    output = ''
    for item in _alphabet:
        if _alphabet.index(item) + distance < 0:
            pushed.append(item)
            continue
        else:
            if _alphabet.index(item) + distance >= len(_alphabet):
                pushed.append(item)
                continue
            else:
                generated_alphabet.append(item)
    if distance < 0:
        generated_alphabet.extend(pushed)
    else:
        generated_alphabet = pushed + generated_alphabet
    del pushed
    for letter in caestring:
        try:
            output += generated_alphabet[_alphabet.index(letter)]
        except ValueError:
            output += generated_alphabet[_alphabet.index('?')] # Fallback
    return output

def _asciinumber(ascstring):
    numbers = []
    for item in ascstring:
        numbers.append(ascii_json.translation.get(item,0x3f)) # 0x3f is ascii for "?"
    return numbers

def _asciistring(binlist):
    string = ''
    for item in binlist:
        string += ascii_json.numbertext.get(str(item),'?')
    return string

def _multiplyencode(numblist):
    possiblenumbers = [1.3456635,1.345663,1.34566,1.3456,1.345,1.34,1.3,369,368,354,241,167,82,25,8,2] # If one is lossy, switch to a different one
    number = 2
    returnnumber = 0
    for item in numblist:
        try:
            number = int(f'{number}4{format(item,"08b")}')
        except ValueError as e:
            sys.stderr.write('Error in helper function "_multiplyencode": String entered too large. Full traceback: "{e}".')
            sys.exit(1)
    number = int(f'{number}43')
    nc_index = 0 # originally possiblenumbers was named something different; that is why this is nc_index and not pn_index
    
    while True:
        if nc_index >= len(possiblenumbers):
            sys.stderr.write('Error: No viable options for encoding.\n')
            sys.exit(1)
        else:
            try:
                returnnumber = number * possiblenumbers[nc_index]
            except OverflowError:
                nc_index += 1
                continue
            if (returnnumber // possiblenumbers[nc_index]) == number:
                break
            else:
                nc_index += 1
    return returnnumber

def _multiplydecode(string):
    possiblenumbers = [1.3456635,1.345663,1.34566,1.3456,1.345,1.34,1.3,369,368,354,241,167,82,25,8,2] # If one is lossy, switch to a different one
    numb = int(string)
    nc_index = 0
    
    while True:
        if nc_index >= len(possiblenumbers):
            return [False,[]]
        try:
            val_test = numb // possiblenumbers[nc_index]
        except OverflowError:
            val_test = 1234567890
        val_test_string = str(val_test)
        if '0' in val_test_string and '1' in val_test_string and '2' in val_test_string and '3' in val_test_string and '4' in val_test_string: # Technically, it would be possible to have a binary number that does not have 1 (0x00), but the ascii_json module has no reference for that.
            if '5' in val_test_string or '6' in val_test_string or '7' in val_test_string or '8' in val_test_string or '9' in val_test_string: # You thought there would not be any if statement longer than the last one; YOU ARE WRONG!!!
                pass
            else:
                if val_test_string[0] == '2' and val_test_string[-1] == '3':
                    val_test_string = val_test_string.replace('2','0').replace('3','0')
                    val_test_list = val_test_string.split('4')[1:-1] # [1:-1] is required because there will be a 24 at the beginning, and a 43 at the end
                    vtl_index = 0
                    for item in val_test_list:
                        val_test_list[vtl_index] = int(item,base=2)
                        vtl_index += 1
                    return [True,val_test_list]
                else:
                    pass
        else:
            pass
        nc_index += 1
    return [False,[]]

def encode(encstring):
    if encstring:
        cae = _caesarcipher(encstring,-7)
        asc = _asciinumber(cae)
        mul = _multiplyencode(asc)
        return [True,mul]
    else:
        return [False,0]

def decode(decstring):
    if decstring:
        mul = _multiplydecode(decstring)
        if mul[0]:
            asc = _asciistring(mul[1])
            cae = _caesarcipher(asc,7)
            if cae:
                return [True,cae]
            else:
                return [False,'']
        else:
            return [False,'']
    else:
        return [False,'']

if __name__ == '__main__': # Allow you to use this as a module
    arguments = sys.argv
    if '--encode' in arguments or '-e' in arguments:
        string = input('What do you want to encode?: ').lower() # Lowercase makes it easier on the caesar cipher
        if string:
            res = encode(string)
            if res[0]:
                print(f'Your code is {res[1]}.')
                time.sleep(0.1) # let it print to the console; I was having times where the code would not print because the program immediately exited
                sys.exit(0)
            else:
                sys.stderr.write('Error: Code generation failed; no extra information.\n')
                sys.exit(1)
        else:
            sys.stderr.write('Error: No string passed. Quitting...\n')
            sys.exit(1)
    elif '--decode' in arguments or '-d' in arguments:
        string = input('What do you want to decode?: ')
        if string:
            try:
                encoded_int = int(string)
            except ValueError:
                sys.stderr.write('Error: Expected a series of numbers; got string.\n')
                sys.exit(1)
            res = decode(encoded_int)
            if res[0]:
                print(f'Your string is "{res[1]}".')
                time.sleep(0.1) # let it print to the console; I was having times where the code would not print because the program immediately exited
                sys.exit(0)
            else:
                sys.stderr.write('Error: Code generation failed; no extra information.\n')
                sys.exit(1)
        else:
            sys.stderr.write('Error: No string passed. Quitting...\n')
            sys.exit(1)
    elif '--help' in arguments or '-h' in arguments:
        print(f'{arguments[0]} v{version} help:')
        print('\n  --encode, -e: Encode a string')
        print('  --decode, -d: Decode a series of numbers that was previously a string, and was encoded by this program or a compatible program')
        print('  --help, -h: Shows this help menu and exits')
        print('End of help')
        time.sleep(0.05) # Let the text print to display
        sys.exit(0)
    else:
        sys.stderr.write(f'{arguments[0]} v{version}: No arguments specified. For help, pass --help or -h.\n')
        sys.exit(1)