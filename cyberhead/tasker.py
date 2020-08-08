from threading import Timer
from termcolor import colored

from builder import read_compose


RUNNING = colored('RUNNING', 'green')
FAILED = colored('FAILED', 'red')

modules = read_compose('/app/cyberhead-compose.yml')['modules']


def start_module(start, callback_time):
    message, callback_time = start()
    timer = Timer(callback_time, start_module, [start, callback_time])
    timer.start()
    print(message, callback_time, start)


def start_modules():
    for module in modules:
        exec('from cyberhead.' + module + ' import start', globals())
        message, callback_time = start()
        start_module(start, callback_time)
        print(message, callback_time, start)


start_modules()
