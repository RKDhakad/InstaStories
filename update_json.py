import json
import os

def update_json(username, user_data, filename):
    with open(filename, 'r') as f:
        data = json.loads(f.read())
        data[username] = user_data

    os.remove(filename)
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def update_heighlight(username, user_data, filename):
    with open(filename, 'r') as f:
        data = json.loads(f.read())

    new_heighlights = user_data['stories']
    
    if username in data:
        old_heighlights = data[username]
        old_stories_len = len(old_heighlights['stories'])
        for key in new_heighlights:

            old_stories_lst = []
            for old_key in old_heighlights["stories"]:
                old_stories_lst.append(old_heighlights["stories"][old_key]["Img"])

            if new_heighlights[key]["Img"] in old_stories_lst:
                pass
            else:
                old_stories_len += 1
                new_key = f"Story {old_stories_len}"
                data[username]["stories"][new_key] = new_heighlights[key]
                data[username]["Profile Pic"] = user_data["Profile Pic"]
    else:
        data[username] = user_data

    os.remove(filename)
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)