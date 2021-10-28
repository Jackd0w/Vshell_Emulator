import sys
import zipfile
import operator

def help():
    print('''
    List of available commands:
            help - print information
            exit - exit
            pwd - print working directory
            ls - list files
            cd - change directory
            cat - concatenate
    ''')





if __name__ == '__main__':
    print('''
    Welcome to Vshell Emulator 0.0-a
    Made by Andrey Komarov
    These shell commands are defined internally. Type 'help' to see this list.
    ''')

    help()