from colorama import Fore;
import os

print();
config=input(Fore.BLUE+'Press Enter to continue to raspi-config or any other key to skip it for now: ')

if config:
    print('You can setup later with'+Fore.MAGENTA+' raspi-config')
else:
    os.system('raspi-config')
