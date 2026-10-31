# ANSI color codes
GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'

def cfprint(attr, value):
    print(f"{GREEN}{attr}{RESET} : {RED}{value}{RESET}")


def bytes2gb(bytes: int): return str((bytes / (1024 ** 3))) + " GB"
def bytes2kb(bytes: int): return str((bytes / 1024)) + " KB"
def bytes2mb(bytes: int): return str((bytes / (1024 **2))) + " MB"
