import json
from .Getfpath_Database import Getfolderpath

def createpythonfile(file, lines, code, filefolder):
    filepath = Getfolderpath(filefolder)
    full_path = filepath + "/" + file + ".py"
    F = open(full_path, "w")
    F.close()

    try:
        Writecode = open(full_path, "r").readlines                                
    except FileNotFoundError:
        Writecode = []

    max_index = max(lines)
    while len(Writecode) <= max_index:
        Writecode.append("\n")

    for i in lines:
        Writecode[i] = code[i] + "\n"

    with open(full_path, "w") as out:
        out.writelines(Writecode)