import json
from .EmotionDatabase_Folders import emotion_file_database

def read_emotion_level(emotion):
    with open(emotion_file_database(emotion), "r") as file:
        data = json.load(file)    
    level = data[emotion]["level"]
    intensity = data[emotion]["intensity"]
    output = (intensity * 10) + level
    if level != 10:
        output -= 10                           
    return output
    print("Reading "+ emotion + " was successful \n >Intensity:"+intensity+"\n Level:"+level)

