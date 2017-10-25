from hostswitcher.cli import cli
from hostswitcher.version import version
from hostswitcher.utils import os_resolver
from hostswitcher.utils.logger import logger
from hostswitcher.utils.file import *

import os

__version__ = version
__title__ = 'hostswitcher'

class Hostswitcher(object):
    
    title = '''
        ╦ ╦╔═╗╔═╗╔╦╗  ╔═╗╦ ╦╦╔╦╗╔═╗╦ ╦╔═╗╦═╗
        ╠═╣║ ║╚═╗ ║───╚═╗║║║║ ║ ║  ╠═╣║╣ ╠╦╝
        ╩ ╩╚═╝╚═╝ ╩   ╚═╝╚╩╝╩ ╩ ╚═╝╩ ╩╚═╝╩╚═
        '''

    log = logger()
    
    def __init__(self):
        self.__print_title()
        self.__custom_hosts_path()
        self.__start_cli()

    def __print_title(self):
        print(self.title)
        print('Version: %s' % (__version__))
        print('OS: %s' % (os_resolver()), end='\n\n')

    def __start_cli(self):
        self.cli = cli()
        self.args = self.cli.args()
    
    def __custom_hosts_path(self):

        homedir = os.path.expanduser("~")

        if os_resolver() == 'Windows':
            homedir += "\\AppData\\Roaming"

        self.custom_hosts_path = os.path.join(homedir,'.hostswitcher/hosts_files')
        create_path(self.custom_hosts_path)

    def run(self):
        import hostswitcher.lib.commands as commands
        
        class_ = getattr(commands, '%s_%s' % (self.args['command'], 'command'))
        
        cmd = class_(self.args)

def main():
    app = Hostswitcher()
    app.run()
