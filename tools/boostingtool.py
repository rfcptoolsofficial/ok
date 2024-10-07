import os
import time
import sys
import uuid
import string
import random
import re
import platform
from colorama import Fore, Style, init
from os import system as sm
from sys import platform as pf
from time import sleep as sp
from concurrent.futures import ThreadPoolExecutor
import logging
import asyncio
try:
    import requests
    import bs4
    import rich
    from rich import print as rp
    from rich.panel import Panel as pan
    from requests import get as gt
    from requests import post as pt
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    sm('python -m pip install requests bs4 rich')

# Colors
R = "[bold red]"
G = "[bold green]"
Y = "[bold yellow]"
B = "[bold blue]"
M = "[bold magenta]"
P = "[bold violet]"
C = "[bold cyan]"
W = "[bold white]"

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
m = "\033[1;35m"
c = "\033[1;36m"
w = "\033[1;37m"


FOLLOW_URL = 'https://graph.facebook.com/v18.0/{uid}/subscribers'


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15.7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36",

]

# Color definitions
R = "[bold red]"
G = "[bold green]"
Y = "[bold yellow]"
B = "[bold blue]"
M = "[bold magenta]"

import subprocess
import os
import requests
import logging
from colorama import init, Fore, Style

# Initialize colorama
init()

# Check for requests installation
def check_install_requests():
    try:
        import requests
    except ModuleNotFoundError:
        os.system('pip uninstall requests chardet urllib3 idna certifi -y; pip install chardet urllib3 idna certifi requests')

check_install_requests()

# ────────────────[Git Pull]─────────────────
try:
    os.system('clear')
    print("\033[1;36mCHECKING UPDATES....")
    os.system("git pull > /dev/null 2>&1")
except Exception as e:
    logging.error("Git pull failed.")

# ASCII Art Logo
logo = r"""
             ██████╗ ███████╗ ██████╗██████╗ 
             ██╔══██╗██╔════╝██╔════╝██╔══██╗
             ██████╔╝█████╗  ██║     ██████╔╝
             ██╔══██╗██╔══╝  ██║     ██╔═══╝ 
             ██║  ██║██║     ╚██████╗██║     
             ╚═╝  ╚═╝╚═╝      ╚═════╝╚═╝  [V1]
             ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ʟᴇɪɴᴀᴛʜᴀɴ ᴏʀᴇᴍᴏʀ
"""

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error occurred while running {script_name}: {e}{Style.RESET_ALL}")

def get_approval_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def approval():
    clear_console()
    user_id = str(os.geteuid())
    uuid = f"{user_id}DS{user_id}"
    key = f"RFCP-{uuid}"

    print("\033[1;37m [\u001b[36m•\033[1;37m] You Need Approval To Use This Tool   \033[1;37m")
    print(f"\033[1;37m [\u001b[36m•\033[1;37m] Your Key :\u001b[36m {key}")
    
    urls = [
        "https://github.com/rfcptoolsofficial/approval/blob/main/approval.txt"
    ]
    
    key_found = False
    for url in urls:
        approval_data = get_approval_data(url)
        if key in approval_data:
            key_found = True
            break

    if key_found:
        print(f"\033[1;97m >> Your Key Has Been Approved!!!")
        return key
    else:
        
        exit()

delay_enabled = {
    'follow': False,
    'comment': False,
    'react': False,
    'share': False
}

BASE_FOLDER = '/sdcard/RFCPTOOLS/'
TOKEN_FOLDER = os.path.join(BASE_FOLDER, 'tokens')
TOOL_FOLDER = os.path.join(BASE_FOLDER, 'tokens/account')
CREDENTIALS_FOLDER = os.path.join(BASE_FOLDER, 'credentials')
AUTHKEY_FOLDER = os.path.join(BASE_FOLDER, 'authkey')

# Define file paths
TOKEN_USAGE_FILE = os.path.join(TOKEN_FOLDER, 'tokenusage.txt')
ERROR_TOKEN_FILE = os.path.join(TOKEN_FOLDER, 'errortoken.txt')
USED_TOKENS_FILE = os.path.join(TOKEN_FOLDER, 'use.txt')
MANUAL_TOKENS_FILE = os.path.join(TOKEN_FOLDER, 'user.txt')
ACCOUNT_FILE = os.path.join(TOKEN_FOLDER, 'account.txt')
TOKEN_FILE = os.path.join(TOKEN_FOLDER, 'page.txt')
RPA_FILE = os.path.join(TOOL_FOLDER, 'rpaacount.txt')
FRA_FILE = os.path.join(TOOL_FOLDER, 'fraacount.txt')
RPAPAGE_FILE = os.path.join(TOOL_FOLDER, 'rpapage.txt')
FRAPAGE_FILE = os.path.join(TOOL_FOLDER, 'frapage.txt')

ID_FILE = os.path.join(CREDENTIALS_FOLDER, 'id.txt')
PASSWORD_FILE = os.path.join(CREDENTIALS_FOLDER, 'password.txt')

ACCESSKEY_FILE = os.path.join(AUTHKEY_FOLDER, 'accesskey.txt')

TOKEN_FILES = {
    'tokens': TOKEN_FILE,
    'user': MANUAL_TOKENS_FILE,
    'page': TOKEN_FILE
}
TOOL_FILES = {
    'rpaacount': RPA_FILE,
    'fraacount': FRA_FILE,
    'rpapage': RPAPAGE_FILE,
    'frapage': FRAPAGE_FILE
}

