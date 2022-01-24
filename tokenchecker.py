import colorama, ctypes, time, json, datetime
from colorama import Fore, init, Back, Style
from random import choice, randint
from os import system, name
import os, datetime, random, string
from os.path import exists, isfile
from requests import get, post
from json import loads, dumps
from urllib.request import Request, urlopen
import json
import discord, requests
import sys
colorama.init()


paymentskolvo = 0
q = 0
z = 0
c = 0
g = 0

os.system("cls")
if __name__ == "__main__":
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Token checker by vlc#1769")
    

def getHeader(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

with open('unchecked.txt') as ww:
    line_count = 0
    for line in ww:
        line_count += 1
f = open('checkedpayments.txt', 'a')
f.truncate(0)
time.sleep(0.1)
f = open('checkedvalid.txt', 'a')
f.truncate(0)
time.sleep(0.1)
f = open('checkedphones.txt', 'a')
f.truncate(0)
time.sleep(0.1)
payments = 'False'
tokensch = ''
paymentskolvo = 0
q = 0
z = 0
c = 0
g = 0
d = 0
checks = input("Input tokens into unchecked.txt and press enter")
if checks == 'y' or "Y":
    file1 = open("unchecked.txt", "r")
    while True:

        line = file1.readline()

        if not line:
            break

        tokensch = line.strip()
        headers = {'Authorization': tokensch, 'Content-Type': 'application/json'}  
        response = post(f'https://discord.com/api/v6/invite/{randint(1, 9999999)}', headers={'Authorization': tokensch})
        request = requests.get('https://canary.discordapp.com/api/v8/users/@me', headers=headers)
        if response.status_code == 401:
            q += 1
            d += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f"Token checker by vlc#1769 | All tokens: {line_count} | Checked: {d} | Valid: {z+paymentskolvo} | With payment sources: {paymentskolvo} | With phone number: {g} | Invalid: {q} | Phone locked: {c}")
            print(f'{tokensch} | {Fore.RED}Invalid token{Fore.WHITE}')
        elif "You need to verify your account in order to perform this action." in str(response.content):
            c += 1
            d += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f"Token checker by vlc#1769 | All tokens: {line_count} | Checked: {d} | Valid: {z+paymentskolvo} | With payment sources: {paymentskolvo} | With phone number: {g} | Invalid: {q} | Phone locked: {c}")
            print(f'{tokensch} | {Fore.RED}Phone locked token{Fore.WHITE}')
        else:
            cards = bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                                            headers=getHeader(tokensch))).read().decode())) > 0)
            if cards is True:
                d += 1
                paymentskolvo += 1
                print(f'{tokensch} | {Fore.LIGHTGREEN_EX}Valid token{Fore.WHITE}')
                userName = request.json()['username'] + '#' + request.json()['discriminator']
                userID = request.json()['id']
                phone = request.json()['phone']
                email = request.json()['email']
                mfa = request.json()['mfa_enabled']
                headers = {
                'path': '/api/v9/users/@me/guilds',
                'authorization': f'{tokensch}'
                }
                b = requests.get('https://discord.com/api/v9/users/@me/guilds',headers=headers).json()
                headers = {
                'path': '/api/v9/users/@me/relationships',
                'authorization': f'{tokensch}'
                }
                a = requests.get('https://discord.com/api/v9/users/@me/relationships',headers=headers).json()
                print(f'''
Username: {Fore.MAGENTA}{userName}{Style.RESET_ALL}
User ID: {Fore.MAGENTA}{userID}{Style.RESET_ALL}
2FA: {Fore.MAGENTA}{mfa}{Style.RESET_ALL}
Email: {Fore.MAGENTA}{email}{Style.RESET_ALL}
Phone number: {Back.GREEN}{phone if phone else f'{Style.RESET_ALL}{Back.RED}None'}{Style.RESET_ALL}
Friends amount: {Fore.MAGENTA}{len(a)}{Style.RESET_ALL}
Servers amount: {Fore.MAGENTA}{len(b)}{Style.RESET_ALL}
{Back.GREEN}Has payment sources{Style.RESET_ALL}
''')
                f = open('checkedpayments.txt', 'a')
                f.write(f"{tokensch}\n")
                time.sleep(0.5)
                f = open('checkedvalid.txt', 'a')
                f.write(f"{tokensch}\n")
                if phone is not None:
                    time.sleep(0.5)
                    f = open('checkedphones.txt', 'a')
                    f.write(f"{tokensch}\n")
                    g += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f"Token checker by vlc#1769 | All tokens: {line_count} | Checked: {d} | Valid: {z+paymentskolvo} | With payment sources: {paymentskolvo} | With phone number: {g} | Invalid: {q} | Phone locked: {c}")
            else:
                d += 1
                z += 1
                print(f'{tokensch} | {Fore.LIGHTGREEN_EX}Valid token{Fore.WHITE}')
                userName = request.json()['username'] + '#' + request.json()['discriminator']
                userID = request.json()['id']
                phone = request.json()['phone']
                email = request.json()['email']
                mfa = request.json()['mfa_enabled']
                headers = {
                'path': '/api/v9/users/@me/guilds',
                'authorization': f'{tokensch}'
                }
                b = requests.get('https://discord.com/api/v9/users/@me/guilds',headers=headers).json()
                headers = {
                'path': '/api/v9/users/@me/relationships',
                'authorization': f'{tokensch}'
                }
                a = requests.get('https://discord.com/api/v9/users/@me/relationships',headers=headers).json()
                print(f'''
Username: {Fore.MAGENTA}{userName}{Style.RESET_ALL}
User ID: {Fore.MAGENTA}{userID}{Style.RESET_ALL}
2FA: {Fore.MAGENTA}{mfa}{Style.RESET_ALL}
Email: {Fore.MAGENTA}{email}{Style.RESET_ALL}
Phone number: {Back.GREEN}{phone if phone else f'{Style.RESET_ALL}{Back.RED}None'}{Style.RESET_ALL}
Friends amount: {Fore.MAGENTA}{len(a)}{Style.RESET_ALL}
Servers amount: {Fore.MAGENTA}{len(b)}{Style.RESET_ALL}
''')
                f = open('checkedvalid.txt', 'a')
                f.write(f"{tokensch}\n")
                if phone is not None:
                    time.sleep(0.5)
                    f = open('checkedphones.txt', 'a')
                    f.write(f"{tokensch}\n")
                    g += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f"Token checker by vlc#1769 | All tokens: {line_count} | Checked: {d} | Valid: {z+paymentskolvo} | With payment sources: {paymentskolvo} | With phone number: {g} | Invalid: {q} | Phone locked: {c}")
    print(f'''
Tokens: {Fore.MAGENTA}{q+z+c}{Style.RESET_ALL}
Valid: {Fore.GREEN}{z+paymentskolvo}{Style.RESET_ALL}
Phone locked: {Fore.RED}{c}{Style.RESET_ALL}
Invalid: {Fore.RED}{q}{Style.RESET_ALL}
-----------------------------------------------------------
With payment sources: {Fore.GREEN}{paymentskolvo}{Style.RESET_ALL}
With phone number: {Fore.GREEN}{g}{Style.RESET_ALL}
-----------------------------------------------------------
Valid tokens saved in {Back.GREEN}checked.txt{Style.RESET_ALL}
Valid tokens {Back.GREEN}with payment sources{Style.RESET_ALL} saved in {Back.GREEN}checkedpayments.txt{Style.RESET_ALL}
Valid tokens {Back.GREEN}with phone number{Style.RESET_ALL} saved in {Back.GREEN}checkedphones.txt{Style.RESET_ALL}
        ''')
input()
