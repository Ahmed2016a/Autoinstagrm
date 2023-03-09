import requests
import random
import socket
from time import sleep
import requests
import time
import json
from user_agent import generate_user_agent
from colorama import Fore,Style

# -*- coding: utf-8 -*-


class ahmedfiras():
    def __init__(self):
        self.x = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.t = "@Not_Ahmed"
        self.b0 = Style.RESET_ALL
        self.b1 = Fore.YELLOW + '['
        self.b2 = Fore.YELLOW + ']'
        self.b3 = Fore.GREEN + '-'
        self.b4 = Fore.RED + '!'
        self.b5 = Fore.LIGHTCYAN_EX + '+'

    def internet(self,host="8.8.8.8", port=53, timeout=3):
        """
        Host: 8.8.8.8 (google-public-dns-a.google.com)
        OpenPort: 53/tcp
        Service: domain (DNS/TCP)
        """
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error as ex:
            return False
    def HomeScreen(self):
        while True:
            print(f'{self.b1}{self.b3}{self.b2}{self.b0} Ahmed firas || Tele {self.t}')
            print(f"""
{self.b1}1{self.b2}{self.b0} Login instagram
{self.b1}2{self.b2}{self.b0} Auto Comment instagram
{self.b1}3{self.b2}{self.b0} exit
        """)
            tool = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Num of Tool > ')
            if tool == '1':
                self.logins()
            elif tool == '2':
                self.Auto_comment()
            elif tool == '3':
                print(f'{self.b3} I wish u a happy day :)')
                sleep(3)
                exit()
            else:
                print(f'{self.b4} Bad Number')
                sleep(1.5)
                ahmedfiras().HomeScreen()
    def logins(self):
        username = input(f"{self.b1}{self.b3}{self.b2}{self.b0} Enter your username: ")
        password = input(f"{self.b1}{self.b3}{self.b2}{self.b0} Enter your password: ")
        while True:
            if ahmedfiras().internet() == True:
                print("True Network")
                break
            else:
                print("Network Error Wait 5 Sec")
                sleep(5)
        logina = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'viewport-width': '424',
            'x-asbd-id': '198387',
            'x-csrftoken': 'missing',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR1IMAIWPNnlPeUCa1Z9ZHzY6Pxeu3W04eOOFPE_XrauU1OR',
            'x-instagram-ajax': '1006773434',
            'x-requested-with': 'XMLHttpRequest',
        }

        millisec = int(round(time.time() * 1000))
        enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time}:{password}"
        dataw = {
            'enc_password': enc_password,
            'username': f'{username}',
            'queryParams': '{}',
            'optIntoOneTap': 'false',
            'trustedDeviceRecords': '{}',
        }

        login = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=logina, data=dataw)
        if "userId" in login.text:
                co = login.cookies
                coo = co.get_dict()
                csrf = coo["csrftoken"]
                ds_user_id = coo["ds_user_id"]
                ig_did = coo["ig_did"]
                mid = coo["mid"]
                rur = coo["rur"]
                sessionid = coo["sessionid"]
                cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"
                with open("datalogib.json","r") as f:
                     ahmed = json.loads(f.read()) #data becomes a dictionary
                     mid = mid
                     ig_didq = ig_did
                     ds_user_idq = ds_user_id
                     csrfq = csrf
                     sessionid = sessionid
                     rur = rur
                     f.close()
                     ahmed[f"{username}"] = {"mid":mid,"ig_did":ig_didq,"ds_user_id":ds_user_idq,"csrftoken":csrfq,"sessionid":sessionid,"rur":rur}
                     with open("datalogib.json", 'w') as f:
                         f.write(json.dumps(ahmed, sort_keys=True, indent=4, separators=(',', ': ')))
                         f.close()
                         print(f"{self.b3} True login : {username}\n\n")
                         ahmedfiras().HomeScreen()
        else:
              try:
                  jsonpath = "datalogib.json"
                  with open(jsonpath) as file:
                      j = json.loads(file.read())
                  del j[f'{username}']  
                  with open(jsonpath, 'w') as file:
                      file.write(json.dumps(j, indent=4))
                      file.close()
                  print(f"{self.b4} Fail login : {username}\n\n")
                  ahmedfiras().HomeScreen()
              except:
                   print(f"{self.b4} Fail login : {username}\n\n")

    def Auto_comment(self):
            while True:
                if ahmedfiras().internet() == True:
                    print("True Network")
                    break
                else:
                    print("Network Error Wait 5 Sec")
                    sleep(5)
            commentnum = 0
            username = input(f"{self.b1}{self.b3}{self.b2}{self.b0} Enter your username To Login : ")
            print(username)
            community = input(f"{self.b1}{self.b3}{self.b2}{self.b0} Enter your Comment : ")
            print("community")
            with open("datalogib.json","r") as fsss:
              content = json.loads(fsss.read())
              if str(username) in str(content):
                        print(f"{self.b3} Found {username}\n\n")
                        csrf = content[f"{username}"]["csrftoken"]
                        ds_user_id = content[f"{username}"]["ds_user_id"]
                        ig_did = content[f"{username}"]["ig_did"]
                        mid = content[f"{username}"]["mid"]
                        rur = content[f"{username}"]["rur"]
                        sessionid = content[f"{username}"]["sessionid"]
                        headerscomm = {
                                     'authority': 'www.instagram.com',
                                     'accept': '*/*',
                                     'accept-language': 'en-US,en;q=0.9',
                                     'cookie': f'mid={mid}; ig_did={ig_did};csrftoken={csrf}; ds_user_id={ds_user_id}; sessionid={sessionid}; rur={rur}',
                                     'origin': 'https://www.instagram.com',
                                     'sec-ch-prefers-color-scheme': 'light',
                                     'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                                     'sec-ch-ua-mobile': '?0',
                                     'sec-ch-ua-platform': '"Windows"',
                                     'sec-fetch-dest': 'empty',
                                     'sec-fetch-mode': 'cors',
                                     'sec-fetch-site': 'same-origin',
                                     'user-agent': generate_user_agent(),
                                     'viewport-width': '423',
                                     'x-asbd-id': '198387',
                                     'x-csrftoken': csrf,
                                     'x-ig-app-id': '936619743392459',
                                     'x-ig-www-claim': 'hmac.AR0LQ3lD7wLaTH7uHEkX70s-YMw4GU1UPXkowI150swT07lk',
                                     'x-instagram-ajax': '1006768086',
                                     'x-requested-with': 'XMLHttpRequest',
                                 }
                        for i in range(300):
                             while True:
                                if ahmedfiras().internet() == True:
                                    print("True Network")
                                    break
                                else:
                                    print("Network Error Wait 5 Sec")
                                    sleep(5)
                             try:
                                 hashtag = {'tag_name': 'اكسبلور',}
                                 pkposts = requests.get('https://www.instagram.com/api/v1/tags/web_info/', params=hashtag, headers=headerscomm).json()
                                 apk = pkposts["data"]["recent"]["sections"][0]["layout_content"]["medias"][0]["media"]["pk"]
                                 code = pkposts["data"]["recent"]["sections"][0]["layout_content"]["medias"][0]["media"]["code"]
                                 emoji = ["🤍","❤️","😮","🔥"]
                                 comment = {'comment_text': f'{random.choice(emoji)} {community}',}
                                 setcomment = requests.post(f'https://www.instagram.com/api/v1/web/comments/{apk}/add/',headers=headerscomm,data=comment,)
                                 url = "https://www.instagram.com/p/" + code
                                 if setcomment.json()['status'] == "ok":
                                     commentnum += 1
                                     print(f"{self.b3} Comment {commentnum} DONE by {username} :{url} , {comment['comment_text']}")
                                     sleep(288)
                                 else:
                                     print(setcomment.json())
                             except: 
                                     print(f"{self.b4}  error")
                        print(f'{self.b3} Done {commentnum} Commennt')
              else:
                      print(f"{self.b4} not found {username} re login\n\n")
                      ahmedfiras().HomeScreen()

ahmedfiras().HomeScreen()