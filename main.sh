#!/usr/bin/env bash

python3 -c "from colorama import Fore;print();print(Fore.GREEN+'logging in as root\n');"
sudo su

python3 -m ssh-config
systemctl restart ssh

##

mkdir -p ~/.ssh
touch ~/.ssh/authorized_keys
python3 -m public_key

python3 -m setup-pi


python3 -c "from colorama import Fore;print();print(Fore.CYAN+'🌀 Installing linux packages');"
sleep 1
sudo apt-get update
sudo apt-get -y install build-essential tar unzip curl git screen ntp zip tree lsof colordiff rsync net-tools cmake arp-scan netcat nmon highlight evtest iperf iperf3 jq mosquitto mosquitto-clients socat


python3 -c "from colorama import Fore;print();print(Fore.CYAN+'🌀 INSTALLING node.js ENVIRONMENT');"
curl -L https://git.io/n-install | bash

python3 -c "from colorama import Fore;print();print(Fore.CYAN+'Fixing arp-scan issue');"
sleep 1
chmod u+s /usr/bin/arp-scan
chmod u+s /usr/sbin/arp-scan

python3 -c "from colorama import Fore;print();print(Fore.CYAN+'removing Avahi-daemon which is the frequent source of networking issues.');"
sleep 1
sudo apt-get -y remove avahi-daemon

python3 -c "from colorama import Fore;print();print(Fore.MAGENTA+'🌀 INSTALLING DMT from unippath');"
git clone https://github.com/uniqpath/dmt.git ~/.dmt
cd ~/.dmt
./install

cd -


python3 -c "from colorama import Fore;print();print(Fore.CYAN+'Added syntax hightlighting for .def files in nano');"
ln -s ~/.dmt/etc/syntax/nano/def.nanorc /usr/share/nano/def.nanorc
python3 -c "from colorama import Fore;print();print(Fore.CYAN+'Configure user.def for full shell');"
python3 -m dmt-user

python3 -c "from colorama import Fore;print();print(Fore.CYAN+'choose your default editor');"
sleep 1
update-alternatives --config editor

python3 -c "from colorama import Fore;print();print(Fore.CYAN+'🌀 Installing python-crontab to setup dmt @reboot crontab');"
sleep 1
apt install python3-pip
pip3 install python-crontab
python3 -m dmt-crontab


python3 -c "from colorama import Fore;print();print(Fore.CYAN+'KIOSK MODE SETUP\n🌀 Installing chromium-browser packages');"
sleep 1
apt-get install -y chromium-browser ttf-mscorefonts-installer unclutter x11-xserver-utils xdotool
python3 -m light-dm


python3 -c "from colorama import Fore;print();print(Fore.CYAN+'🌀 Installing and setting up pulseaudio');"
sleep 1
apt-get install -y pulseaudio
python3 -m pulse-audio-setup
systemctl enable pulseaudio
systemctl start pulseaudio

exit

python3 -c "from colorama import Fore;print();print(Fore.CYAN+'Adjusting autostart script for browser');"
mkdir -p ~/.config/lxsession/LXDE-pi
python3 -m adjust-browser-auto-start-script

python3 -c "from colorama import Fore;print();print(Fore.BLUE+'restarting pi...');"
sleep 1
shut r