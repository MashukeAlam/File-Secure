import os
import threading
import time
import shutil

DEFENSE_DIR = os.path.expanduser('~')
FILE_DIR = ""
FILE_NAME = ""
CPY_CMD = 'copy' if os.name == 'nt' else 'cp'
HARD_MODE = False


def path_purify(path: str) -> str:
    if os.name != 'nt':
        return path
    return path.replace('\\', '\\\\')

def defense(path: str) -> bool:
    res = os.system(f"{CPY_CMD} {path} {DEFENSE_DIR}")
    if res != 0:
        print('Ohho there was an error!')
        return False
    return True

def just_dir(path: str) -> str:
    return '\\'.join(f"{path}".split('\\')[:-1])

def just_file(path: str) -> str:
    return path.split('\\')[-1]

def restore(path: str) -> bool:
    if not HARD_MODE:
        res = os.system(f"{CPY_CMD} {DEFENSE_DIR}\\{FILE_NAME} {FILE_DIR}")
        if res != 0:
            print('Ohho there was an error!')
            return False
    else:
        res = os.system(f"{CPY_CMD} {DEFENSE_DIR}\\{FILE_NAME} {FILE_DIR}")
        res = os.system(f"{CPY_CMD} {DEFENSE_DIR}\\{FILE_NAME} {FILE_DIR}")
        res = os.system(f"{CPY_CMD} {DEFENSE_DIR}\\{FILE_NAME} {FILE_DIR}")
        res = os.system(f"{CPY_CMD} {DEFENSE_DIR}\\{FILE_NAME} {FILE_DIR}")
        if res != 0:
            print('Ohho there was an error!')
            return False
    return True

def magic(path: str):
    try:
        while 1:
            if not os.path.exists(path):
                if(restore(path)):
                    print("Successfully restored!")
                else:
                    print("Sorry, Failed to restore.")
            time.sleep(1)
    except KeyboardInterrupt:
        file_secure_thread.join()
        

if __name__ == "__main__":
    
    print("############################")
    print("\t\tWelcome\t\t")
    print("############################")

    file_path = input("Please give the file address that you want to protect: ")
    file_path = path_purify(file_path)

    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            FILE_DIR = just_dir(file_path)
            FILE_NAME = just_file(file_path)
            print( FILE_DIR, FILE_NAME, CPY_CMD)
            defense(file_path)
            file_secure_thread = threading.Thread(target=magic, args=(file_path, ))
            file_secure_thread.start()
        else: print("This is not a file.")
    else: print("The directory was invalid or non-existant!")

