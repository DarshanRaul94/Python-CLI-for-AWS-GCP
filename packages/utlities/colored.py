
"""
This module will be utilized for using the colored dialogue that are used for showing warnings and other important instructiosn
"""



from termcolor import colored, cprint

def coloredtext(input):
    text = colored(str(input), 'red', attrs=['reverse', 'blink'])
    print(text)

