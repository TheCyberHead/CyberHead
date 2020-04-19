
from sys import argv
from os import environ, chdir, listdir, path, system
from threading import Timer
from termcolor import colored
# from celery import Celery

# import web


RUNNING = colored('RUNNING', 'green')
FAILED = colored('FAILED', 'red')


# process_queue = Celery('core', broker="amqp://localhost//")
# process_queue = Celery(__name__)
# process_queue.config_from_object(__name__)


# @process_queue.task
def run_module(parent, module):
    module_have_parent = parent != ''
    if module_have_parent:
        added_path = parent + '.' + parent + '.'
    else:
        added_path = ''

    exec('from cyberhead.modules.' + added_path + module + ' import start', globals())
    module_answer, callback_timing = start()

    if module_answer == 'Submodules called':
        modules_path = environ.get('CH_PATH') + '/modules/' + module + '/' + module
        parent = module
        initialize_modules(parent, modules_path)

    print(f'[{module}]', RUNNING, f'{module_answer}')

    if callback_timing > 0:
        Timer(callback_timing, run_module, [module]).start()
        print(f'[{module}]', RUNNING, f'callback: {callback_timing} seconds')
    else:
        print(f'[{module}]', RUNNING, f'no callback')


def initialize_modules(parent, modules_path):
    '''If the module have submodules we use this same function
    on a submodule we need to know the parent module for the path'''

    chdir(modules_path)
    modules = [folder for folder in listdir(".") if path.isdir(folder)]
    for module in modules:
        try:
            if module != '__pycache__':
                run_module(parent, module)
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


def production():
    print(colored('CYBERHEAD CORE STARTING...\n', 'green'))


def development():
    print(colored('INSTALLING CYBERHEAD...\n', 'red'))
    chdir(environ.get('CH_PATH'))
    chdir('../')
    system('sudo python setup.py install')

    print(colored('CYBERHEAD CORE DEVELOPMENT MODE STARTING...\n', 'red'))
    modules_path = environ.get('CH_PATH') + '/modules'
    modules = initialize_modules('', modules_path)
    # initialize_web(modules)

    chdir(environ.get('CH_PATH') + '/web')
    #system('yarn install')
    #system('yarn start')


if __name__ == '__main__':
    if len(argv) < 2:  # no arg case
        production()
    elif argv[1] == 'dev':
        development()
    else:
        print(argv[0], 'command not found')

