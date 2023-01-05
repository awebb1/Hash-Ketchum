#!/usr/bin/env python3

import re
import sys
import datetime
import argparse

HELP_MSG_COLOR = '\033[1;37;40m'
ERROR_COLOR = '\033[1;31;40m'
SUCCESS_COLOR = '\033[1;36;40m'
PROCESSING_COLOR = '\033[1;35;40m'
COUNTING_COLOR = '\033[1;33;40m'
GREEN_COLOR = '\033[1;32;40m'
DEFAULT_COLOR = '\033[1;0;40m'

parser = argparse.ArgumentParser(description='Scrape MD5 hashes from a readable file', epilog=f'{ERROR_COLOR}eg:{DEFAULT_COLOR} hashketchum.py {GREEN_COLOR}path/to/file.sql{DEFAULT_COLOR} -c')
parser.add_argument('file', help='the file to scrape hashes from')
parser.add_argument('-c', '--count', action='store_true', help='display a pretty visual of the number rising')
parser.add_argument('-rD', action='store_true', help='remove duplicates from list')

args = parser.parse_args()

def main ():
	try:
	    md5()
	except FileNotFoundError:
	    print(f"\n{ERROR_COLOR}[-] {HELP_MSG_COLOR}File not found")
	except:
	    print(f"\n{ERROR_COLOR}[-] {HELP_MSG_COLOR}An unknown error occurred")

def md5():
	count = 0
	file_name = args.file

	with open(file_name) as input_file:
		file_content = input_file.read()

	print(f"\n{SUCCESS_COLOR}[+] {HELP_MSG_COLOR}File loaded, attempting scrape...")

	hash_list = re.findall(r"([a-f\d]{32})", file_content, re.I)
	if hash_list:
		print(f"{SUCCESS_COLOR}[+] {HELP_MSG_COLOR}Hashes Found\n", end='')

		if args.rD:
			hash_list = removeDuplicates(hash_list)
        
		print(f"{SUCCESS_COLOR}[+] {HELP_MSG_COLOR}Processing File...")

		for hash in hash_list:
			count += 1
			if args.count:
				print(f'\r{PROCESSING_COLOR}[+] {COUNTING_COLOR}{count}', end='')

		if args.count:
			print(f'\r{PROCESSING_COLOR}[+] {ERROR_COLOR}{count}\n', end='')

	print(f"{SUCCESS_COLOR}[+] {HELP_MSG_COLOR}Complete\n")

	if hash_list:
		hashes = '\n'.join(hash_list)
		with open("scraped_hashes_" + str(datetime.datetime.now()) + ".txt", "w") as f:
			f.write(hashes)

		if count < 11:
			print(f"{SUCCESS_COLOR}[+] {ERROR_COLOR}{count} {HELP_MSG_COLOR}Hashes Found and Saved to {GREEN_COLOR}./scraped_hashes_{str(datetime.datetime.now())}.txt")
		else:
			print(f"{SUCCESS_COLOR}[+] {ERROR_COLOR}{count} {HELP_MSG_COLOR}Hashes Found and Saved to {GREEN_COLOR}./scraped_hashes_{str(datetime.datetime.now())}.txt")
	else:
		print(f"{ERROR_COLOR}[X] {HELP_MSG_COLOR}No Hashes Found")

def removeDuplicates(hash_list):
	print(f"\r{SUCCESS_COLOR}[+] {HELP_MSG_COLOR}Removing Any Duplicates...", end='')
	hash_list = [*set(hash_list)]
	print(f"\r{SUCCESS_COLOR}[+] {HELP_MSG_COLOR}Removing Any Duplicates...DONE\n", end='')

	return hash_list

if __name__ == '__main__':
	main()
