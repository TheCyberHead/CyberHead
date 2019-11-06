import os
import subprocess
import psutil
import schedule


IB_PROCESS = 'java'
ENTRY_POINT="/home/ubuntu/Jts/ibgateway/972/ibgateway"

for proc in psutil.process_iter():
    if proc.name() == IB_PROCESS:
        proc.kill()


def start_gateway():
	username = "username={}".format(os.getenv('IB_USERNAME'))
	password = "password={}".format(os.getenv('IB_PASSWORD'))
	line_execution = "{} {} {}".format(ENTRY_POINT, username, password)
	subprocess.Popen(line_execution, shell=True)


def check_running():
	if IB_PROCESS not in list(map(lambda x: x.name(), psutil.process_iter())):
		start_gateway()

def persist():
    schedule.every(10).seconds.do(check_running)
    while True:
	    schedule.run_pending()

if __name__ == '__main__':
    persist()
