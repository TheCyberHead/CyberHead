from os import environ, chdir, listdir, path, system
from threading import Timer
from termcolor import colored
# from celery import Celery

import web


RUNNING = colored('RUNNING', 'green')
FAILED = colored('FAILED', 'red')


print(colored('CYBERHEAD CORE STARTING...\n', 'green'))
# process_queue = Celery('core', broker="amqp://localhost//")
# process_queue = Celery(__name__)
# process_queue.config_from_object(__name__)


# @process_queue.task
def run(parent, module):
    if parent != '':
        parent = parent + '.' + parent + '.'

    exec('from modules.' + parent + module + ' import start', globals())
    module_answer, callback_timing = start()

    if module_answer == 'Submodules called':
        modules_path = environ.get('CH_PATH') + '/modules/' + module + '/' + module
        parent = module
        initialize_modules(parent, modules_path)

    print(f'[{module}]', RUNNING, f'{module_answer}')

    if callback_timing > 0:
        Timer(callback_timing, run, [module]).start()
        print(f'[{module}]', RUNNING, f'callback: {callback_timing} seconds')
    else:
        print(f'[{module}]', RUNNING, f'no callback')


def initialize_modules(parent, modules_path):
    chdir(modules_path)
    modules = [folder for folder in listdir(".") if path.isdir(folder)]
    for module in modules:
        try:
            if module != '__pycache__':
                run(parent, module)
        except Exception as err:
            print(f'[{module}]', FAILED, f'{err}')
    return modules


def initialize_web(modules):
    try:
        web.start(modules)
        print('[WEB]', RUNNING)
    except Exception as err:
        print('[WEB]', FAILED)
        print(err)

    while True:
        web_request = input('>>>')
        try:
            run(web_request)
            print('[WEB REQUEST]', RUNNING)
        except Exception as err:
            print('[WEB REQUEST]', FAILED)
            print(err)


if __name__ == '__main__':
    modules_path = environ.get('CH_PATH') + '/modules'
    modules = initialize_modules('', modules_path)
    # initialize_web(modules)