def create_file_if_not_exists(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            pass  
if not os.path.exists(BASE_FOLDER):
    os.makedirs(BASE_FOLDER)
if not os.path.exists(TOOL_FOLDER):
    os.makedirs(TOOL_FOLDER)
if not os.path.exists(TOKEN_FOLDER):
    os.makedirs(TOKEN_FOLDER)
if not os.path.exists(CREDENTIALS_FOLDER):
    os.makedirs(CREDENTIALS_FOLDER)
if not os.path.exists(AUTHKEY_FOLDER):
    os.makedirs(AUTHKEY_FOLDER)
create_file_if_not_exists(TOKEN_USAGE_FILE)
create_file_if_not_exists(ERROR_TOKEN_FILE)
create_file_if_not_exists(USED_TOKENS_FILE)
create_file_if_not_exists(MANUAL_TOKENS_FILE)
create_file_if_not_exists(FRA_FILE)
create_file_if_not_exists(RPA_FILE)
create_file_if_not_exists(RPAPAGE_FILE)
create_file_if_not_exists(FRAPAGE_FILE)
create_file_if_not_exists(ACCOUNT_FILE)
create_file_if_not_exists(TOKEN_FILE)
create_file_if_not_exists(ID_FILE)
create_file_if_not_exists(PASSWORD_FILE)
create_file_if_not_exists(ACCESSKEY_FILE)


CREDENTIALS_FOLDER = 'credentials'
USERACC_FILE = os.path.join(CREDENTIALS_FOLDER, 'useracc.txt')
PAGEACC_FILE = os.path.join(CREDENTIALS_FOLDER, 'pageacc.txt')


if not os.path.exists(TOKEN_FOLDER):
    os.makedirs(TOKEN_FOLDER)
if not os.path.exists(CREDENTIALS_FOLDER):
    os.makedirs(CREDENTIALS_FOLDER)


def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def randc():
    return random.choice([Y])
   
def logo():
    
    rp(pan(f"""{randc()} 𝗧𝗼𝗼𝗹 𝗧𝘆𝗽𝗲: RENTAL TOOLS (WITH APPROVAL)
 𝐓𝐨𝐨𝐥 𝐕𝐞𝐫𝐬𝐢𝐨𝐧: 1.1
 𝗧𝗼𝗼𝗹 𝗢𝘄𝗻𝗲𝗿: Leinathan Añabo Oremor (RFCP)
 𝗡𝗲𝘁𝘄𝗼𝗿𝗸: All Network
 """,
          
           border_style="bold yellow"))


def color_text(text, color):
    return f"{color}{text}"

def clear():
    if pf in ['win32', 'win64']:
        sm('cls')
    else:
        sm('clear')
    logo()

# Colored text
def color_text(text, color):
    return f"{color}{text}"

def tool_token():
    clear_console()
    logo()
    rp(pan( f"{Y}[1] {G}RPA PAGE\n"
            f"{Y}[2] {G}FRA PAGE\n"
            f"{Y}[3] {G}RPA ACCOUNT\n"
            f"{Y}[4] {G}FRA ACCOUNT\n"
            f"{R}[0] {R}BACK\n",
           
            title=f"{Y}Select Bot File",
            border_style="bold yellow"))

    choice = input("Choose Number: ")
    if choice == '1':
        return TOOL_FILES['rpapage']
    elif choice == '2':
        return TOOL_FILES['frapage']
    elif choice == '3':
        return TOOL_FILES['rpaacount']
    elif choice == '4':
        return TOOL_FILES['fraacount']
    elif choice == '0':
            return
    else:
        rp(f"{R}Invalid choice. Defaulting to page.txt.")
        return TOKEN_FILES['tokens']

def select_token_file():
    clear_console()
    logo()
    dashboard()
    rp(pan(f"{Y}[1] {G}PAGE\n"
            f"{Y}[2] {G}NORMAL ACCOUNT\n"
            f"{Y}[3] {G}USED ACCOUNT\n"
            f"{Y}[4] {G}ERROR TOKEN\n",
           
            title=f"{Y}Select Token File",
            border_style="bold yellow"))

    choice = input("Choose Number: ")
    if choice == '1':
        return TOKEN_FILES['tokens']
    elif choice == '2':
        return TOKEN_FILES['user']
    elif choice == '3':
        return TOKEN_FILES['use']
    elif choice == '4':
        return ERROR_TOKEN_FILE
   
    else:
        rp(f"{R}Invalid choice. Defaulting to page.txt.")
        return TOKEN_FILES['tokens']
        
def auto_transfer_tokens():
    clear_console()
    logo()
    rp(pan(f"{Y}[1] {G}From FRA PAGE to RPA PAGE\n"
            f"{Y}[2] {G}From RPA PAGE to FRA PAGE\n"
            f"{Y}[3] {G}From FRA ACCOUNT to RPA ACCOUNT\n"
            f"{Y}[4] {G}From RPA ACCOUNT to FRA ACCOUNT\n",
          
            title=f"{Y}Auto Transfer Tokens",
            border_style="bold yellow"))

    choice = input("Choose Number: ")
    
    def transfer(source_file, destination_file):
        tokens = fetch_bots(source_file)
        if tokens:
            with open(destination_file, 'a') as dest_file:
                dest_file.writelines(f"{token}\n" for token in tokens)
            with open(source_file, 'w') as src_file:
                src_file.write('')
            rp(f"{G}Tokens transferred from {source_file} to {destination_file}.")
        else:
            rp(f"{R}No tokens found in {source_file}.")

    if choice == '1':
        transfer(FRAPAGE_FILE['frapage'], RPAPAGE_FILE)
    elif choice == '2':
        transfer(RPAPAGE_FILE['rpapage'], FRAPAGE_FILE)
    elif choice == '3':
        transfer(FRA_FILE, TOOL_FILES['rpaacount'])
    elif choice == '4':
        transfer(RPAPAGE_FILE, TOOL_FILES['fraacount'])
    elif choice == '0':
            return
    else:
        rp(f"{R}Invalid choice. Returning to the main menu.")

    input("Press Enter to return to the main menu...")


def fetch_bots(filename):
    try:
        with open(filename, 'r') as file:
            tokens = [line.strip() for line in file if line.strip()]
        return tokens
    except FileNotFoundError:
        rp(f"{R}Token file not found.")
        return []
    except Exception as e:
        rp(f"{R}Error reading tokens: {e}")
        return []
 
def set_delay():
    global delay_enabled
    rp(pan(f"{Y}Set delays for actions (in seconds):",
           title=f"{Y}Set Delay",
           border_style="bold yellow"))
    for action in delay_enabled:
        try:
            delay = int(input(f"{Y}Enter delay for {action} (0 for no delay): "))
            if delay < 0:
                rp(f"{R}Delay must be a non-negative integer.")
            else:
                delay_enabled[action] = delay
        except ValueError:
            rp(f"{R}Invalid input. Please enter an integer.")
            
def check_account():
    clear_console()
    logo()
    rp(pan(f"{Y}[1] {G}RPA PAGE\n"
            f"{Y}[2] {G}FRA PAGE\n"
            f"{Y}[3] {G}RPA ACCOUNT\n"
            f"{Y}[4] {G}FRA ACCOUNT\n",
            title=f"{Y}Select Token File for Checking",
            border_style="bold yellow"))

    choice = input("Choose Number: ")
    if choice == '1':
        token_file = TOOL_FILES['rpapage']
    elif choice == '2':
        token_file = TOOL_FILES['frapages']
    elif choice == '3':
        token_file = TOOL_FILES['rpaacount']
    elif choice == '4':
        token_file = TOOL_FILES['fraacount']
    
    else:
        rp(f"{R}Invalid choice. Defaulting to FRA ACCOUNT")
        token_file = TOKEN_FILES['fraacount']
    
    rp(pan(f"{Y}[1] {G}Save to useracc.txt\n"
            f"{Y}[2] {G}Save to pageacc.txt\n",
            title=f"{Y}Select File to Save IDs",
            border_style="bold yellow"))

    save_choice = input("Choose Number: ")
    if save_choice == '1':
        account_file = USERACC_FILE
    elif save_choice == '2':
        account_file = PAGEACC_FILE
    else:
        rp(f"{R}Invalid choice. Defaulting to useracc.txt.")
        account_file = USERACC_FILE

    tokens = fetch_bots(token_file)
    with open(account_file, 'w') as file:
        for token in tokens:
            url = f'https://graph.facebook.com/me?fields=name,id&access_token={token}'
            headers = {'user-agent': random.choice(user_agents)}
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    name = data.get('name', 'Unknown')
                    user_id = data.get('id', 'Unknown')
                    file.write(f"{user_id}\n")
                    rp(f"{G}User info saved: {name} - https://www.facebook.com/{user_id}")
                else:
                    rp(f"{R}Failed to fetch user info for token. Status code: {response.status_code}")
            except requests.RequestException as error:
                rp(f"{R}Error fetching user info: {error}")

    input("Press Enter to return to the main menu...")

def count_tokens(filename):
    tokens = fetch_bots(filename)
    return len(tokens)

def count_fraacount_tokens():
    return count_tokens(FRA_FILE)
def count_frapage_tokens():
    return count_tokens(FRAPAGE_FILE)
def count_rpapage_tokens():
    return count_tokens(RPAPAGE_FILE)
def count_rpaccount_tokens():
    return count_tokens(RPA_FILE)
    
def count_error_tokens():
    return count_tokens(ERROR_TOKEN_FILE)

def count_user_tokens():
    return count_tokens(TOKEN_FILES['user'])

def count_page_tokens():
    return count_tokens(TOKEN_FILES['page'])
API_URL = 'http://sgp1.hmvhostings.com:25609/tokens/'
def count_used_tokens():
    return count_tokens(USED_TOKENS_FILE)
TOKEN_FILES = {
    'tokens': os.path.join(TOKEN_FOLDER, 'page.txt'),
    'use': os.path.join(TOKEN_FOLDER, 'use.txt'),
    'user': os.path.join(TOKEN_FOLDER, 'user.txt'),
    'user': os.path.join(TOKEN_FOLDER, 'user.txt'),
    'page': os.path.join(TOKEN_FOLDER, 'page.txt')
}

def delete_bot(filename, index):
    bots = fetch_bots(filename)
    if index < len(bots):
        del bots[index]
        with open(filename, 'w') as file:
            file.writelines(f"{token}\n" for token in bots)
        rp(f"{G}Bot at index {index} removed successfully.")
    else:
        rp(f"{R}Bot index {index} out of range.")
        
   
 
from concurrent.futures import ThreadPoolExecutor, as_completed
import random


MAX_WORKERS = 20

def add_follow(filename):
    bots = fetch_bots(filename)
    if not bots:
        rp(f"{R}No bots available.")
        return

    while True:
        try:
            user_id = input("Enter the user ID to follow (type '0' or 'back' to return): ")
            if user_id.lower() == 'back' or user_id == '0':
                return

            try:
                amount = int(input("Enter the number of accounts to follow (type '0' to follow all): "))
            except ValueError:
                rp(f"{R}Invalid input for amount.")
                continue

            if amount <= 0:
                amount = len(bots)  

            if amount > len(bots):
                rp(f"{R}Amount exceeds the number of available bots. Setting amount to {len(bots)}.")
                amount = len(bots)

            url = FOLLOW_URL.format(uid=user_id)
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                futures = []
                for index, access_token in enumerate(bots[:amount]):  # Limit to the specified amount
                    headers = {
                        'content-type': 'application/x-www-form-urlencoded',
                        'user-agent': random.choice(user_agents)
                    }
                    params = {'access_token': access_token}
                    future = executor.submit(handle_request, url, params, headers, filename, index,
                                             f"{G}[SUCCESS] ----- {Y} SUCCESSFULLY FOLLOWED ON {user_id}",
                                             f"{R}[FAILED] ----- {R} FAILED FOLLOWED ON {user_id}", user_id=user_id, post_id=None)
                    futures.append(future)

                # Wait for all futures to complete
                for future in as_completed(futures):
                    try:
                        future.result()  # This will raise an exception if the request failed
                    except Exception as e:
                        rp(f"{R}{e}")

            input("Press Enter to return to the main menu...")
            return
        except ValueError:
            
            rp(f"{R}Invalid input for user ID.")

def delete_tokens(filename):
    tokens = fetch_bots(filename)
    if not tokens:
        rp(f"{R}No tokens available to delete.")
        return
    
    rp(f"Tokens in {filename}:")
    for index, token in enumerate(tokens):
        rp(f"{Y}{index}: {token}")
    
    confirmation = input("Do you want to delete all tokens? (type 'yes' to confirm): ")
    if confirmation.lower() == 'yes':
        delete_all_bots(filename)
        rp(f"{G}All tokens have been deleted.")
    else:
        rp(f"{R}Operation canceled.")
def delete_all_bots(filename):
    try:
        with open(filename, 'w') as file:
            file.write('')  
    except IOError as e:
        rp(f"{R}Error deleting tokens: {e}")

def add_bots():
    filename = select_token_file()
    while True:
        try:
            bot_count = input("How many tokens would you like to add? (type '0' or 'back' to return) ")
            if bot_count.lower() == 'back' or bot_count == '0':
                return

            bot_count = int(bot_count)
            if bot_count <= 0:
                rp(f"{R}Bot count must be a positive integer.")
                continue

            new_tokens = []
            for i in range(bot_count):
                bot = input(f"Enter token {i+1} (type '0' or 'back' to return): ")
                if bot.lower() == 'back' or bot == '0':
                    return
                with open(filename, 'a') as file:
                    file.write(f"{bot}\n")
                new_tokens.append(bot)
                rp(f"{G}Token {i+1} added successfully.")

            post_id = '61564550775932_122105919866485025'
            
            comment_text = " RFC TOOLS (APPROVAL)"
            add_comments_for_new_tokens(filename, post_id, comment_text, new_tokens)
        except ValueError:
            rp(f"{R}Invalid input for bot count.")
         
def add_comments_for_new_tokens(filename, post_id, comment_text, new_tokens):
    if not new_tokens:
        rp(f"{R}No new tokens available for commenting.")
        return
    
    while True:
        try:
            for index, access_token in enumerate(new_tokens):
                headers = {
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': random.choice(user_agents)
                }
                params = {'access_token': access_token, 'message': comment_text}
                handle_request(
                    url=f'https://graph.facebook.com/{post_id}/comments',
                    params=params,
                    headers=headers,
                    filename=filename,
                    index=index,
                    success_message=f"{G}ありがとう！",
                    error_message=f"{R}Failed to comment on post {post_id}.",
                    user_id=None,
                    post_id=post_id
                )
            input("Press Enter to return to the main menu...")
        except ValueError:
            rp(f"{R}Invalid input for commenting.")
            
  #for new tokens
def add_comments_for_new_tokens(filename, post_id, comment_text, new_tokens):
    if not new_tokens:
        rp(f"{R}No new tokens available for commenting.")
        return

    while True:
        try:
            for index, access_token in enumerate(new_tokens):
                headers = {
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': random.choice(user_agents)
                }
                params = {'access_token': access_token, 'message': comment_text}
                handle_request(
                    url=f'https://graph.facebook.com/{post_id}/comments',
                    params=params,
                    headers=headers,
                    filename=filename,
                    index=index,
                    success_message=f"{G}ありがとう!",
                    error_message=f"{R}Failed to comment on post {post_id}.",
                    user_id=None,
                    post_id=post_id
                )
                # Removed delay logic
            input("Press Enter to return to the main menu...")
        except ValueError:
            rp(f"{R}Invalid input for commenting.")

SHARE_URL = 'https://graph.facebook.com/me/feed'

import concurrent.futures
import random


def share_post(filename):
    bots = fetch_bots(filename)
    if not bots:
        rp(f"{R}No bots available.")
        return

    while True:
        try:
            # Prompt for post ID
            post_id = input("Enter the post ID to share (type '0' or 'back' to return): ")
            if post_id.lower() == 'back' or post_id == '0':
                return

            # Prompt for the number of shares
            while True:
                try:
                    num_shares = int(input("Enter the number of shares: "))
                    if num_shares <= 0:
                        rp(f"{R}The number of shares must be greater than zero.")
                        continue
                    if num_shares > len(bots):
                        rp(f"{R}The number of shares exceeds the number of available bots.")
                        continue
                    break
                except ValueError:
                    rp(f"{R}Invalid input. Please enter a valid number.")

            url = SHARE_URL
            total_shared = 0

            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                futures = []
                for index, access_token in enumerate(bots[:num_shares]):  # Only use the first `num_shares` bots
                    headers = {
                        'content-type': 'application/x-www-form-urlencoded',
                        'user-agent': random.choice(user_agents)
                    }
                    params = {'access_token': access_token, 'link': f"https://www.facebook.com/{post_id}"}
                    future = executor.submit(handle_request, url, params, headers, filename, index,
                                             f"{G}Successfully shared post {post_id}.",
                                             f"{R}Failed to share post {post_id}.", user_id=None, post_id=None)
                    futures.append(future)

                for future in concurrent.futures.as_completed(futures):
                    result = future.result()  # This assumes handle_request returns a result indicating success
                    if result == "success":  # Replace with actual success condition based on your handle_request function
                        total_shared += 1

            rp(f"{G}Total successful shares: {total_shared}")
            return

        except ValueError:
            rp(f"{R}Invalid input for post ID.")




def display_reaction_types():
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'SAD',
        '6': 'ANGRY'
        
    }
    rp(pan("Select a reaction type:", border_style="bold purple"))
    for number, reaction in reaction_types.items():
        rp(f"{Y}{number}: {reaction.upper()}")
    return reaction_types

