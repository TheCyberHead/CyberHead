from os import path, system
system('pip3 install -r /app/cyberhead/requirements.txt')


import yaml
import git
from shutil import rmtree, copytree


def read_compose(file):
    with open(file) as compose_file:
        compose = yaml.load(compose_file, Loader=yaml.FullLoader)
        return compose


def copy_folder(source, destination):
    if path.exists(destination):
        rmtree(destination)
    copytree(source, destination)
    print(f'[COPIED] from:{source} to:{destination}')


def clone_repo(source, destination):
    rm_folder = destination + source.split('/')[-1]
    if path.exists(rm_folder):
        rmtree(rm_folder)

    fixed_source = 'https://' + source.split('//')[-1]
    git.Git(destination).clone(fixed_source)
    print(f'[CLONED] from:{source} to:{destination}')


def transfer_modules(modules):
    for module_key, module in modules.items():
        if 'dir' in module:
            source = module['dir']
            destination = f'/app/cyberhead/{module_key}'
            copy_folder(source, destination)
        elif 'git' in module:
            source = submodule['git']
            destination = f'/app/cyberhead/'
            clone_repo(source, destination)

        for submodule_key, submodule in module.items():
            if submodule_key != 'dir':
                if 'dir' in submodule:
                    source = submodule['dir']
                    destination = f'/app/cyberhead/{module_key}/{submodule_key}'
                    copy_folder(source, destination)
                elif 'git' in submodule:
                    source = submodule['git']
                    destination = f'/app/cyberhead/{module_key}/'
                    clone_repo(source, destination)


def build(file):
    compose = read_compose(file)
    transfer_modules(compose['modules'])
    system('pip3 install .')


if __name__=='__main__':
    build('/app/cyberhead-compose.yml')
