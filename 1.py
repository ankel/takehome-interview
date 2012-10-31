""" Write a python program that prompts the user for input and then answered
based on a given set of Q-A's. If Q not recognized then exit.
Program should work with Python 2.7 (it's witten in Python 3.2 though, may not
work with 2.7), free from traceback errors (it is).

Limitation: input is read case-sensitive."""

import os, sys, traceback

responds = {'Red'  : 'Blue',
            'Blue' : 'Green',
            'Green': 'White',
            'White': 'Black',
            'Black': 'Pink'}  ##list of expected q's and respective a's

while True:
    try:
        user_input = input('Enter the word: ');
        print("The magic eight ball says " + responds[user_input]);
        
    except KeyError:
        print("Answer not found, program terminating...")
        os._exit(0)         ##normal termination
        
    except KeyboardInterrupt:
        print("That's not fair, program terminating...")
        os._exit(-1)        ##Ctrl-C ???
        
    except:
        print("Uh oh, something's wrong, please let the monkeys know\n")
        print(sys.exc_info()[0])
        os._exit(-2)        ##Will always exit without traceback and ok debug info
