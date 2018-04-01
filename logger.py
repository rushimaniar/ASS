'''
Logger for writing pretty shit to the terminal. We mean business yo.
'''
from time import strftime, gmtime

'''
Status can be Warning, Error, Info
'''
WARN = 'warn'
ERROR = 'err'
INFO = 'info'
RED = '\033[31;1m'
YELLOW ='\033[33m' 
CYAN = '\033[36m'
WHITE = '\033[37;0m'
    

# General Log
def log(status, text):
    text = str(text)
    if status == 'err':
        print(RED + '[ ERROR ]\t' + text + WHITE)
    elif status == 'warn':
        print(YELLOW + '[ WARN ]\t' + text + WHITE)
    elif status == 'info':
        print(CYAN + '[ INFO ]\t' + text + WHITE)
    else:
        print(text)
    return

# Camera Log
def clog(status, camera, text):
    text = str(text)
    camera = str(camera)
    if status == 'err':
        print(RED + '[ ' + camera + '\t]\t' + text + WHITE)
    elif status == 'warn':
        print(YELLOW + '[ ' + camera + '\t]\t' + text + WHITE)
    elif status == 'info':
        print(CYAN + '[ ' + camera + '\t]\t' + text + WHITE)
    else:
        print(text)