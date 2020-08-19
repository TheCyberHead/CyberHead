import argparse
from sys import argv
from os import system, environ

'''
environ['CH_REPO_PATH'] = '/home/ubuntu/cyberhead'
repo_path = environ['CH_REPO_PATH']
'''

repo_path = '/home/ubuntu/cyberhead'
docker_path = f'{repo_path}/docker-compose.yml'
container_exec = f'docker-compose -f {docker_path} exec cyberhead'


def enter():
    '''open a terminal into the container'''
    system(f'{container_exec} bash')


def update():
    '''reinstall the wrapper outside the container'''
    system(f'pipx install {repo_path} --force')

def clean():
    system(f'{container_exec} python3 /app/cyberhead/cleaner.py')

def build():
    '''erase modules and build the package into de container'''
    update()
    clean()
    system(f'{container_exec} python3 /app/cyberhead/builder.py')


def dev():
    '''start the developer mode in te container'''
    build()
    system(f'{container_exec} python3 /app/cyberhead/tasker.py')


def run():
    '''run cyberhead in te container'''
    system(f'{container_exec} python3 /app/cyberhead/tasker.py')


def cli():
    '''asd'''
    cmd = argv[1]
    if cmd == 'enter':
        enter()
    elif cmd == 'update':
        update()
    elif cmd == 'clean':
        clean()
    elif cmd == 'build':
        build()
    elif cmd == 'dev':
        dev()
    elif cmd == 'run':
        run()
    elif cmd == '--help' or cmd or cmd == 'help':
        print('No written help yet, please read wrapper.py')
    else:
        print('Command not found, use --help for the commands list')
