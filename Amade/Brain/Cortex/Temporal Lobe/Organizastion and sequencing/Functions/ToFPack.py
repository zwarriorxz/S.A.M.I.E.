def ToF(str):
    if str.lower() == 't':
        return True
    elif str.lower() == 'f':
        return False
    else:
        raise ValueError("Not a valid argument: " + str)