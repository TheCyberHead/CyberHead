from time import sleep


def stuff():
    '''do the specific module stuff'''
    print('doing the tester stuff')


def start():
    stuff()
    return 3


if __name__ == '__main__':
    start()
