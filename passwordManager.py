import os
from cryptography.fernet import Fernet

'''
Load this function once to create the key for the encryption
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
'''
def load_key():
    with open('key.key', 'rb') as file:
        key = file.read()
    return key


master_pwd = input('What is your master password? ') 
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def prompt_master_pass():
    master_pwd = input('What is your master password? ')
    return master_pwd

def add(master_pwd):
    with open('masterpass.key', 'r') as file:
        master = file.read()
        master_pass = fer.decrypt(master.encode()).decode()
    
    if master_pwd == master_pass:
        acc_name = input('Account Name: ')
        pwd = input('Password: ')
        with open('passwords.txt', 'a') as f:
            f.write(acc_name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')
        return True
    else:
        print('MASTER PASSWORD INCORRECT!')
        response = input('Do you want to enter again? (yes/no) ').lower()
        if response == 'yes':
            master_pwd = prompt_master_pass()
            add(master_pwd)
        else:
            quit()

def view(master_pwd):
    with open('masterpass.key', 'r') as file:
        master = file.read()
        master_pass = fer.decrypt(master.encode()).decode()

    if master_pwd == master_pass:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, password = data.split('|')
                print('User:', user, '| Password:', fer.decrypt(password.encode()).decode())
    else:
        print('MASTER PASSWORD INCORRECT!')
        response = input('Do you want to enter again? (yes/no) ').lower()
        if response == 'yes':
            master_pwd = prompt_master_pass()
            view(master_pwd)
        else:
            quit()

def main():
    if not os.path.exists('masterpass.key'):
        with open('masterpass.key', 'w') as f:
            f.write(fer.encrypt(master_pwd.encode()).decode())
    while True:
        choice = input('Would you like to add a new password or view existing ones? (click Q to Quit) ').lower()
        
        if choice == 'q':
            quit()
        if choice == 'add':
            add(master_pwd)
        elif choice == 'view':
            view(master_pwd)
        else:
            print('INVALID CHOICE!')

if __name__ == '__main__':
    main()