# ANSI color codes
GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'

def cfprint(attr, value):
    print(f"{GREEN}{attr}{RESET} : {RED}{value}{RESET}")