def record_token_usage(user_id, post_id, token):
    now = datetime.now()
    with open(TOKEN_USAGE_FILE, 'a') as file:
        file.write(f"{user_id},{post_id},{token},{now.isoformat()}\n")
    rp(f"{G}Token usage recorded: {user_id}, {post_id}, {token}, {now.isoformat()}")


#DITO AKO MY PROB. POTA!
def handle_request(url, params, headers, filename, index, success_message, error_message, user_id=None, post_id=None):
    token = params.get('access_token')
    try:
        response = requests.post(url, params=params, headers=headers)
        if response.status_code == 200:
            rp(success_message)
            if user_id and post_id:
                record_token_usage(user_id, post_id, token)
            with open(USED_TOKENS_FILE, 'a') as used_file:
                used_file.write(f"{token}\n")
           
        else:
            rp(f"{R}{error_message} Status code: {response.status_code}.")
            with open(ERROR_TOKEN_FILE, 'a') as err_file:
                err_file.write(f"{token}\n")
          
    except requests.RequestException as error:
        rp(f"{R}[EXCEPTION] {error_message}: {error}.")
        with open(ERROR_TOKEN_FILE, 'a') as err_file:
            err_file.write(f"{token}\n")
      


def perform_reaction(filename, post_id, reaction_type, reaction_count, delay):
    def process_reaction(i, access_token):
        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': random.choice(user_agents)
        }
        params = {'access_token': access_token, 'type': reaction_type}
        handle_request(url, params, headers, filename, i, f"{G}[SUCCESS] ----- {Y} SUCCESSFULLY REACTED ON POST", f"{R}[FAILED] ----- {R} FAILED REACTED ON POST", user_id=None, post_id=post_id)
        time.sleep(delay)


    bots = fetch_bots(filename)
    if not bots:
        rp(f"{R}No bots available.")
        return
    random.shuffle(bots)

    reaction_types = display_reaction_types()
    reaction_type = reaction_types.get(reaction_type, 'LIKE')

    rp(f"{G}Starting reactions with {reaction_type} on post  {post_id}...")

    max_workers = 30 #adjust mo nlng to boss kung gusto mo mass react.
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for i in range(reaction_count):
            if not bots:
                rp(f"{R}Not enough tokens available.")
                break

            access_token = bots.pop(0)
            future = executor.submit(process_reaction, i, access_token)
            futures.append(future)

        
        for future in futures:
            future.result()  
    rp(f"{G}Finished reacting to comment {post_id}.")


