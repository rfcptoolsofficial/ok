import os
import sys
import uuid
import random
import re
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from os import system as sm
from sys import platform as pf
from rich import print as rp
from rich.panel import Panel as pan

# Colors
R = "[bold red]"
G = "[bold green]"
Y = "[bold yellow]"
B = "[bold blue]"
M = "[bold magenta]"
P = "[bold violet]"
C = "[bold cyan]"
W = "[bold white]"

# Random color
def randc():
    return random.choice([R, G, Y, B, M, P, C, W])

# Logo
def logo():
    rp(pan(f"""{randc()}""",
           title=f"{Y}Leinathan Oremor",
           subtitle=f"{R}AUTOMATED ACCOUNT CHECKER",
           border_style="bold purple"))

# Clear screen
def clear():
    if pf in ['win32', 'win64']:
        sm('cls')
    else:
        sm('clear')
    logo()

# Read credentials from files
def read_credentials():
    credentials_folder = "/sdcard/RFCPTOOLS/credentials/"
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

# Transfer IDs to uid.txt
def transfer_ids_to_uid(users):
    uid_file_path = "/sdcard/RFCPTOOLS/successid.txt"
    with open(uid_file_path, "a") as uid_file:
        for user in users:
            uid_file.write(f"{user}\n")

# Remove processed IDs from id.txt
def remove_processed_ids(users):
    id_file_path = "/sdcard/RFCPTOOLS/credentials/id.txt"
    with open(id_file_path, "r") as id_file:
        all_ids = id_file.readlines()

    with open(id_file_path, "w") as id_file:
        for line in all_ids:
            if line.strip() not in users:
                id_file.write(line)

# Ensure the tokens directory exists
def ensure_tokens_directory():
    if not os.path.exists("/sdcard/RFCPTOOLS/tokens"):
        os.makedirs("/sdcard/RFCPTOOLS/tokens")
    
    files = ["/sdcard/RFCPTOOLS/user.txt", "/sdcard/RFCPTOOLS/page.txt", "/sdcard/RFCPTOOLS/cuser.txt", "/sdcard/RFCPTOOLS/invalid.txt", "/sdcard/RFCPTOOLS/successid.txt", "/sdcard/RFCPTOOLS/errorpage.txt", "/sdcard/RFCPTOOLS/errortogetpages.txt"]
    for file in files:
        file_path = os.path.join("tokens", file) if file != "successid.txt" else file
        if not os.path.isfile(file_path):
            open(file_path, "w").close()

def worker(user_pass):
    user, passw = user_pass
    success = cuser(user, passw)  # Process login
    return user, success

def main():
    clear()
    credentials = read_credentials()
    if not credentials:
        rp(f"{R}Error: No credentials found.")
        sys.exit(1)

    ensure_tokens_directory()

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(worker, user_pass): user_pass for user_pass in credentials}
        for future in as_completed(futures):
            user, success = future.result()
            if success:
                rp(f"{G}[SUCCESS] --- Getting the tokens for {user}")
                transfer_ids_to_uid([user])
            else:
                rp(f"{R}[FAILED] --- Getting the tokens for {user}")
            remove_processed_ids([user])

def cuser(user, passw):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'email': user,
        'password': passw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
    }
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW)",
    }
    response = requests.post("https://b-graph.facebook.com/auth/login", headers=headers, data=data, allow_redirects=False).json()
    
    if "session_key" in response:
        access_token = response.get('access_token')
        with open("/sdcard/RFCPTOOLS/tokens/user.txt", "a") as file:
            file.write(f"{access_token}\n")
        return True
    else:
        with open("/sdcard/RFCPTOOLS/tokens/errorpage.txt", "a") as errorpage_file:
            errorpage_file.write(f"{user}:{passw} - INVALID/CHECKPOINT\n")
        return False

if __name__ == "__main__":
    main()
