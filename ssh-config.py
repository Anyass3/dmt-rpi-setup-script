import re
with open('/etc/ssh/sshd_config') as f:
    content=f.read()
    content = re.sub(r'#PermitRootLogin Yes','PermitRootLogin Yes' , content)
    content = re.sub(r'#UseDNS no','UseDNS no' , content)
with open('/etc/ssh/sshd_config','w') as f:
    f.write(content)