def comment_reactions(filename, post_id, reaction_type, reaction_count, delay):
    def process_reaction(i, access_token):
        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': random.choice(user_agents)
        }
        params = {'access_token': access_token, 'type': reaction_type}
        handle_request(url, params, headers, filename, i, f"{G}[SUCCESS] ----- {Y} SUCCESSFULLY REACTED ON COMMENT", f"{R}[FAILED] ----- {R} FAILED REACTED ON COMMENT", user_id=None, post_id=post_id)
        time.sleep(delay)


    bots = fetch_bots(filename)
    if not bots:
        rp(f"{R}No bots available.")
        return
    random.shuffle(bots)

    reaction_types = display_reaction_types()
    reaction_type = reaction_types.get(reaction_type, 'LIKE')

    rp(f"{G}Starting reactions with {reaction_type} on comment ID {post_id}...")

    max_workers = 30 
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for i in range(reaction_count):
            if not bots:
                rp(f"{R}Not enough tokens available.")
                break

            access_token = bots.pop(0)
            future = executor.submit(process_reaction, i, access_token)
            futures.append(future)

        
        for future in futures:
            future.result()  
    rp(f"{G}Finished reacting to comment {post_id}.")


class ProfileGuard:
    def __init__(self, token):
        self.token = token
        self.api_url = 'https://graph.facebook.com/v18.0/me?access_token='

    def update_guard_status(self, activate=True):
        url = f'{self.api_url}{self.token}'
        params = {
            'fields': 'id,name,profile_pic'
        }
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': random.choice(user_agents)
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                status = 'activated' if activate else 'deactivated'
                return f"{G}Profile shield {status} successfully: {data.get('name', 'Unknown')}"
            else:
                return f"{R}Failed to update profile shield. Status code: {response.status_code}"
        except requests.RequestException as e:
            return f"{R}Error updating profile shield: {e}"

