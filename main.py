import sys
import zipfile
import operator

try:
    archieve_path = argv[1]
    if not(zipfile.is_zipfile(archieve_path)):
        raise Exception()
except:
    raise Exception('No archive name given')



host_name = archieve_path.split('.')[0]
current_dir = '/'

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



def cd(next_dir):
    global current_dir
    tmp_dir = ''

    if next_dir == '..':
        cur_list = current_dir.split('/')
        cur_list = cur_list[1:len(cur_list) - 2]
        tmp_dir = '/'.join(cur_list)
        if tmp_dir == '':
            tmp_dir = '/'
        else:
            tmp_dir = '/' + tmp_dir + '/'

    else:
        if ('/' in next_dir):
            if (next_dir[-1] =='/'):
                tmp_dir = next_dir
            else:
                tmp_dir = next_dir + '/'
        else:
            tmp_dir = current_dir + next_dir + '/'



if __name__ == '__main__':
    print('''
    Welcome to Vshell Emulator 0.0-a
    Made by Andrey Komarov
    These shell commands are defined internally. Type 'help' to see this list.
    ''')

    help()