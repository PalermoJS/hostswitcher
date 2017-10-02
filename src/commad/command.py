"""Command."""
from src.logger.logger import logger
from src.commad.action.init_action import init_action
from src.commad.action.create_action import create_action
from src.commad.action.list_action import list_action
from src.commad.action.edit_action import edit_action
from src.commad.action.set_action import set_action
from src.commad.action.remove_action import remove_action


log = logger()

description = """
Usage: main.py [OPTIONS]

  Host-switcher

Options:
  --init           set current hosts file default hosts file
  --create         create new hosts file by current hosts file
  --createby       create new hosts file from selected file
  --edit           edit hosts file
  --set            set hosts file
  --list           list of hosts files
  --remove         remove custom hosts files
  --help           Show this message and exit.
"""


def command(func):
    def getArgs(self, arg):
        try:
            log.log_info('Command cli start')
            func = getattr(function, arg[1][2:])
            func()
        except Exception as e:
            log.log_warning(e)
            function.help()
    return getArgs


class function:

    def help():
        print(description)

    def init():
        init_a = init_action()
        init_r = init_a.copy_current_host_file()
        if init_r is True:
            print('* Copy current hosts file')
        else:
            print('* No copy current hosts file')

    def create():
        create_a = create_action()
        create_r = create_a.create_new_file_by_current()
        if create_r is True:
            print('* Create new hosts file')
        else:
            print('* No create new hosts file')

    def createby():
        create_a = create_action()
        create_r = create_a.create_new_file_by_select()
        if create_r is True:
            print('* Create by new hosts file')
        else:
            print('* No create by new hosts file')

    def edit():
        edit_a = edit_action()
        edit_a.edit_file()
        print('Edit complete')

    def set():
        set_a = set_action()
        set_r = set_a.set_file()
        if set_r is True:
            print('* Set new hosts file')
        else:
            print('* No set hosts file')

    def list():
        list_a = list_action()
        lof = list_a.list_of_file()
        lof = list_a.in_use(lof)
        for file_name in lof:
            print(file_name)

    def remove():
        remove_a = remove_action()
        remove_a.remove_file()
        print('remove complete')
