"""Write a python program that promts user for input of a hex number, could be
0x12345678, 12345678h or just 12345678. Print out the number in decima and binary
and count the number of bit sets in the result"""

import os, sys, traceback

try:
    user_input = input('Enter the number in hex: ')

    if (user_input[-1].lower() == 'h'):
        user_input = user_input[:-1]

    try:
        n = int(user_input, 16)
    except ValueError:
        print("Input " + user_input + " cannot be recognized as a hex number. Program terminating...")
        os._exit(-1);

    print("Number in decimal: {}".format(n))    ## number has been converted successfully, no need to check for ValueError
    binary_string = bin(n)                      ## like wise
    print("Number in binary: {}".format(binary_string))

    count = 0
    for bit in binary_string:
        if bit == '1':
            count += 1

    print("Number of bit sets: {}".format(count))
except Exception:
    print("Uh oh, something's wrong, please let the monkey know\n")
    print(sys.exc_info()[0])
    os._exit(-2)        ##Will always exit without traceback and ok debug info
