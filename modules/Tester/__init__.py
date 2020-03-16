from time import sleep
import os


def stuff():
    '''do the specific module stuff'''
    print('doing the tester stuff')
    os.system('ping google.com -c 4')


def start():
    stuff()
    return 100


if __name__ == '__main__':
    start()
