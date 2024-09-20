import requests
import os
import time
import random
import platform

# ANSI escape codes for colors
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'  # Reset to default color

# ASCII Logo with placeholders for counts
logo_template = """
           ██████  ████████ ███████ 
           ██   ██    ██    ██      
           ██████     ██    █████   
           ██         ██    ██      
           ██         ██    ███████ 
             PAGE TOKEN  EXTRACTOR              
    
 
 Dashboard:
  - Total Tokens in acc.txt: {token_count}
  - Total Page Tokens in pages.txt: {page_token_count}
"""

# List of user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/90.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36"
]

def create_file_if_not_exists(file_path):
    """Create a file if it does not exist."""
    if not os.path.exists(file_path):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            pass  # Optionally, you can write some initial content here

def load_tokens():
    """Load all tokens from acc.txt."""
    file_path = '/sdcard/RFCPTOOLS/PageExtractor/acc.txt'
    create_file_if_not_exists(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            tokens = f.read().strip().splitlines()  # Read and split tokens into a list
        return tokens
    return []

def save_page_tokens(tokens, token_folder='/sdcard/RFCPTOOLS/PageExtractor/page'):
    """Append page tokens to a file in the tokens folder as plain text."""
    if not os.path.exists(token_folder):
        os.makedirs(token_folder)
    file_path = os.path.join(token_folder, 'pages.txt')
    create_file_if_not_exists(file_path)
    with open(file_path, 'a') as f:
        for token in tokens:
            f.write(f"{token}\n")  # Write each token on a new line

def get_random_user_agent():
    """Return a random user agent from the list."""
    return random.choice(user_agents)

def process_token(access_token):
    """Process a single token and extract page tokens."""
    headers = {'User-Agent': get_random_user_agent()}
    try:
        # Request to get pages managed by the user
        pages_response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={access_token}', headers=headers)
        if pages_response.status_code == 200:
            pages_data = pages_response.json().get("data", [])
            page_tokens = []

            for page in pages_data:
                page_access_token = page.get('access_token')  # Get page access token

                if page_access_token:
                    page_tokens.append(page_access_token)

            save_page_tokens(page_tokens)
            print(f"{Colors.GREEN}Successfully processed and saved page access tokens for token: {access_token}{Colors.RESET}")
        else:
            print(f"{Colors.RED}Failed to retrieve pages for token: {access_token}{Colors.RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{Colors.RED}Exception for token {access_token}: {e}{Colors.RESET}")

def count_lines(file_path):
    """Count the number of lines in a file."""
    create_file_if_not_exists(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return len(f.readlines())
    return 0

def display_dashboard():
    """Display the dashboard with token and page token counts."""
    token_count = count_lines('/sdcard/RFCPTOOLS/PageExtractor/acc.txt')
    page_tokens_count = count_lines('/sdcard/RFCPTOOLS/PageExtractor/page/pages.txt')
    logo = logo_template.format(token_count=token_count, page_token_count=page_tokens_count)
    print(f"{Colors.GREEN}{logo}{Colors.RESET}")

def clear_console():
    """Clear the console screen."""
    # Check the platform and execute the appropriate command
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def main():
    display_dashboard()
    
    tokens = load_tokens()
    
    if not tokens:
        print(f"{Colors.YELLOW}No tokens found.{Colors.RESET}")
        return

    while tokens:
        current_token = tokens.pop(0)  # Get and remove the first token from the list
        
        process_token(current_token)
        
        # Clear console
        clear_console()
        
        display_dashboard()
        
        # Remove the token from acc.txt
        with open('/sdcard/RFCPTOOLS/PageExtractor/acc.txt', 'w') as f:
            f.write("\n".join(tokens))
        
        time.sleep(2)  # Delay before processing the next token

    print(f"{Colors.GREEN}All tokens have been processed.{Colors.RESET}")

if __name__ == "__main__":
    main()
