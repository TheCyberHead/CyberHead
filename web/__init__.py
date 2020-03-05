from os import system, chdir, environ


def yarnStart():
    chdir(environ.get('CH_PATH') + '/web')
    system('yarn install')
    system('yarn start')

def makeMenu(menu):
    '''create the menu elements based on the modules'''
    chdir(environ.get('CH_PATH') + '/web/src')
    with open('App.js', 'r+') as code:
        c = code.read()
        flag = '{/* Automated Menu */}'
        txt = c.split(flag)
        txt2 = txt[0] + flag + str(menu) + flag + txt[2]
        code.seek(0)
        code.truncate()
        code.write(txt2)
        print(txt2)

def collectMenu(modules):
    menu = ''
    for module in modules:
        print(module)
        chdir(environ.get('CH_PATH') + '/modules/' + module)
        try:
            with open('menu.html', 'r') as code:
                c = code.read()
                menu += '\n' + c + '\n'
            print('Menu added from:', module)
        except:
            print('Menu not founded in:', module)
    return menu


def startWeb():
    '''launch the web service'''
    return


def start(modules):
    menu = collectMenu(modules)
    makeMenu(menu)
    yarnStart()
    return

environ['CH_PATH'] = '/home/sebu/CyberHead'
start(['strategies'])
