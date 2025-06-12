import os

def emotion_file_database(emotion):
    script_path = os.path.dirname(os.path.abspath(__file__))#gets this script directory
    project_root = os.path.abspath(os.path.join(script_path "..", ".."))#gets brain folder

    emotion_path = os.path.join(project_root, "Moto", "Felilevelo",emotion, "emotion.json")
    return emotion_path

    if os.path.exists(emotion_path):
        print("Found emotion.json at:", emotion_path)
    else:
        print("emotion.json not found.")
