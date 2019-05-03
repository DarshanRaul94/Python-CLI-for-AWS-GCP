from termcolor import colored, cprint
from progress.bar import FillingCirclesBar
import sys 
from time import sleep

def progressbar(title):
    # for i in range(21):
    #     sys.stdout.write('\r')
    #     # the exact output you're looking for:
    #     sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
    #     sys.stdout.flush()
    #     sleep(0.05)
    text = colored(str(title), 'red', attrs=['reverse', 'blink'])
    print(text)
    bar = FillingCirclesBar('Processing', max=100)
    for i in range(100):
        # Do some work
        sleep(0.025)
        bar.next()
    bar.finish()