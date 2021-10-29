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

    
def cat(file_directory):
    if file_directory[0] !='/':
        file_directory = current_dir + file_directory

    file_sub_system = zipfile.Path(archieve_path, at = file_directory[1:])
    if file_sub_system.is_file() and file_sub_system.exists():
        print(file_sub_system.read_text())
    else:
        print('Wrong directory')


def ls():
    object_list = list(
        zipfile.Path(
            archieve_path,
            at = current_dir[1:]
        ).iterdir
    )
    print(
        *list(
            map(
                operator.attrgetter('name'),
                object_list
            )
        )
    )


#def pwd():


def main():
    user_input = input('%s@%s %s >>> ' % ('root', host_name, current_dir)).split()

    input_size = len(user_input)
    if input_size == 0:
        return

    if input_size == 1 and user_input[0] == 'help':
        help()
    elif input_size == 1 and user_input[0] == 'exit':
        sys.exit(0)
    elif input_size == 1 and user_input[0] == 'pwd':
        print(current_dir)
    elif input_size == 1 and user_input[0] == 'ls':
        ls()
    elif input_size == 2 and user_input[0] == 'cd':
        cd(user_input[1])
    elif input_size == 2 and user_input[0] == 'cat':
        cat(user_input[1])
    else:
        print('\nWrong input. Check syntax or command list\n')





if __name__ == '__main__':
    print('''
    Welcome to Vshell Emulator 0.0-a
    Made by Andrey Komarov
    These shell commands are defined internally. Type 'help' to see this list.
    ''')
    while True:
        main()