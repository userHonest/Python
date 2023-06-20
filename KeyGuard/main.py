#===main.py======================================#
#   Author: u$3r_h0n3$t
#   Description: Main function that holds the menu 
#   Name: Password Manager
#   Version: 1.0
#=====================================================#
# ---< MODULES > ------------------------------------- 
#=====================================================#
import getpass
import sys
import os
from userAuth import UserAuth
sys.path.append("/home/python/Documents/python/Pasword_Manager")
import selection
from selection import PasswordManager
#=====================================================#
#--------------------------------------------------------------------------------#
#  this program provides a simple interface for managing passwords by 
#  storing them securely in a database file
#  It allows users to store, retrieve, update, and delete passwords 
#  for different types of accounts or services
#  The progrma has a main function that displays the authenticate class 
#  User must provide a password that will be ecnrypted, this paswoword will
#   authenticate the login for next login time.
# ------------------------------------------------------------------------------#

## Main function ======##
def main():
    
    print("\nKeyGuard")
    print("Version 1.0\n")
    # creating user auth instance
    user_auth = UserAuth()
    
    # asking user when the program starts.
    password = user_auth.authenticate_user()
    
    
    while True:
        print("-" * 30)
        print("1: Store a Password")
        print("2: Retrieve a Password")
        print("3: Update a Password")
        print("4: Delete a Password")
        print("5. Display All")
        print("9: Quit")
        
        try:
            option = int(input("\nEnter an option: "))
        except ValueError:
            print("[-] Invalid input. Please enter a number.")
            continue
            
        if option == 9:
            print("\nExiting program..")
            break
        
        try:
         
            password_type_menu = int(input("1: Email \n2: Service \nEnter a password type: "))
        except ValueError:
            print("Invalid input, Please enter a number.")
            continue
            
        password_type = "Email" if password_type_menu == 1 else "Service"
        db_path = 'dataEmail.bin' if password_type == "Email" else 'dataService.bin'
        
        password_manager = PasswordManager(db_path, password)

        if option == 1:
            password_manager.store_password()
        
        elif option in [2, 3, 4]:
            print(f"\nThere are currently <{len(password_manager.passwords)}> ID's in the database.")
            
            password_id = int(input("\nEnter the ID for the existing entry: "))
            
            if option == 2:
                password_manager.retrieve_password(password_id)
            
            elif option == 3:
                password_manager.update_password(password_id)
            
            elif option == 4:
                password_manager.delete_password(password_id)
            
        elif option == 5:
            print("\nDisplaying all passwords")
            print("-" * 30)
            password_manager.display_all_passwords()

# ==== INIT MAIN ========#  
if __name__ == "__main__":
    main()
        
# == End of file  == # 
       
