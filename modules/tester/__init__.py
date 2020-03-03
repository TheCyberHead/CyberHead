from time import sleep
import os


def stuff():
    '''do the specific module stuff'''
    print('doing the tester stuff')
    os.system('ping google.com')


def start():
    stuff()
    return 3


if __name__ == '__main__':
    start()
