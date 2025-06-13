import os

def Getfolderpath(folder):
    start_path = os.getcwd()
    for _ in range(3):
        start_path = os.path.dirname(start_path)

    for root, dirs, _ in os.walk(start_path):
        if folder in dirs:
            return os.path.join(root, folder)
    return None

def Getfilepath(file):
    start_path = os.getcwd()
    for _ in range(3):
        start_path = os.path.dirname(start_path)

    for root, _, files in os.walk(start_path):
        if file in files:
            return os.path.join(root, file)
    return None
