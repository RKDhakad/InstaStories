from os import system
import json
import datetime

system("mkdir json")

try:
    json.load(open(f"json/data.json", encoding="utf-8"))
except:
    with open(f"json/data.json", "a", encoding="utf-8") as f:
        f.write("{}")
        f.close()

try:
    json.load(open(f"json/extracted_data_{str(datetime.datetime.today()).split()[0]}.json", encoding="utf-8"))
except:
    with open(f"json/extracted_data_{str(datetime.datetime.today()).split()[0]}.json", "a", encoding="utf-8") as f:
        f.write("{}")
        f.close()

try:
    json.load(open(f"json/heighlight.json", encoding="utf-8"))
except:
    with open(f"json/heighlight.json", "a", encoding="utf-8") as f:
        f.write("{}")
        f.close()