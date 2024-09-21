import os
import subprocess

# Path to your local repository
repo_path = 'ok'  # Assuming you cloned it in the current working directory

def update_repo():
    try:
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
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    update_repo()
