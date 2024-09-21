import os
import subprocess

# Path to your local repository
repo_path = 'ok'  # Change this if your repo is in a different location

def update_repo():
    try:
        # Ensure the repository path exists
        if not os.path.isdir(repo_path):
            print(f"Error: The directory '{repo_path}' does not exist.")
            return
        
        # Change the current working directory to the repository path
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
