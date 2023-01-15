#!/usr/bin/ python

# Coded by user_honest
# 20/09/2022
# Version 1.0

from colorama import init,Fore


def main():

	print("\n")
	print("██╗  ██╗███████╗██╗  ██╗")
	print("██║  ██║██╔════╝╚██╗██╔╝")
	print("███████║█████╗   ╚███╔╝ ")
	print("██╔══██║██╔══╝   ██╔██╗ ")
	print("██║  ██║███████╗██╔╝ ██╗")
	print("╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
	print("Version 1.0")
	print("\n")

	init()
	GREEN =Fore.GREEN


	def convert(hexSubString):
		return chr(int(hexSubString, 16))

	print("--------------------------------")
	print("Convert Hexadecimals to Strings ")

	print("Enter Hexadecimals")
# Input variable that holds the hexa data
	hexaString = input(">> ")
# Output variable with a empty string 
	outString = ""

	if len (hexaString) % 2 == 0:
		for i in range(0,len(hexaString),2):
			subStr = hexaString[i] + hexaString[i + 1]
			outString += convert(subStr)


	print(f"{GREEN}[+] Decoded String : {outString}")


if __name__ == "__main__":
	main()
