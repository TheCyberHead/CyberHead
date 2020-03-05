from os import environ, chdir, listdir, path
from threading import Timer
# from celery import Celery

import web


print('CYBERHEAD CORE STARTING...\n')
environ['CH_PATH'] = '/home/sebu/CyberHead'
# process_queue = Celery('core', broker="amqp://localhost//")
# process_queue = Celery(__name__)
# process_queue.config_from_object(__name__)


# @process_queue.task
def run(module):
    try:
        exec('from modules.' + module + ' import start', globals())
        timing = start()

        Timer(timing, run, [module]).start()

        print(module, '\033[32mRUNNING\033[39m')
        print(timing, 'seconds to callback')
    except:
        print(module, '\033[31mFAILED\033[39m')


def initializeModules():
    chdir(environ.get('CH_PATH') + '/modules')
    modules = [folder for folder in listdir(".") if path.isdir(folder)]
    for module in modules:
        run(module)
    return modules


def initializeWebService(modules):
    print('Starting Web Service')
    web.start(modules)
    while True:
        web_request = input('>>>')
        try:
            run(web_request)
        except:
            print('\033[31mWEB REQUEST FAILED\033[39m')


modules_list = initializeModules()
initializeWebService(modules_list)