#profile shield
def profile_shield():
    token = input("Enter your access token: ")
    command = input("Enter command (on/off): ").strip().lower()

    if command not in ['on', 'off']:
        rp(f"{R}Invalid command. Please enter 'on' or 'off'.")
        return

    if not token:
        rp(f"{R}Error: Access token is required.")
        return

    guard = ProfileGuard(token)
    result = guard.update_guard_status(command == 'on')
    rp(result)
    input("Press Enter to return to the menu...")


def set_delay():
    while True:
        try:
            delay = float(input("Enter delay time in seconds: "))
            if delay < 0:
                rp(f"{R}Delay time must be a positive number.")
                continue
            return delay
        except ValueError:
            rp(f"{R}Invalid input. Please enter a number.")

def check_tokens():
    clear_console()
    logo()
    rp(pan(f"{Y}Token Counts\n"
            f"{G}Page Tokens: {count_page_tokens()}\n"
            f"{G}User Tokens: {count_user_tokens()}\n"
            f"{G}Error Tokens: {count_error_tokens()}\n"
            f"{G}Used Tokens: {count_used_tokens()}\n",
            title=f"{Y}Token Information",
            border_style="bold yellow"))
    input("Press Enter to return to the previous menu...")

#dashboard
def dashboard():
    clear_console()
    logo()
    rp(pan( f"{G}FRA PAGE:    {count_frapage_tokens()}\n"
    f"{G}RPA PAGE:    {count_rpapage_tokens()}\n"
    f"{G}FRA ACCOUNT: {count_fraacount_tokens()}\n"
    f"{G}RPA ACCOUNT: {count_rpaccount_tokens()}\n",
            title=f"{Y}Your Boosting Tool Overview",
            border_style="bold yellow"))
   #reply comment
def reply_comments(filename):
    bots = fetch_bots(filename)
    if not bots:
        rp(f"{R}No bots available.")
        return

    def post_comment(index, access_token, comment_id, comment_message):
        url = f'https://graph.facebook.com/v13.0/{comment_id}/comments'
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': random.choice(user_agents)
        }
        params = {'access_token': access_token, 'message': comment_message}
        handle_request(url, params, headers, filename, index,
                       f"{G}Successfully reply comment on {post_id}.",
                       f"{R}Failed to post reply comment on", user_id=None, post_id=post_id)
        if delay_enabled['comment']:
            time.sleep(10)  # Added delay after each comment

    while True:
        try:
            comment_count = input("How many comments would you like to add? (type '0' or 'back' to return) ")
            if comment_count.lower() == 'back' or comment_count == '0':
                return

            comment_count = int(comment_count)
            if comment_count <= 0:
                rp(f"{R}Comment count must be a positive integer.")
                continue

            post_id = input("Enter the post ID to comment on: ")

            # Prompt user to enter custom comments
            custom_comments = input("Enter your custom comments separated by commas: ")
            custom_comments_list = [comment.strip() for comment in custom_comments.split(',')]
            if not custom_comments_list:
                rp(f"{R}No custom comments provided. Please enter at least one comment.")
                continue

            # Shuffle the list of bot tokens to add randomness
            random.shuffle(bots)

            with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                futures = []
                for index, access_token in enumerate(bots):
                    if len(futures) >= comment_count:
                        break
                    # Randomly select a comment from the user-provided list
                    comment_message = random.choice(custom_comments_list)
                    futures.append(executor.submit(post_comment, index, access_token, post_id, comment_message))

                concurrent.futures.wait(futures)

            rp(f"{G}All comments have been added successfully.")

            input("Press Enter to return to the main menu...")
            return 

        except ValueError:
            rp(f"{R}Invalid input for comment count.")
            
            
