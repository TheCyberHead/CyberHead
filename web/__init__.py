from os import system, chdir, environ


def yarnInstall():
    chdir(environ.get('CH_PATH') + '/web')
    system('yarn install')
    system('yarn start')
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
