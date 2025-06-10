import json

def read_emotion_level(emotion):
    with open(emotion_file_database(emotion)) as file:
        data = json.load(file)     
    level = data[emotion]["level"]
    intensity = data[emotion]["intensity"]
    output = (intensity * 10) + level
    if level != 10:
        output -= 10                           
    return output

