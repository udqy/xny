import os
import shutil
import subprocess

'''
CACHE_DIR -> default directory to store the files

git_clone()
clean_repo()
update_cache()
'''


CACHE_DIR = os.path.join(os.path.expanduser("~"), ".xny")

def git_clone():
    print(f"|--> Cloning Git Repository")
    repo_url = "https://github.com/adambard/learnxinyminutes-docs"
    subprocess.run(["git", "clone", "--quiet", repo_url, CACHE_DIR], check=True)

def delete_files():
   print("|--> Deleting Unnecessary Files")
   unwanted_files = [
       "README.md",
       "CONTRIBUTING.md", 
       "LICENSE.txt",
       ".gitignore",
       "lint",
       "images"
   ]
   
   for file in unwanted_files:
       file_path = os.path.join(CACHE_DIR, file)
       if os.path.exists(file_path):
           if os.path.isdir(file_path):
               shutil.rmtree(file_path)
           else:
               os.remove(file_path)

def delete_language_folders():
   print("|--> Deleting Language Folders")
   language_folders = [
       'ar', 'be', 'bg', 'ca', 'cs', 'de', 'el', 'es', 'fa', 
       'fi', 'fr', 'he', 'hi', 'hu', 'id', 'it', 'ja', 'ko',
       'lt', 'ms', 'nl', 'no', 'pl', 'pt-br', 'pt-pt', 'ro',
       'ru', 'sk', 'sl', 'sv', 'ta', 'th', 'tr', 'uk', 'vi',
       'zh-cn', 'zh-tw'
   ]
   
   for folder in language_folders:
       folder_path = os.path.join(CACHE_DIR, folder)
       if os.path.exists(folder_path):
           shutil.rmtree(folder_path)

def clean_repo():
    print("|--> Cleaning Cache")
    delete_files()
    delete_language_folders()
    

def update_cache():
    print(f"|--> Updating Cache")
    if os.path.exists(CACHE_DIR):
        shutil.rmtree(CACHE_DIR)
    os.makedirs(CACHE_DIR)
    print(f"|--> Created new cache directory at {CACHE_DIR}")
    git_clone()
    clean_repo()
    print(f"|--> Cache Updated")
