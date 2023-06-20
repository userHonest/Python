#===selection.py======================================#
#   Author: u$3r_h0n3$t
#   Description: selection file that hold functions 
#   to be called upon in main.
#   Version: 1.0
#=====================================================#
# --- <  MODULES  > ------------------------
#==========================================================#
from cryptography.fernet import Fernet
import getpass
import os
import pickle
import bcrypt
import base64
import sys
#=========================================================#

#--------------------------------------------------------------#
# The PasswordManager class provides methods for interacting 
# with passwords such as storing, retrieving, updating, and 
# deleting. It uses the Fernet encryption provided by the 
# cryptography library to encrypt and decrypt passwords. 
# The _save_db() method is a helper method that saves the 
# passwords, counter, and available_ids to the database 
# file using pickle for serialization
# -------------------------------------------------------------# 

#==  Main Class == # 
class PasswordManager:
    
    def __init__(self, db_path, password):
        self.db_path = db_path
        self.cipher_suite = Fernet(password)
        if os.path.exists(db_path): #<- Load data 
            with open(db_path, "rb") as file:
                loaded_data = pickle.load(file)
                
                # - extracting availabe passowrds with ID counter -- # 
                if len(loaded_data) == 2:
                    self.passwords, self.counter = loaded_data
                    self.availabe_ids = []
                else:
                    self.passwords, self.counter, self.availabe_ids = loaded_data
                    
                if self.passwords:
                    self.counter = max(self.passwords.keys())
                else:
                    self.counter = 1 
                    
        else:
            self.passwords = {}
            self.counter = 0 # <- adding a counter for unique ID
            self.availabe_ids = []# <- Replacing the deleted slot isntead of incrementing it.
  
# ============================================================================================= #
#   Stores a new password in the database
#   Generates a new ID for the password and prompts the user for details
#   Encrypts the password and saves it along with other details to the passwords dictionary
#   Calls the _save_db() method to save the updated database  
# ============================================================================================= #   
    
    def store_password(self):
        
        if self.availabe_ids:
            password_id = min(self.availabe_ids)
            self.availabe_ids.remove(password_id)
        
        else:
            self.counter += 1
            password_id = self.counter
        
        print("\n")    
        title = input("Add a title: ")
        email = input("Add a email: ")
        password = getpass.getpass("Add a password you want to store: ")
        description = input("Add a small description: ")
        
        encrypted_password = self.cipher_suite.encrypt(password.encode())
        self.passwords[password_id] = (encrypted_password, email, title, description)
        self._save_db()
        
        print(f"\n[+] Password with ID {password_id} added to the database ")
    
# ======================================================================= #
#   Retrieves and displays a password based on the given ID
#   Decrypts the password using the cipher suite
#   Prints the password details
# ======================================================================= # 
    def retrieve_password(self, password_id):
        
        password_data = self.passwords.get(password_id)
        if password_data:
            encrypted_password, email,title, description = password_data
            decrypted_password = self.cipher_suite.decrypt(encrypted_password).decode()
            
            print("-" * 30)
            print("ID", password_id)
            print("Title: ", title)
            print("Email: ", email)
            print("Password: ", decrypted_password)
            print("Description: ", description)
            
                
        else:
            print("[-] No password found for ID", password_id)
        
# =========================================================================== #
#   Retrieves and displays a password based on the given ID
#   Decrypts the password using the cipher suite
#   Prints the password details
# =========================================================================== #   
    
    def display_all_passwords(self):
        
        if len(self.passwords) == 0:
            print("[-] No passwords stored in the database.")
            return
        
        for password_id, password_data in self.passwords.items():
            encrypted_password, email, title, description = password_data
            decrypted_password = self.cipher_suite.decrypt(encrypted_password).decode()
        
            print("-" * 30)
            print("ID", password_id)
            print("Title: ", title)
            print("Email: ", email)
            print("Password: ", decrypted_password)
            print("Description: ", description)
            
# ====================================================================================== # 
# Displays all passwords stored in the database
# Decrypts and prints the password details for each password in the passwords dictionary            
# ====================================================================================== #           
    
    
    def update_password(self,password_id):
        
        new_password = getpass.getpass("Enter New password: ")
        encrypted_password = self.cipher_suite.encrypt(new_password.encode())
    
        # If there is data for the given ID, update it
        if password_id in self.passwords:
            _, email, title, description = self.passwords[password_id]
            self.passwords[password_id] = (encrypted_password, email, title, description)
            self._save_db()
            print("\n[+]Password updated for ID:", password_id)
        else:
            print("\n[-] No password found for ID", password_id)

# ================================================================================== #
#   Updates an existing password based on the given ID
#   Prompts the user to enter a new password
#   Encrypts the new password and updates the passwords dictionary
#   Calls the _save_db() method to save the updated database          
# ================================================================================== #            
    
    def delete_password(self, password_id):
        if password_id in self.passwords:
            del self.passwords[password_id]
            self.availabe_ids.append(password_id)
            self._save_db()
            print("\n[+] Password deleted for ID:", password_id)
        else:
            print("\n[-] No password found for ID", password_id)
            
# ============================================================================ # 
#   Saves the passwords, counter, and available_ids to the database file 
#   using pickle for serialization
# ============================================================================ #
    
    def _save_db(self):
        with open(self.db_path, 'wb') as f:
            pickle.dump((self.passwords, self.counter, self.availabe_ids), f)
        
            

# === End_of_file ========================================= #
