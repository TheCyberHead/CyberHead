from os import environ, chdir, listdir, path
from threading import Timer
from termcolor import colored
# from celery import Celery


RUNNING = colored('RUNNING', 'green')
FAILED = colored('FAILED', 'red')


print('CYBERHEAD CORE STARTING...\n')
# process_queue = Celery('core', broker="amqp://localhost//")
# process_queue = Celery(__name__)
# process_queue.config_from_object(__name__)


# @process_queue.task
def run(module):
    try:
        exec('from strategies.' + module + ' import start', globals())
        timing = start()

        Timer(timing, run, [module]).start()

        print(f'[{module}]', RUNNING, f'callback: {timing} seconds')
    except Exception as err:
        print(f'[{module}]', FAILED)
        print(err)


def initialize_strategies():
    chdir(environ.get('CH_PATH') + '/modules/strategies/strategies')
    modules = [folder for folder in listdir(".") if path.isdir(folder)]
    for module in modules:
        run(module)
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
    modules = initialize_strategies()
    # initialize_web(modules)
