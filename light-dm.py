import re
with open('/etc/lightdm/lightdm.conf') as f:
    content=f.read()
    content = re.sub(r'#?xserver-command=X.*\n','xserver-command=X -s 0 dpms -nocursor\n' , content)
with open('/etc/lightdm/lightdm.conf','w') as f:
    f.write(content)