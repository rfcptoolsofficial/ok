import subprocess
import os
from colorama import init, Fore, Style

# Initialize colorama
init()

def check_install_requests():
    try:
        import requests
    except ModuleNotFoundError:
        os.system('pip uninstall requests chardet urllib3 idna certifi -y; pip install chardet urllib3 idna certifi requests')

check_install_requests()

# ────────────────[Git Pull]─────────────────

def update_repository():
    try:
        os.system('clear')
        print(Fore.CYAN + "CHECKING UPDATES...." + Style.RESET_ALL)
        result = subprocess.run(['git', 'pull'], capture_output=True, text=True)
        if result.returncode == 0:
            print(Fore.GREEN + "Update successful!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Update failed: " + result.stderr + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"An error occurred while trying to update: {e}" + Style.RESET_ALL)

update_repository()

# ASCII Art Logo
logo = r"""
             ██████╗ ███████╗ ██████╗██████╗ 
             ██╔══██╗██╔════╝██╔════╝██╔══██╗
             ██████╔╝█████╗  ██║     ██████╔╝
             ██╔══██╗██╔══╝  ██║     ██╔═══╝ 
             ██║  ██║██║     ╚██████╗██║     
             ╚═╝  ╚═╝╚═╝      ╚═════╝╚═╝  [V1.2]
             ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ʟᴇɪɴᴀᴛʜᴀɴ ᴏʀᴇᴍᴏʀ
"""

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error occurred while running {script_name}: {e}{Style.RESET_ALL}")

def main():
    while True:
        clear_console()  # Clear the console before displaying the menu
        print(Fore.CYAN + logo + Style.RESET_ALL)  # Display logo in cyan
        print(Fore.GREEN + "Choose a script to run:" + Style.RESET_ALL)
        print(Fore.YELLOW + "[1.] Boosting Tools" + Style.RESET_ALL)
        print(Fore.YELLOW + "[2.] Auto Create Page" + Style.RESET_ALL)
        print(Fore.YELLOW + "[3.] Remove Invalid Account" + Style.RESET_ALL)
        print(Fore.YELLOW + "[4.] Duplicated Id Checker" + Style.RESET_ALL)
        print(Fore.YELLOW + "[5.] Page Token Extractor" + Style.RESET_ALL)
      
        print(Fore.YELLOW + "[6.] Approval Tools" + Style.RESET_ALL)
        print(Fore.YELLOW + "[7.] Stop" + Style.RESET_ALL)  # Option to stop
        
        choice = input(Fore.MAGENTA + "Enter the number of your choice: " + Style.RESET_ALL)
        
        if choice == '1':
            run_script('tools/boostingtool.py')
        elif choice == '2':
            run_script('tools/autocreatepagev1.py')
        elif choice == '3':
            run_script('tools/removeerror.py') 
        elif choice == '4':
            run_script('tools/idchecker.py') 
        elif choice == '5':
            run_script('tools/pagetokenextractor.py')
        
        elif choice == '6':
            run_script('tools/approvaltools.py')
       
        elif choice == '7':
            print(Fore.GREEN + "Exiting program. Goodbye!" + Style.RESET_ALL)
            break  # Exit the loop to stop the program
        else:
            print(Fore.RED + "Invalid choice. Please choose 1, 2, 3, 4, or 5." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
