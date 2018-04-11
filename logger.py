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
    
DEBUG = False
R_DEBUG = False
C_DEBUG = False


# General Log
def log(status, text):
    if DEBUG is False:
        return
    text = str(text)
    if status == 'err':
        print(RED + '[ ERROR\t]________' + text + WHITE)
    elif status == 'warn':
        print(YELLOW + '[ WARN\t]________' + text + WHITE)
    elif status == 'info':
        print(CYAN + '[ INFO\t]________' + text + WHITE)
    else:
        print(text)
    return

# Camera Log
def clog(status, camera, text):
    if C_DEBUG is False:
        return
    text = str(text)
    camera = str(camera)
    if status == 'err':
        print(RED + '[ ' + camera + '\t]________' + text + WHITE)
    elif status == 'warn':
        print(YELLOW + '[ ' + camera + '\t]________' + text + WHITE)
    elif status == 'info':
        print(CYAN + '[ ' + camera + '\t]________' + text + WHITE)
    else:
        print(text)

def rlog(status, camera, rule, text):
    if R_DEBUG is False:
        return
    text = str(text)
    camera = str(camera)
    if status == 'err':
        print(RED + '[ ' + camera + '\t]___[ ' + rule + '\t]___' + text + WHITE)
    elif status == 'warn':
        print(YELLOW + '[ ' + camera + '\t]___[ ' + rule + '\t]___' + text + WHITE)
    elif status == 'info':
        print(CYAN + '[ ' + camera + '\t]___[ ' + rule + '\t]___' + text + WHITE)
    else:
        print(text)