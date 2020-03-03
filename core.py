from celery import Celery
from threading import Timer
from os import walk


print('CYBERHEAD CORE STARTING...\n')
#process_queue = Celery('core', broker="amqp://localhost//")
#process_queue = Celery(__name__)
#process_queue.config_from_object(__name__)

#@process_queue.task
def run(module):
    try:
        exec('from modules.' + module + ' import start', globals())
        timing = start()

        #to rabbitmq
        Timer(10, run, [module]).start()

        print(module, '\033[32mRUNNING\033[39m')
        print(timing, 'seconds to callback')
    except:
        print(module, '\033[31mFAILED\033[39m')


def initializeModules():
    for (dirpath, modules, filenames) in walk('./modules'):
        for module in modules:
            run(module)


def initializeWebService():
    print('Starting Web Service')
    while True:
        web_request = input('>>>')
        try:
            run(web_request)
        except:
            print('\033[31mWEB REQUEST FAILED\033[39m')

initializeModules()
initializeWebService()
