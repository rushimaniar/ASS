'''
Logger for writing pretty shit to the terminal. We mean business yo.
'''

'''
Status can be Warning, Error, Info
'''
WARN = 'warn'
ERROR = 'err'
INFO = 'info'
def log(status, text):
    RED = '\033[31;1m'
    YELLOW ='\033[33m' 
    CYAN = '\033[36m'
    WHITE = '\033[37;0m'
    if status == 'err':
        print(RED + '[ ERROR ]\t' + text + WHITE)
    elif status == 'warn':
        print(YELLOW + '[ WARN ]\t' + text + WHITE)
    elif status == 'info':
        print(CYAN + '[ INFO ]\t' + text + WHITE)
    else:
        print(text)

    return

log(WARN, 'This is a warning')
log(ERROR, 'This is an error')
log(INFO, 'This is some information')