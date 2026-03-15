import json

def load_passwords():
    try:
        with open("passwords.json","r")as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []

def save_passwords(data):
    with open("passwords.json",'w')as file:
        json.dump(data,file,indent=4)