def D_emotion(emotion, tense):
    status = emotion + tense
    print(status)
    if tense > 1:
        print("Intensity more than 1")
    if tense > 15:
        print("Intensity levels rising")
    if tense > 25:
        print("Intensity more than half.")
    if tense >40:
        print("Intensity level high")
    if tense != range(1,51):
        print("num is not valid number")
