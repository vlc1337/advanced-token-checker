import requests
from datetime import datetime
import os
from colorama import *
import ctypes
import time
from config import save_results, check_payments

clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')
init()

#reading tokens
if not os.path.exists(f'{os.getcwd()}/tokens.txt'):
    info_loaded = 'Put your tokens into tokens.txt and restart the programm'
    with open(f'{os.getcwd()}/tokens.txt', "a") as file:
        pass
else:
    tokens = open(f'{os.getcwd()}/tokens.txt').readlines()
    tokens = [q.replace('\n','') for q in tokens]
    info_loaded = f'Loaded {len(tokens)} tokens'


intro = f'''{Fore.MAGENTA}
▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █     ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █    ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒   ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒   ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒    ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░     ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
  ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░    ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
             ░ ░  ░  ░      ░  ░         ░    ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                                              ░                       ░                               

{info_loaded}
'''
print(intro)

def get_payment_methods(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(
        'https://discord.com/api/v10/users/@me/billing/payment-sources',
        headers=headers
    )
    if response.status_code == 200:
        return response.json()
    else:
        return None

def decode_user_flags(flag):
    flags = {
            1 << 0: "STAFF (Discord Employee)",
            1 << 1: "PARTNER (Partnered Server Owner)",
            1 << 2: "HYPESQUAD (HypeSquad Events Member)",
            1 << 3: "BUG_HUNTER_LEVEL_1",
            1 << 6: "HYPESQUAD (House Bravery)",
            1 << 7: "HYPESQUAD (House Brilliance)",
            1 << 8: "HYPESQUAD (House Balance)",
            1 << 9: "EARLY_SUPPORTER",
            1 << 10: "TEAM_PSEUDO_USER",
            1 << 14: "BUG_HUNTER_LEVEL_2",
            1 << 16: "VERIFIED_BOT",
            1 << 17: "VERIFIED_DEVELOPER",
            1 << 18: "CERTIFIED_MODERATOR",
            1 << 19: "BOT_HTTP_INTERACTIONS",
            1 << 22: "ACTIVE_DEVELOPER"
        }
    return [value for bit, value in flags.items() if flag & bit]

def decode_nitro(nitro):
    nitros = {
        1: 'Nitro Classic',
        2: 'Nitro Boost',
        3: 'Nitro Basic'
    }
    return nitros[nitro]

def progress_bar(current, total, length=10):
    percent = current / total
    filled = int(length * percent)
    bar = "\N{FULL BLOCK}" * filled + "\N{LIGHT SHADE}" * (length - filled)
    return f"\r[{bar}] {percent:.0%}"

try:
    start_time = time.time()
    c=0
    valid=[]
    invalid=[]
    phone_locked=[]
    for token in tokens:
        headers = {"Authorization": token}
        response = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
        c+=1
        if response.status_code == 401:
            print(f'{Fore.RED}{token} | Invalid token')
            invalid.append(token)
        elif "You need to verify your account in order to perform this action." in str(response.content):
            print(f'{Fore.RED}{token} | Phone locked token')
            phone_locked.append(token)
        else:
            info = response.json()
            output = f'{Fore.GREEN}{token} | Valid token\nUsername: {info['username']}\nMail: {info['email']}'
            if info['phone']:
                output+=f'\nPhone: {info['phone']}'
            if info['public_flags']:
                output+=f'\nBadges: {decode_user_flags(info['public_flags'])}'
            if info['premium_type']:
                output+=f'\nNitro subscription: {decode_nitro(info['premium_type'])}'
            if check_payments:
                payments = get_payment_methods(token)
                if payments:
                    output+=f'\nPayment sources: {len(payments)}'
            print(output)
            valid.append(token)
        ctypes.windll.kernel32.SetConsoleTitleW(f"Token checker | {progress_bar(c, len(tokens))} | Valid: {len(valid)} | Invalid: {len(invalid)} | Phone locked: {len(phone_locked)}")
    elapsed_time = time.time() - start_time
    print(f'\n{Fore.WHITE}Elapsed time: {elapsed_time:.2f}')
    if save_results:
        os.makedirs(os.path.join(os.getcwd(), f'check_results_{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'), exist_ok=True)
        with open(f'{os.getcwd()}\\check_results_{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}\\valid.txt', "a") as file:
            file.write('\n'.join(valid))
        print(f'Saved results in check_results_{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}\\valid.txt')
except Exception as e:
    print(e)
finally:
    input('\nPress enter to close the programm')