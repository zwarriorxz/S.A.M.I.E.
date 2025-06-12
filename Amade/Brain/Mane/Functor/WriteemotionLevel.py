import json
from .EmotionDatabase_Folders import emotion_file_database
 __init__.py
def write_emotion_level(emotion,level,intensity):
    with open("info.json", "r") as file:
        data = json.load(file)
    data[emotion]["level"] = level
    data[emotion]["intensity"] = intensity 
    with open(emotion_file_database(emotion), "w") as file:
        json.dump(data, file, indent=4)                             
    print("Writing to "+ emotion + " was a success")