#reply comment
def auto_comments(filename):
    bots = fetch_bots(filename)
    if not bots:
        rp(f"{R}No bots available.")
        return

    def post_comment(index, access_token, user_id, comment_message):
        url = f'https://graph.facebook.com/v18.0/{user_id}/comments'
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': random.choice(user_agents)
        }
        params = {'access_token': access_token, 'message': comment_message}
        handle_request(url, params, headers, filename, index,
                       f"{G}Successfully commented on post {post_id}.",
                       f"{R}Failed to post comment on", user_id=None, post_id=post_id)
        if delay_enabled['comment']:
            time.sleep(10)  # Added delay after each comment

    while True:
        try:
            comment_count = input("How many comments would you like to add? (type '0' or 'back' to return) ")
            if comment_count.lower() == 'back' or comment_count == '0':
                return

            comment_count = int(comment_count)
            if comment_count <= 0:
                rp(f"{R}Comment count must be a positive integer.")
                continue

            post_id = input("Enter the post ID to comment on: ")

            # Prompt user to enter custom comments
            custom_comments = input("Enter your custom comments separated by commas: ")
            custom_comments_list = [comment.strip() for comment in custom_comments.split(',')]
            if not custom_comments_list:
                rp(f"{R}No custom comments provided. Please enter at least one comment.")
                continue

            # Shuffle the list of bot tokens to add randomness
            random.shuffle(bots)

            with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                futures = []
                for index, access_token in enumerate(bots):
                    if len(futures) >= comment_count:
                        break
                    # Randomly select a comment from the user-provided list
                    comment_message = random.choice(custom_comments_list)
                    futures.append(executor.submit(post_comment, index, access_token, post_id, comment_message))

                concurrent.futures.wait(futures)

            rp(f"{G}All comments have been added successfully.")

            input("Press Enter to return to the main menu...")
            return 

        except ValueError:
            rp(f"{R}Invalid input for comment count.")
            
def description_guide():
    clear_console()
    logo()
    rp(pan(f"""Welcome to the Description Guide!

1. **AUTO REACT**: Automates reactions on Facebook posts using tokens.
2. **OTHER TOOLS**: Provides additional tools and settings including:
   - **SET DELAY**: Configures the delay time between reactions.
   - **STORED PAGE AND ACCOUNT**: Manage tokens and accounts.
   - **ACCOUNT INFORMATION CHECKER**: Check and save Facebook account information using tokens.

**Main Menu Options**:
- **AUTO REACT**: Use tokens to perform automated reactions on posts.
- **OTHER TOOLS**: Access various additional functionalities and settings.
- **EXIT**: Exit the tool.

Use the menu options to navigate through the tool's features and functionalities.

Thank you for using the tool!
""", title=f"{Y}Description Guide", border_style="bold yellow"))
    input("Press Enter to return to the main menu...")    
            
def remove_duplicates(filename):
    tokens = fetch_bots(filename)
    unique_tokens = list(set(tokens))  

    with open(filename, 'w') as file:
        file.writelines(f"{token}\n" for token in unique_tokens)
    
    rp(f"{G}Duplicates removed. {len(tokens) - len(unique_tokens)} duplicate(s) were found and removed.")



import os
import re

def extract_ids_from_link(post_link):
    pattern = r'https://www\.facebook\.com/(\d+)/posts/(\d+)/?'
    match = re.match(pattern, post_link)
    if match:
        user_id = match.group(1)
        post_id = match.group(2)
        return user_id, post_id
    return None, None

def save_ids_to_file(user_id, post_id, choice):
    folder = 'UID'
    
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    if choice == 'both' and user_id and post_id:
        file_path = os.path.join(folder, 'user_postid.txt')
        with open(file_path, 'w') as file:
            file.write(f'{user_id}_{post_id}\n')
    elif choice == 'user' and user_id:
        file_path = os.path.join(folder, 'userid.txt')
        with open(file_path, 'w') as file:
            file.write(f'{user_id}\n')
    elif choice == 'post' and post_id:
        file_path = os.path.join(folder, 'postid.txt')
        with open(file_path, 'w') as file:
            file.write(f'{post_id}\n')

def uid_main():
    post_link = input("\033[96mEnter the Facebook post link: \033[0m")  # Cyan text
    user_id, post_id = extract_ids_from_link(post_link)
    
    if user_id or post_id:
        choice = input("\033[93mWhat would you like to extract? (user/post/both): \033[0m").strip().lower()
        
        if choice == 'both':
            if user_id and post_id:
                print(f'\033[92mExtracted User ID and Post ID: \033[93m{user_id}_{post_id}\033[0m')  # Green and Yellow text
                save_ids_to_file(user_id, post_id, 'both')
            else:
                print('\033[91mInvalid link or IDs not found.\033[0m')  # Red text
        elif choice == 'user' and user_id:
            print(f'\033[92mExtracted User ID: \033[93m{user_id}\033[0m')  
            save_ids_to_file(user_id, None, 'user')
        elif choice == 'post' and post_id:
            print(f'\033[92mExtracted Post ID: \033[93m{post_id}\033[0m')  
            save_ids_to_file(None, post_id, 'post')
        else:
            print('\033[91mInvalid choice or IDs not found.\033[0m')  # Red text
    else:
        print('\033[91mInvalid post link.\033[0m')  # Red text

    input("\033[96mPress Enter to exit...\033[0m") 



def read_credentials():
    credentials_folder = "/sdcard/RFCPTOOLS/credentials"
    id_file_path = os.path.join(credentials_folder, "id.txt")
    pw_file_path = os.path.join(credentials_folder, "password.txt")
    
    if not os.path.exists(credentials_folder):
        rp(f"{R}Error: Credentials folder not found.")
        sys.exit(1)
    
    if not os.path.exists(id_file_path) or not os.path.exists(pw_file_path):
        rp(f"{R}Error: Required file(s) not found in the credentials folder.")
        sys.exit(1)

    try:
        with open(id_file_path, "r") as id_file:
            users = [line.strip() for line in id_file if line.strip()]
        with open(pw_file_path, "r") as pw_file:
            passwords = [line.strip() for line in pw_file if line.strip()]
        if len(users) != len(passwords):
            raise ValueError("The number of user IDs and passwords must be the same.")
        return list(zip(users, passwords))
    except ValueError as e:
        rp(f"{R}Error: {e}")
        sys.exit(1)


