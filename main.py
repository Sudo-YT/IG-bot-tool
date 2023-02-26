import time
import json
from instagrapi import Client

print("\033[1;32;40m\n""""{}
 _______  __   __  ______   _______  _______ 
|       ||  | |  ||      | |       ||       |
|  _____||  | |  ||  _    ||   _   ||  _____|
| |_____ |  |_|  || | |   ||  | |  || |_____ 
|_____  ||       || |_|   ||  |_|  ||_____  |
 _____| ||       ||       ||       | _____| |
|_______||_______||______| |_______||_______|
 ___   _______    _______  _______  _______  
|   | |       |  |  _    ||       ||       | 
|   | |    ___|  | |_|   ||   _   ||_     _| 
|   | |   | __   |       ||  | |  |  |   |   
|   | |   ||  |  |  _   | |  |_|  |  |   |   
|   | |   |_| |  | |_|   ||       |  |   |   
|___| |_______|  |_______||_______|  |___|   
 _______  _______  _______  ___              
|       ||       ||       ||   |             
|_     _||   _   ||   _   ||   |             
  |   |  |  | |  ||  | |  ||   |             
  |   |  |  |_|  ||  |_|  ||   |___          
  |   |  |       ||       ||       |         
  |___|  |_______||_______||_______| 2.0                   
                                                                                           
{}\n\t[+] Welcome to my improved Instagram bot tool (•◡ •) /\n\t[+] Subscribe to Sudo on YouTube\n{}""".format("="*100,"="*100,"="*100))

with open("Login.json", "r") as logins:
    logs = json.load(logins)

client = Client()
print("[+] Loading Instagram account...")
client.login(logs['user'], logs['pw'])
print("[+] Account loaded!\n")
time.sleep(1)

account = input(f"[>] Is your username {logs['user']}? (y/n): ")

if account == "n":
    print("[+] Open Login.json and edit your login")

if account == "y":
    HashUser = input("\n[>] Do you want to target a hashtag or an account? (h/a): ")

    if HashUser == "h":
        hash = input("[>] Enter the hashtag you want to target: ")
        type = input("[>] Do you want to view top posts (t) or recent posts (r): ")
    if HashUser == "a":
        acc = input("[>] Enter the account you want to target: ")

    amount = int(input("[>] Enter the amount of posts you want to view: "))

    if HashUser == "a":
        story = input("[>] Do you want to like their stories? (y/n): ")

    like = input("[>] Do you want to like the posts? (y/n): ")
    follow = input("[>] Do you want to follow the accounts? (y/n): ")
    comment = input("[>] Do you want to comment under the posts? (y/n): ")

    if comment == "y":
        cmt = input("[>] What would you like to comment?: ")

    delay = int(input("[>] Enter a delay (Higher delay will be less detectable but will take longer): "))

    time.sleep(1)

    if HashUser == "h":
        print(f"\n[+] Loading {amount} posts in the '{hash}' hashtag...")

    if HashUser == "a":
        print(f"\n[+] Loading {amount} posts from '@{acc}'...")
        target = client.user_id_from_username(acc)
        medias = client.user_medias(target, int(amount))
        print(f"[+] {amount} have posts have been loaded!")
        time.sleep(1)

    if type == "t":
        medias = client.hashtag_medias_top(hash, int(amount))
        print(f"[+] {amount} have been posts loaded!")
        time.sleep(1)

    if type == "r":
        medias = client.hashtag_medias_recent(hash, int(amount))
        print(f"[+] {amount} posts have been loaded!")
        time.sleep(1)

    try:
        if story == "y":
            print("[+] Story liking has begun!")
            time.sleep(1)
            print(f"[+] Estimated time for story liking: {amount * delay * 1.5} seconds")
            for media in medias:
                stories_pk = []
                user_pk = media.user.pk
                stories = client.user_stories(int(user_pk), amount=1)

                if stories:
                    for story in stories:
                        stories_pk.append(int(story.pk))
                    client.story_seen(story_pks=stories_pk)

                for one_story_id in stories_pk:
                    client.story_like(story_id=one_story_id)
    except NameError:
        pass

    if like == "y":
        print("[+] Post liking has begun!")
        time.sleep(1)
        print(f"[+] Estimated time for post liking: {amount * delay * 1.5} seconds")
        for i, media in enumerate(medias):
            client.media_like(media.id)
            time.sleep(int(delay))

    if follow == "y":
        print("[+] Following has begun!")
        time.sleep(1)
        print(f"[+] Estimated time for following: {amount * delay * 1.5} seconds")
        for i, media in enumerate(medias):
            client.user_follow(media.user.pk)
            time.sleep(int(delay))
    
    try:
        if cmt == cmt:
            print("[+] Commenting has begun!")
            time.sleep(1)
            print(f"[+] Estimated time for commenting: {amount * delay * 1.5} seconds")
            for i, media in enumerate(medias):
                client.media_comment(media.id, cmt)
                time.sleep(int(delay))
    except NameError:
        pass
