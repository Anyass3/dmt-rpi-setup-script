from colorama import Fore
import re

content="""
[Unit]
Description=PulseAudio system server
[Service]
ExecStart=/usr/bin/pulseaudio --system --realtime --disallow-exit --no-cpu-limit
[Install]
WantedBy=multi-user.target
"""
try:
    with open('/etc/systemd/system/pulseaudio.service','x') as f:
        f.write(content)
except:
    print('pulseaudio service already exists')


with open('/etc/pulse/client.conf') as f:
    content=f.read()
    content=content.replace('; autospawn = yes','autospawn = no')
with open('/etc/pulse/client.conf','w') as f:
    f.write(content)


with open('/etc/pulse/default.pa') as f:
    content=f.read()
    content=content.replace('load-module module-suspend-on-idle','#load-module module-suspend-on-idle')
with open('/etc/pulse/default.pa','w') as f:
    f.write(content)


with open('/etc/pulse/system.pa') as f:
    content=f.read()
    content = re.sub(r'load-module module-native-protocol-unix.*\n','load-module module-native-protocol-unix auth-anonymous=true\n' , content)
with open('/etc/pulse/system.pa','w') as f:
    f.write(content)