from mitmproxy import http
from story_data import imp_data
from update_json import update_json, update_heighlight
import time
import json
import datetime
import path_setup

try:
    import pyserver                         # only for termux in Android
except:pass

def request(flow: http.HTTPFlow):
    reels_url = "www.instagram.com/api/v1/feed/reels_media/?media_id="
    url = flow.request.pretty_url
    print(f"{url}\n")

def response(flow):
    reels_url = "instagram.com/api/v1/feed/reels_media/"
    heiglight = "instagram.com/api/v1/feed/reels_media/?reel_ids=highlight"
    url = flow.request.pretty_url

    if heiglight in url :
        heiglight = url
        responce = flow.response.content
        with open("json/data.json", "w", encoding="utf-8") as f:
            data = str(responce.decode('utf-8'))
            f.write(str(data))

        impdata = imp_data(json_file="json/data.json")

        for data in impdata:
            with open(f"json/heighlight.json", "r") as jf2:
                old_json_data = json.load(jf2)

            if str(impdata) not in str(old_json_data):
                update_heighlight(username=data["Username"], user_data=data, filename = f"json/heighlight.json")

    elif reels_url in url :
        reels_url = url
        responce = flow.response.content
        with open("json/data.json", "w", encoding="utf-8") as f:
            data = str(responce.decode('utf-8'))
            f.write(str(data))

        impdata = imp_data(json_file="json/data.json")

        for data in impdata:
            with open(f"json/extracted_data_{str(datetime.datetime.today()).split()[0]}.json", "r") as jf2:
                old_json_data = json.load(jf2)

            if str(impdata) not in str(old_json_data):
                update_json(username=data["Username"], user_data=data, filename = f"json/extracted_data_{str(datetime.datetime.today()).split()[0]}.json")
