import subprocess
import os
import requests
import logging
from colorama import init, Fore, Style
import marshal, time
import platform

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

#__________________| COLOUR |__________________#
A = '\x1b[1;97m'; Y = '\033[1;33m'; G = '\033[1;96m'; R = '\x1b[38;5;196m'; B = '\x1b[38;5;8m'; G1 = '\x1b[38;5;48m'; G2 = '\x1b[38;5;47m'; G3 = '\x1b[38;5;48m'; X1 = '\x1b[38;5;14m'; X2 = '\x1b[38;5;123m'; X5 = '\x1b[38;5;121m'

#__________________| Logo |__________________#
# ASCII Art Logo
logo = (f'''
   \x1b\033[38;5;196m ██████╗ ███████╗ ██████╗ ███████╗ 
   \x1b\033[38;5;197m ██╔══██╗██╔════╝██╔════╝ ██╔══██╗ 
   \x1b\033[38;5;198m ██████╔╝█████╗  ██║       ██████╔╝ 
   \x1b\033[38;5;199m ██╔══██╗██╔══╝  ██║       ██╔═══╝  
   \x1b\033[38;5;196m ██║  ██║██║     ╚██████╗ ██║       
   \x1b\033[38;5;197m ╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝       

 {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{X2}【{X5}✦{X2}】{Y}DEVELOPER   {B}»----{A}➤ {G3}RFCP TEAM
{X2}【{X5}✦{X2}】{Y}ABOUT    {B}»----{A}➤ {G3}ONLY ADMIN CAN USE THIS TOOL.
{X2}【{X5}✦{X2}】{Y}TOOL'S NAME {B}»----{A}➤ {G3}[\x1b\033[38;5;196m\x1b[1;97m\x1b[1;41mPYTHON ENCRYPTION\x1b[0m{G3}]
 {X5}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')

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
    print(Fore.CYAN + logo + Style.RESET_ALL)  # Display logo in cyan

    # Get a unique identifier based on the platform
    if platform.system() == "Windows":
        user_id = os.getpid()  # Use process ID as a substitute
    else:
        user_id = os.geteuid()  # Effective user ID for Unix-like systems

    uuid = f"{user_id}DS{user_id}"
    key = f"RFCP-{uuid}"

    print("\033[1;37m [\u001b[36m•\033[1;37m] You Need Approval To Use This Tool   \033[1;37m")
    print(f"\033[1;37m [\u001b[36m•\033[1;37m] Your Key :\u001b[36m {key}")

    urls = [
        "https://github.com/rfcptools/approvalenc/blob/main/encapproval.txt"
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
        print("\033[1;31m >> Your Key Has Not Been Approved. Exiting...")
        exit()

def main():
    try:
        print(logo)
        approval()
        print('    \033[1;32m┏━━━\033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m]\033[1;32m EXAMPLE :\033[33;1m/sdcard/file.py')
        file = input('    \033[1;32m┗━━━\033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32mFILE NAME :\033[33;1m ')
        fileopen = open(file).read()
        a = compile(fileopen, 'dg', 'exec')
        m = marshal.dumps(a)
        s = repr(m)
        b = ('##-----------------------ADMIN>INFO---------------------------##\n# ENCRYPTION BY :RFCP TEAM\n# VERSION : 1.1\n# GITHUB : https://github.com/rfcptools\n##------------------------MAIN>MENU-------------------------##\nimport marshal\nexec(marshal.loads(' + s + '))')
        c = file.replace('.py', '.py')
        d = open(c, 'w')
        d.write(b)
        d.close()
        print('    \033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32mENCRYPTION SUCCESSFUL >', c)
        print('    \033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        time.sleep(1)
        aq = input('    \033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32mWANT TO ENCRYPT AGAIN? [Y/N]')
        if aq == "":
            print('    \033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32mCOMMAND NOT FOUND !')
            os.sys.exit()
        elif aq.lower() == "y":
            main()
        else:
            if aq.lower() == "n":
                print('    \033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32m➤THANKS FOR USING RFCP ENCRYPTOR\n')
            else:
                print('    \033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32mCOMMAND NOT FOUND!')
                os.sys.exit()
    except IOError:
        print('   \033[97;1m\033[1;31m[\x1b[1;92m+\033[1;31m] \033[1;32mFILE NOT FOUND ! ')
        time.sleep(1)
        main()

if __name__ == '__main__':
    main()
