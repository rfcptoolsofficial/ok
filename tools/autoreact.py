from time import sleep
import re
import requests
import colorama
from colorama import Fore, Style
import os

colorama.init()

def logo():
    print(Fore.CYAN + """
        ██████╗ ███████╗ ██████╗██████╗ 
        ██╔══██╗██╔════╝██╔════╝██╔══██╗
        ██████╔╝█████╗  ██║     ██████╔╝
        ██╔══██╗██╔══╝  ██║     ██╔═══╝ 
        ██║  ██║██║     ╚██████╗██║     
        ╚═╝  ╚═╝╚═╝      ╚═════╝╚═╝ 
           ʟᴇɪɴᴀᴛʜᴀɴ ᴏʀᴇᴍᴏʀ | ꜱʜɪᴋɪ
                                """ + Style.RESET_ALL)

def countdown(delay):
    while delay > 0:
        delay -= 1
        print(Fore.YELLOW + f"[DELAY][X    ][{delay}]" + Style.RESET_ALL, end='\r')
        sleep(1 / 5)
        print(Fore.YELLOW + f"[DELAY][ X   ][{delay}]" + Style.RESET_ALL, end='\r')
        sleep(1 / 5)
        print(Fore.YELLOW + f"[DELAY][  X  ][{delay}]" + Style.RESET_ALL, end='\r')
        sleep(1 / 5)
        print(Fore.YELLOW + f"[DELAY][   X ][{delay}]" + Style.RESET_ALL, end='\r')
        sleep(1 / 5)
        print(Fore.YELLOW + f"[DELAY][    X][{delay}]" + Style.RESET_ALL, end='\r')
        sleep(1 / 5)

class Machine:
    def __init__(self):
        self.session = []
        self.delay = 0
        self.url = None
        self.dict_buff = {'1': 'like', '2': 'love', '3': 'care', '4': 'haha', '5': 'wow', '6': 'sad', '7': 'angry'}
        self.list_select = []
        self.headers_buff = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi-VN,vi;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-AU;q=0.6,en;q=0.5,fr-FR;q=0.4,fr;q=0.3,en-US;q=0.2',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        }
        self.cookies = []
        self.count = 0

    def buff(self, session):
        get_token = session.get('https://machineliker.net/auto-reactions').text
        token = get_token.split('name="_token" value="')[1].split('"')[0]
        hash_ = get_token.split('name="hash" value="')[1].split('"')[0]
        data_buff = {
            'url': self.url,
            'limit': '20',
            'reactions[]': self.list_select,
            '_token': token,
            'hash': hash_
        }
        response = session.post('https://machineliker.net/auto-reactions', headers=self.headers_buff, data=data_buff).text
        if '><strong>Error!</strong>' in response and "You're currently under cooldown periods, please try again after" in response:
            count = re.findall(r'please try again after (\d+) minutes.</p>', response)[0]
            second = int(count) * 60
            print(Fore.RED + f"Please wait {second}s more" + Style.RESET_ALL)
            self.delay = second
        elif 'Order Submitted' in response:
            self.count += 1
            print(Fore.GREEN + f"Successfully Increased +20 Reactions [\033[32;1m{self.count}\033[0m]" + Style.RESET_ALL)
            self.delay = 20
        else:
            print(Fore.RED + "Error" + Style.RESET_ALL)

    def main(self):
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')

        # Ensure the directory and file exist
        os.makedirs('/sdcard/RFCPTOOLS/autoreact', exist_ok=True)
        cookie_path = '/sdcard/RFCPTOOLS/autoreact/cookie.txt'
        
        # Prompt for the number of cookies
        num_cookies = int(input(Fore.YELLOW + "How many cookies do you want to add? " + Style.RESET_ALL))

        # Loop to collect cookies
        for i in range(num_cookies):
            fb_cookie = input(Fore.YELLOW + f"Enter Facebook Cookie #{i + 1}: " + Style.RESET_ALL)
            
            # Save the cookie to the file
            with open(cookie_path, 'a') as cookie_file:
                cookie_file.write(fb_cookie + '\n')
            
            print(Fore.GREEN + "Cookie saved successfully!" + Style.RESET_ALL)

        session = requests.Session()
        
        # Continue with the login process
        a = session.get('https://machineliker.net/login')
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi-VN,vi;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-AU;q=0.6,en;q=0.5,fr-FR;q=0.4,fr;q=0.3,en-US;q=0.2',
            'content-type': 'application/x-www-form-urlencoded',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': session.cookies.get('XSRF-TOKEN').replace('%3D', '='),
        }
        
        # Use the last entered cookie for login
        data = {
            'session': fb_cookie
        }
        response = session.post('https://machineliker.net/login', headers=self.headers, data=data).json()
        if response['success']:
            name = response['user']['name']
            id_ = response['user']['id']
            print(Fore.GREEN + f"Login Successful: {id_} | {name}" + Style.RESET_ALL)
            self.session.append(session)
        else:
            print(Fore.RED + f"Login Failed! Check Facebook Cookie Again {fb_cookie.split('c_user=')[1].split(';')[0]}" + Style.RESET_ALL)

        self.url = input(Fore.YELLOW + "Enter the URL of the post to boost: " + Style.RESET_ALL)
        print(Fore.YELLOW + "Choose the type of reaction to boost (you can choose multiple, e.g., 123):" + Style.RESET_ALL)
        print(Fore.GREEN + """
                1: like
                2: love
                3: care
                4: haha
                5: wow
                6: sad
                7: angry
            """ + Style.RESET_ALL)
        select = input(Fore.YELLOW + "Enter numbers: " + Style.RESET_ALL)
        self.list_select = [self.dict_buff[x] for x in select]
        
        while True:
            for session in self.session:
                self.buff(session)
            countdown(self.delay)

logo()
Machine().main()
