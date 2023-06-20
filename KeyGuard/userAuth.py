#===userAuth.py======================================#
#   Author: u$3r_h0n3$t
#   Description: userAuth.py file that holds the userAuth
#   for login to the program.
#   to be called upon in main.
#   Version: 1.0
#=====================================================#
# --- <  MODULES  > ------------------------
#========================================================#
import getpass
import os
from cryptography.fernet import Fernet
import bcrypt
import sys
#=======================================================#
##=========================================================================##
####    <Class UserAuth> stores the password to access the db 
####    made in a file, this file is binary file. The key is stored    
####    in a separate file, both are salted.
####    the same key will open, encrypt data in the database.
####    the function will also promt the user to add password, if the
####    password is wrong, 3 times , the session will exit.
##=========================================================================##
class UserAuth:
    def __init__(self):
        self.KEY_FILE = "key.key"
        self.PASSWORD_FILE = "fernet.key"
        self.MAX_ATTEMPTS = 3

    def authenticate_user(self):
        attempts = 0

        if os.path.exists(self.KEY_FILE) and os.path.exists(self.PASSWORD_FILE):
            with open(self.KEY_FILE, 'rb') as f:
                fernet_key = f.read()
            with open(self.PASSWORD_FILE, 'rb') as f:
                hashed_password = f.read()

            while attempts < self.MAX_ATTEMPTS:
                user_password = getpass.getpass("Enter your password to access the database:  \n")

                if self.check_password(hashed_password, user_password):
                    print("[+] Access granted!")
                    break
                else:
                    attempts += 1
                    print("Invalid Password!, \nPlease try again")

            if attempts == self.MAX_ATTEMPTS:
                print("Maximum number of attempts reached. \nExiting Program. ")
                sys.exit(1)

        else:
            print("No passwords set, Create a new password: \n")
            user_password = getpass.getpass("Add new password to access database. \n")
            fernet_key = Fernet.generate_key()
            with open(self.KEY_FILE, 'wb') as f:
                f.write(fernet_key)

            hashed_password = self.hash_password(user_password)
            with open(self.PASSWORD_FILE, 'wb') as f:
                f.write(hashed_password)

        return fernet_key

    def hash_password(self, password):
        salt = bcrypt.gensalt() #<- Adding salt to the hash
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password

    def check_password(self, hashed_password, user_password):
        return bcrypt.checkpw(user_password.encode(), hashed_password)
        
        
# ==========End_of_file=================================================== #
