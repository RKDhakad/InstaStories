import json

def imp_data(json_file):
    data = json.load(open(json_file, encoding="utf-8"))
    reels_media = data["reels_media"]

    impdatalst = []

    for reel_media in reels_media:
        username = reel_media["user"]["username"]
        username = reel_media["user"]["username"]
        profile_pic_url = reel_media["user"]["profile_pic_url"]

        stories = reel_media["items"]

        x = 1
        impdata = {}
        impdata["Username"] = username
        impdata["Profile Pic"] = profile_pic_url

        story_data = {}

        for story in stories:
            story_info = {}

            story_img = story["image_versions2"]["candidates"][0]["url"]
            story_info["Img"] = story_img

            try:
                story_vid = story["video_versions"][0]["url"]
                story_info["Video"] = story_vid
            except:
                story_info["Video"] = ""

            try:
                mentions = []
                for mention in story["story_bloks_stickers"]:
                    mentions.append(mention["bloks_sticker"]["sticker_data"]["ig_mention"]["username"])
            except:mentions = [""]

            mentioned = ""
            for i in mentions:
                mentioned += f"{i}, "

            story_info[f"Mentions"] = mentioned
            story_data[f"Story {x}"] = story_info
            x += 1

        impdata["stories"] = story_data
        impdatalst.append(impdata)
    return impdatalst

if __name__ == "__main__":
    print("Done")



        
    
