import requests
import hashlib

def hash_passwords(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest.upper()
    return sha1_hash

def check_password(password):
    flag = False
    sha_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    sha_pass_prefix = sha_pass[:5]
    sha_pass_suffix = sha_pass[5:]
    response = requests.get(f'https://api.pwnedpasswords.com/range/{sha_pass_prefix}')
    hash_list = response.text.splitlines()
    for hash in hash_list:
        suffix, count = hash.split(':')
        if sha_pass_suffix == suffix:
            return True, count
    if not flag:
        return False, 0

def check_creds(file_path):
    credentials = {}
    with open('pwdlst.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                username, password = line.split(', ', 1)
                print(f"Checking for username: {username}.")
                is_leaked, count = check_password(password)
                if is_leaked:
                    print(f"Password for {username} is leaked {count} times.")
                else:
                    print(f"Password for {username} is Safe.")


    
check_creds('pwdlist.txt') 
