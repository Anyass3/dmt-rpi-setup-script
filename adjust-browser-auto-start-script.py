
import os

path=os.path.join('/home/pi','.config/lxsession/LXDE-pi/autostart')
string="""
@/usr/bin/chromium-browser --incognito --start-maximized --start-fullscreen --noerrdialogs --disable-translate --no-first-run --fast --fast-start --disable-infobars --disable-features=TranslateUI --overscroll-history-navigation=0 --disk-cache-dir=/dev/null --disable-pinch --force-tablet-mode --tablet-ui --kiosk http://localhost

@unclutter
@xset s off
@xset s noblank
@xset -dpms
"""
with open(path,'w') as user:
    user.write(string)
