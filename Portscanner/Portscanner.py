#!/usr/bin/env python3

# Portscanner v1.2
# 25.01.23
# improved portscanner that uses ThreadPoolExecutor that is 
# It is used to create and manage a pool of worker threads that can be used to execute tasks concurrently.

import argparse
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

# N_THREADS is a global variable that defines 
# the number of worker threads that will be used to perform the port scan concurrently.
N_THREADS = 200

def scanner(host,port):

# we have a try / except block This will raise an exception 
# if the connection cannot be established, for example if 
# the host is unreachable or the port is closed.
	
	try:
		# socket object created and stored in variable s
		s = socket.socket()
		# connect method gets the socket variable nad 
		s.connect((host,port))

	except:

		print(f"{GRAY}{host:15}:{port:5} is closed {RESET}", end='\r')
	else:
		print(f"{GREEN}{host:15}: {port:5} is open  {RESET}")

	finally:
		s.close()


# This code defines the main function, which takes two arguments: host and ports.
def main(host, ports):
	
# The function creates a new ThreadPoolExecutor object with max_workers=N_THREADS 
# which is the number of worker threads to use for scanning ports.
	
	with ThreadPoolExecutor(max_workers=N_THREADS) as executor:

		futures = [executor.submit(scanner,host,port) for port in ports]

		for future in as_completed(futures):
			future.result()


if __name__ == '__main__':

	# in the main we use argparse arguments to execute commandline arguments with the script
	parser = argparse.ArgumentParser(description="Port Scanner ")
	parser.add_argument("host", help="Host to scan. ")
	parser.add_argument("--ports", "-p", dest="ports", default="1-65535", 
		help="Port in range to scan in the form of 'start-end'. Default is 1-65535 (all ports).")

	# This code is responsible for parsing the command-line arguments passed 
	# to the script and passing them to the main function.
	args = parser.parse_args()
	host, ports = args.host, args.ports

	# splits the ports argument by '-' and 
	start_port, end_port = map(int, ports.split("-"))
	ports = range(start_port, end_port + 1)

	# the main(host, ports) function is called, passing in the host and ports variables as arguments.
	main(host, ports)
