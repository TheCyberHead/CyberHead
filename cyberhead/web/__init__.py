from os import system, chdir, environ
from dirsync import sync


def module_to_web(module_path)
    '''sync the web folder from a module
    to their respective folder on web/src'''

    source_path = environ.get('CH_PATH') + module_path + '/web/
    target_path = environ.get('CH_PATH') + '/web/src/modules' + module_path
    sync(source_path, target_path, 'sync')

def yarn_start():
    chdir(environ.get('CH_PATH') + '/web')
    system('yarn install')
    system('yarn start')


def make_menu(menu, imports, route):
    '''create the menu elements based on the modules'''
    chdir(environ.get('CH_PATH') + '/web/src')
    menu_flag = '{/* Automated Menu */}'
    imports_flag = '// Automated Import //'
    route_flag = '{/* Automated Route */}'

    with open('App.js', 'r+') as code:
        c = code.read()
        txt2 = c.split(menu_flag)
        txt3 = txt2[0] + menu_flag + str(menu) + menu_flag + txt2[2]
        txt4 = txt3.split(imports_flag)
        txt5 = txt4[0] + imports_flag + str(imports) + imports_flag + txt4[2]
        txt6 = txt5.split(route_flag)
        txt7 = txt6[0] + route_flag + str(route) + route_flag + txt6[2]
        code.seek(0)
        code.truncate()
        code.write(txt7)
        #print(txt7)


def collect_menu(modules):
    menu = ''
    imports = ''
    route = ''
    for module in modules:
        print(module)
        installModule(module)
        print('files moved')
        chdir(environ.get('CH_PATH') + '/modules/' + module)
        try:
            with open('menu.html', 'r') as code:
                c = code.read()
                menu += '\n' + c + '\n'
                imports += "\nimport " + module + " from './modules/" + module + "'\n"
                route_middle = 'updateKey={this.updateMenuKey}/>\n</Route>\n'
                route += '\n<Route exact path="/{}">\n  <{} '.format(module, module) + route_middle
            print('Menu added from:', module)
        except:
            print('Menu not founded in:', module)
    return menu, imports, route




def install_module(module):
    chdir(environ.get('CH_PATH') + '/modules/' + module)
    system('cp ' + module + '.js ../../web/src/modules/' + module + '.js')
    chdir(environ.get('CH_PATH') + '/modules/' + module + '/actions')
    system('cp * ../../../web/src/modules/actions')


def start_web():
    '''launch the web service'''
    return


def start(modules):
    menu, imports, route = collectMenu(modules)
    makeMenu(menu, imports, route)
    yarnStart()
    return


#environ['CH_PATH'] = '/home/sebu/CyberHead'
#start(['datasets'])
