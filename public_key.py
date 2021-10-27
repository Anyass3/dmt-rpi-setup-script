from colorama import Fore
import os

path=os.path.join(os.environ.get('HOME'),'.ssh/authorized_keys')
with open(path,'a') as ak:
  p_key=input(Fore.BLUE+'Enter public authorized key: ')
  if p_key:
      ak.write('\n\n'+p_key)