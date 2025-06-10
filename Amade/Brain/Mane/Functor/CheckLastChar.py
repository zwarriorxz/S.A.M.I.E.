def TeleLogi_SentenceEndChar(sentence):
        last_char = sentence[-1]
            if last_char in {"?", "!", "."}:
                    return last_char
                        else:
                                return "Invalid syntax sentence char " + last_char 