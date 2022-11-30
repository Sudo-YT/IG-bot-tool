import time
import sys
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
    sys.exit()

if account == "y":
    hash = input("\n[>] Enter the hashtag you want to focus on: ")
    amount = input("[>] Enter the amount of posts you want to view: ")
    like = input("[>] Do you want to like the posts? (y/n): ")
    follow = input("[>] Do you want to follow the accounts? (y/n): ")
    comment = input("[>] Do you want to comment under the posts? (y/n): ")
    if comment == "y":
        cmt = input("[>] What would you like to comment?: ")
    type = input("[>] Do you want to view top posts (t) or recent posts (r): ")

    time.sleep(1)
    print(f"\n[+] Loading {amount} posts in the '{hash}' hashtag...")

    hashtag = hash

    if type == "t":
        medias = client.hashtag_medias_top(hashtag, int(amount))
        print(f"[+] {amount} have been posts loaded!")
        time.sleep(1)

    if type == "r":
        medias = client.hashtag_medias_recent(hashtag, int(amount))
        print(f"[+] {amount} posts have been loaded!")
        time.sleep(1)

    if like == "y":
        print("[+] Liking has begun!")
        for i, media in enumerate(medias):
            client.media_like(media.id)

    if like == "n":
        pass

    if follow == "y":
        print("[+] Following has begun!")
        for i, media in enumerate(medias):
            client.user_follow(media.user.pk)

    if follow == "n":
        pass
    
    try:
        if cmt == cmt:
            print("[+] Commenting has begun!")
            for i, media in enumerate(medias):
                client.media_comment(media.id, cmt)
    except NameError:
        sys.exit()