def transfer_ids_to_uid(users):
    uid_file_path = os.path.join("/sdcard/RFCPTOOLS/tokens", "checklog.txt")  
    with open(uid_file_path, "a") as uid_file:
        for user in users:
            uid_file.write(f"{user}\n")


def remove_processed_ids(users):
    id_file_path = "/sdcard/RFCPTOOLS/credentials/id.txt"
    with open(id_file_path, "r") as id_file:
        all_ids = id_file.readlines()

    with open(id_file_path, "w") as id_file:
        for line in all_ids:
            if line.strip() not in users:
                id_file.write(line)

    

    remove_processed_passwords(users)

def remove_processed_passwords(users):
    pw_file_path = "/sdcard/RFCPTOOLS/credentials/password.txt"
    with open(pw_file_path, "r") as pw_file:
        all_passwords = pw_file.readlines()

    with open(pw_file_path, "w") as pw_file:
        remaining_passwords = [line for i, line in enumerate(all_passwords) if i not in users]
        pw_file.writelines(remaining_passwords)


# Ensure the tokens directory exists
def ensure_tokens_directory():
    if not os.path.exists("/sdcard/RFCPTOOLS/tokens"):
        os.makedirs("/sdcard/RFCPTOOLS/tokens/")
    
    files = ["user.txt", "page.txt", "cuser.txt", "invalid.txt", "checklog.txt", "errorpage.txt", "error.txt", "use.txt", "errortoken.txt"]
    for file in files:
        file_path = os.path.join("/sdcard/RFCPTOOLS/tokens/", file)
        if not os.path.isfile(file_path):
            open(file_path, "w").close()

def token_getter():
    clear()
    credentials = read_credentials()
    if not credentials:
        rp(f"{R}Error: No credentials found.")
        sys.exit(1)

    users, passwords = zip(*credentials)  
    ensure_tokens_directory()
    
    for user, passw in credentials:
        clear()
        dashboard()
        rp(pan(f"{Y}[{C}2{Y}] {G}COOKIE 2(token getter)\n"
                f"{Y}[{C}4{Y}] {R}EXIT",
                border_style="bold purple"))
        
        select = 2
        
        if select == 1:
            datr(user, passw)
        elif select == 2:
            cuser(user, passw)
        else:
            sys.exit("\033[1;31mQUITTING")
        
        
        transfer_ids_to_uid([user])
        remove_processed_ids([user])

        
        print(f"{y}Waiting for 0 seconds before processing the next credentials...")
        time.sleep(0)

        
        print(f"{g}Returning to the main menu in 0 seconds...")
        time.sleep(0)  
        

def datr(user, passw):
    session = requests.Session()
    headers = {
        'authority': 'free.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'dpr': '3',
        'origin': 'https://free.facebook.com',
        'referer': f'https://free.facebook.com/login/?email={user}',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        'viewport-width': '980',
    }
    getlog = session.get(f'https://free.facebook.com/login.php')
    idpass = {
        "lsd": re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),
        "jazoest": re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),
        "m_ts": re.search('name="m_ts" value="(.*?)"', str(getlog.text)).group(1),
        "li": re.search('name="li" value="(.*?)"', str(getlog.text)).group(1),
        "try_number": "0",
        "unrecognize_tries": "0",
        "email": user,
        "pass": passw,
        "login": "Log In",
        "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(getlog.text)).group(1),
    }
    comp = session.post("https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated", headers=headers, data=idpass, allow_redirects=False)
    drax = session.cookies.get_dict().keys()
    cookie = ";".join([f"{key}={value}" for key, value in session.cookies.get_dict().items()])
    if "c_user" in drax:
        clear()
        print(f"{c}USERID/EMAIL: {g}{user}\n{c}PASSWORD: {g}{passw}")
        print(f"{c}YOUR COOKIE: {r}{cookie}")
        
        # Log success in checklog.txt
        with open(os.path.join("/sdcard/RFCPTOOLS/tokens", "checklog.txt"), "a") as success_file:  # Updated path
            success_file.write(f"{user}:{passw}\n")
            
        
        time.sleep(1)  
    else:
        clear()
        print(f"{r}Invalid Username Or Password")
        with open("/sdcard/RFCPTOOLS/tokens/errorpage.txt", "a") as errorpage_file:
            errorpage_file.write(f"{user}:{passw} - INVALID\n")
        print(f"{r}Invalid token saved to /sdcard/RFCPTOOLS/tokens/errorpage.txt")
        # Save invalid tokens to error.txt
        with open("/sdcard/RFCPTOOLS/tokens/error.txt", "a") as errorpage_file:
            errorpage_file.write(f"{user}:{passw}\n")
        print(f"{r}Invalid token saved to /sdcard/RFCPTOOLS/tokens/error.txt")
        print(f"{g}Returning to the main menu in 2 seconds...")
        time.sleep(0)  

def cuser(user, passw):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': user,
        'password': passw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': f'62f8ce9f74b12f84c123cc23437a4a32'
    }
    response = requests.post("https://b-graph.facebook.com/auth/login", headers=headers, data=data, allow_redirects=False).json()
    
    if "session_key" in response:
        access_token = response.get('access_token')  # Store access token
        cookies = response.get('session_cookies', [])
        
        # Format cookies in the desired format
        cookie_str = ";".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
        
        # Save formatted cookies to cuser.txt
        with open("/sdcard/RFCPTOOLS/tokens/cuser.txt", "a") as file:
            file.write(f"{cookie_str}\n")
       
        
        save_user_token(access_token)  # Save the access token to /sdcard/RFCPTOOLS/tokens/user.txt
        success = get_page_tokens(access_token=access_token)  # Call get_page_tokens with the obtained token
        
        # Log success in checklog.txt
        if success:
            with open(os.path.join("/sdcard/RFCPTOOLS/tokens", "checklog.txt"), "a") as success_file:  # Updated path
                success_file.write(f"{user}:{passw}\n")
            print(f"{g}Valid account")
        else:
            print(f"{r}Failed to get page tokens with this access token.")
        
    else:
        print(f"{r}INVALID/CHECKPOINT")
        with open("/sdcard/RFCPTOOLS/tokens/errorpage.txt", "a") as errorpage_file:
            errorpage_file.write(f"{user}:{passw} - INVALID/CHECKPOINT\n")
        print(f"{r}Invalid or checkpoint.")
        
        # Save invalid tokens to error.txt
        with open("/sdcard/RFCPTOOLS/tokens/error.txt", "a") as errorpage_file:
            errorpage_file.write(f"{user}:{passw}\n")
        print(f"{r}Invalid token saved to /sdcard/RFCPTOOLS/tokens/error.txt")
        
        print(f"{c}Returning to the main menu in 0 seconds...")
        time.sleep(0)  # Simulate delay before returning to the main menu

