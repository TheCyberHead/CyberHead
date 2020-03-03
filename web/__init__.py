from os import system, chdir


path = '/home/sebu/CyberHead'
def yarnInstall():
    chdir(path + '/web')
    system('yarn install')
    system('yarn start')
    chdir('/home/CyberHead')
    return

def makeMenu(modules):
    '''create the menu elements based on the modules'''
    print(modules)
    return


def startWeb():
    '''launch the web service'''
    return


def start(modules):
    makeMenu(modules)
    yarnInstall()
    return
