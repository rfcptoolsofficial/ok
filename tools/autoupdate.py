import os
import subprocess
import platform

# Path to your local repository
repo_path = 'ok'  # Adjust this if needed

def clear_console():
    """Clear the console based on the operating system."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def update_repo():
    try:
        # Clear the console
        clear_console()

        # Check if the repository directory exists
        if not os.path.isdir(repo_path):
            print(f"The directory '{repo_path}' does not exist. Cloning the repository...")
            # Clone the repository if it doesn't exist
            subprocess.run(['git', 'clone', 'https://github.com/rfcptoolsofficial/ok.git', repo_path], check=True)
            print(f"Repository cloned successfully into '{repo_path}'.")
            os.chdir(repo_path)  # Change to the new repo directory
        else:
            os.chdir(repo_path)

        # Fetch the latest changes
        subprocess.run(['git', 'fetch'], check=True)

        # Check out the main branch (or the branch you're using)
        subprocess.run(['git', 'checkout', 'main'], check=True)

        # Pull the latest changes
        subprocess.run(['git', 'pull'], check=True)

        print("Repository updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during Git command: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    update_repo()
