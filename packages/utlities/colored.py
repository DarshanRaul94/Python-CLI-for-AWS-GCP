from termcolor import colored, cprint

def coloredtext(input):
    text = colored(str(input), 'red', attrs=['reverse', 'blink'])
    print(text)

    