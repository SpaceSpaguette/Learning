import os, sys, time, colorama
from colorama import Fore, Style

def intro():
    colorama.init(autoreset=True)
    text = Fore.YELLOW + "Loading" + Style.RESET_ALL
    for x in range(20):
        for y in range(4):
            print(text + "." * y + " " * (3 - y), end="\r")
            time.sleep(0.4)
            sys.stdout.flush()

os.system('cls')
intro()
