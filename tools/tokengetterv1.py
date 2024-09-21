import os
import time
import requests
import random
from colorama import Fore, Style, init

init()  # Initialize Colorama

def clear_console():
    """Clear the console depending on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    logo = r"""
             ██████╗ ███████╗ ██████╗██████╗ 
             ██╔══██╗██╔════╝██╔════╝██╔══██╗
             ██████╔╝█████╗  ██║     ██████╔╝
             ██╔══██╗██╔══╝  ██║     ██╔═══╝ 
             ██║  ██║██║     ╚██████╗██║     
             ╚═╝  ╚═╝╚═╝      ╚═════╝╚═╝  [V1]
                  ᴘᴀɢᴇ ᴛᴏᴋᴇɴ ɢᴇᴛᴛᴇʀ
    """
    print(Fore.MAGENTA + logo + Style.RESET_ALL)

def generate_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.277",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.70",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    ]
    return random.choice(user_agents)

def get_user_token(email, password):
    url = 'https://b-api.facebook.com/method/auth.login'
    form = {
        'adid': 'e3a395f9-84b6-44f6-a0ce-fe83e934fd4d',
        'email': email,
        'password': password,
        'format': 'json',
        'device_id': '67f431b8-640b-4f73-a077-acc5d3125b21',
        'cpl': 'true',
        'family_device_id': '67f431b8-640b-4f73-a077-acc5d3125b21',
        'locale': 'en_US',
        'client_country_code': 'US',
        'credentials_type': 'device_based_login_password',
        'generate_session_cookies': '1',
        'generate_analytics_claim': '1',
        'generate_machine_id': '1',
        'currently_logged_in_userid': '0',
        'irisSeqID': 1,
        'try_num': '1',
        'enroll_misauth': 'false',
        'meta_inf_fbmeta': 'NO_FILE',
        'source': 'login',
        'machine_id': 'KBz5fEj0GAvVAhtufg3nMDYG',
        'meta_inf_fbmeta': '',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '882a8490361da98702bf97a021ddc14d',
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32'
    }

    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-friendly-name': 'fb_api_req_friendly_name',
        'x-fb-http-engine': 'Liger',
        'accept-language': 'fil-PH,fil;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': generate_user_agent()
    }

    response = requests.post(url, data=form, headers=headers)
    response.raise_for_status()
    return response.json()

def get_page_tokens(user_token):
    url = 'https://graph.facebook.com/me/accounts'
    params = {
        'access_token': user_token
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def save_to_file(filename, content):
    with open(filename, 'a') as file:  # Changed to 'a' mode to append content
        file.write(content + "\n")  # Ensure each token is on a new line
    print(Fore.GREEN + f"Token successfully saved to {filename}" + Style.RESET_ALL)

def process_credentials():
    id_file = '/storage/RFCPTOOLS/credentials/id.txt'
    password_file = '/storage/RFCPTOOLS/credentials/password.txt'

    if not os.path.exists(id_file) or not os.path.exists(password_file):
        print(Fore.RED + "Credentials files not found. Ensure id.txt and password.txt exist." + Style.RESET_ALL)
        return

    with open(id_file, 'r') as id_file_content:
        emails = [line.strip() for line in id_file_content.readlines()]
    with open(password_file, 'r') as password_file_content:
        passwords = [line.strip() for line in password_file_content.readlines()]

    # Debugging: Print the contents of the files
    print(Fore.CYAN + "Emails in id.txt:" + Style.RESET_ALL)
    print('\n'.join(emails))
    print(Fore.CYAN + "Passwords in password.txt:" + Style.RESET_ALL)
    print('\n'.join(passwords))

    if not emails or not passwords:
        print(Fore.RED + "No credentials found in the files." + Style.RESET_ALL)
        return

    tokens_saved = False
    used_credentials = set()  # Track used credentials to avoid duplicates

    for email, password in zip(emails, passwords):
        if (email, password) in used_credentials:
            continue  # Skip if this credential set has already been processed

        if not email or not password:
            print(Fore.RED + "Empty email or password found." + Style.RESET_ALL)
            continue

        try:
            # Get user token
            user_response = get_user_token(email, password)
            user_token = user_response.get('access_token')

            if user_token:
                print(Fore.YELLOW + f"User Token: {user_token}" + Style.RESET_ALL)
                # Save user token to file
                save_to_file('/sdcard/RFCPTOOLS/tokens/user.txt', user_token)

                # Get page tokens using user token
                pages_response = get_page_tokens(user_token)
                pages = pages_response.get('data', [])

                page_tokens = "\n".join(page.get('access_token') for page in pages if page.get('access_token'))
                if page_tokens:
                    # Save page tokens to file
                    save_to_file('/storage/RFCPTOOLS/tokens/page.txt', page_tokens)
                else:
                    print(Fore.RED + "No page tokens found." + Style.RESET_ALL)

                tokens_saved = True
                used_credentials.add((email, password))

        except requests.RequestException as e:
            print(Fore.RED + f"HTTP request failed: {e}" + Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED + f"Error decoding JSON: {e}" + Style.RESET_ALL)

        # Wait 2 seconds before processing the next set of credentials
        print(Fore.YELLOW + "Waiting 10 seconds before processing the next credential set..." + Style.RESET_ALL)
        time.sleep(2)

    if not tokens_saved:
        print(Fore.RED + "No valid tokens were saved." + Style.RESET_ALL)

    # Remove used credentials from files
    with open(id_file, 'w') as id_file_content, open(password_file, 'w') as password_file_content:
        remaining_emails = []
        remaining_passwords = []
        for email, password in zip(emails, passwords):
            if (email, password) not in used_credentials:
                remaining_emails.append(email + "\n")
                remaining_passwords.append(password + "\n")
        id_file_content.writelines(remaining_emails)
        password_file_content.writelines(remaining_passwords)

def print_menu():
    print(Fore.MAGENTA + "Facebook Token Utility Menu" + Style.RESET_ALL)
    print(Fore.CYAN + "1. Process Credentials" + Style.RESET_ALL)
    print(Fore.CYAN + "2. Exit" + Style.RESET_ALL)

def menu():
    while True:
        print_menu()
        choice = input(Fore.CYAN + "Enter your choice (1 or 2): " + Style.RESET_ALL).strip()

        if choice == '1':
            process_credentials()
        elif choice == '2':
            print(Fore.GREEN + "Exiting the program. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice, please enter 1 or 2." + Style.RESET_ALL)

if __name__ == "__main__":
    clear_console()  # Clear the console before running the menu
    display_logo()   # Display the logo
    menu()