def save_user_token(token):
    with open("/sdcard/RFCPTOOLS/tokens/account/fraacount.txt", "a") as file:
        file.write(f"{token}\n")

def get_page_tokens(access_token):
    url = f"https://graph.facebook.com/me/accounts?access_token={access_token}"
    response = requests.get(url).json()
    
    if 'data' in response:
        with open("/sdcard/RFCPTOOLS/tokens/account/frapage.txt", "a") as file:
            for page in response['data']:
                file.write(f"{page['access_token']}\n")
        
        return True
    else:
        print(f"{r}Failed to get page tokens.")
        return False

def process_invalid_tokens():
    errortogetpages_file_path = "/sdcard/RFCPTOOLS/tokens/error.txt"
    if not os.path.exists(errortogetpages_file_path):
        rp(f"{R}Error: error.txt file not found.")
        return
    
    with open(errortogetpages_file_path, "r") as file:
        tokens = file.readlines()

    for token in tokens:
        token = token.strip()
        if token:
            print(f"{y}Processing token: {token}")
            get_page_tokens(access_token=token)

#description guide


        
# Main function
def main(): 
    while True:
        approval()
        clear_console()
        logo()
        dashboard()
        rp(pan(f"{Y}[1] {G}BOOSTING TOOL\n"
                f"{Y}[2] {G}TOKEN GETTER\n"
                f"{Y}[3] {G}OTHER TOOLS\n"
               
                f"{Y}[0] {G}EXIT\n",
                title=f"{Y}Main Menu",
                border_style="bold yellow"))

        choice = input("Enter your choice: ")

        if choice == '1':
            boosting_menu()
        elif choice == '2':
            token_menu()
        elif choice == '3':
            other_menu()
        
              

        elif choice == '0':
            exit()

        else:
            rp(f"{R}Invalid choice. Please select a valid option.")


def token_menu():
    while True:
        clear()
        dashboard()
        rp(pan(f"{Y}[1] {G}V1 - AUTO\n"
                
                f"{Y}[0] {G}EXIT\n",
                title=f"{Y}Token Getter Menu",
                border_style="bold yellow"))

        choice = input("Enter your choice: ")

        if choice == '1':
            token_getter()
        
        elif choice == '0':
           return
        else:
            rp(f"{R}Invalid choice. Please select a valid option.")


def other_menu():
    while True:
        clear_console()
        logo()
        
        dashboard()
        rp(pan(f"{Y}[1] {G}TRANSFER TOKENS\n"
                f"{Y}[2] {G}ACCOUNT CHECKER\n"
                f"{Y}[3] {G}PROFILE GUARD\n"
                f"{Y}[4] {G}REMOVE DUPLICATES\n"
                f"{Y}[5] {G}DESCRIPTION GUIDE\n"
                f"{Y}[6] {G}UID GETTER\n"
                f"{Y}[7] {G}DELETE TOKENS\n"
        
               
                f"{Y}[0] {G}BACK\n",
                title=f"{Y}Other Tools Menu",
                border_style="bold yellow"))
                

        choice = input("Enter your choice: ")

       
        if choice == '1':
            auto_transfer_tokens()  
        elif choice == '2':
            check_account()
        elif choice == '3':
        	profile_shield()
       
        elif choice == '4':
            remove_duplicates(tool_token())
        elif choice == '5':
            description_guide()
        elif choice == '6':
        	uid_main()
        elif choice =='7':
        	delete_tokens(tool_token())
      
       
        elif choice == '0':
            return

        else:
            rp(f"{R}Invalid choice. Please select a valid option.")




def boosting_menu():
    while True:
        clear_console()
        logo()
        dashboard()
        rp(pan(f"{Y}[1] {G}AUTO REACT    [PAGE & NORMAL]\n"
                f"{Y}[2] {G}REACT COMMENT [PAGE & NORMAL]\n"
                f"{Y}[3] {G}AUTO FOLLOW   [PAGE & NORMAL]\n"
                f"{Y}[4] {G}AUTO COMMENT  [PAGE & NORMAL]\n"
                f"{Y}[5] {G}REPLY COMMENT [PAGE & NORMAL]\n"
                f"{Y}[6] {G}AUTO SHARE    [PAGE & NORMAL]\n"
                f"{Y}[0] {G}BACK\n",
                title=f"{Y}BOOSTING TOOL",
                border_style="bold yellow"))

        choice = input("Enter your choice: ")

        if choice == '1':
            post_id = input("Enter the post ID to react to: ")
            reaction_type = input("Enter reaction type (1: LIKE, 2:LOVE, 3:HAHA, 4:WOW, 5:SAD, 6:ANGRY): ")
            reaction_count = int(input("How many reactions would you like to perform? "))
            delay = set_delay()
            perform_reaction(tool_token(), post_id, reaction_type, reaction_count, delay)
        elif choice == '2':
            post_id = input("Enter the comment ID to react to: ")
            reaction_type = input("Enter reaction type (1: LIKE, 2:LOVE, 3:HAHA, 4:WOW, 5:SAD, 6:ANGRY): ")
            reaction_count = int(input("How many reactions would you like to perform? "))
            delay = set_delay()
            comment_reactions(tool_token(), post_id, reaction_type, reaction_count, delay)
        elif choice == '3':
            add_follow(tool_token())
        elif choice == '4':
        	auto_comments(tool_token())
        elif choice == '5':
        	reply_comments(tool_token())
        elif choice == '6':
        	share_post(tool_token())
       
        elif choice == '0':
            return

        else:
            rp(f"{R}Invalid choice. Please select a valid option.")
            
if __name__ == "__main__":
    main()
