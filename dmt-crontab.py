from crontab import CronTab
from colorama import Fore;

cron = CronTab(user='root')

command="bash -ic ~/.dmt/etc/onboot/onboot"

is_active=[j for j in list(cron) if j.command==command]

if not is_active:
    job = cron.new(command=command)
    job.every_reboot()
    cron.write()
    print(Fore.GREEN+'DMT @reboot crontab enabled')
else:
    print(Fore.LIGHTBLACK_EX+'DMT @reboot crontab already enabled')