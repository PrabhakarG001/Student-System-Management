import json
F = "students.txt"

def load_data():
    try: return json.load(open(F))
    except: return []

def save_data(d):
    try: json.dump(d, open(F, 'w'))
    except: pass
