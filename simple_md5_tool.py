#!/usr/bin/env python

import re
import sys
import datetime

hashes = ''

# create a dict for args
arg_name = ['script', 'file', 'option1', 'option2']
args = dict(zip(arg_name, sys.argv))

help_msg = '\n\033[1;37;40mPlease provide a file after the script:\n\t\033[1;31;40meg: \033[1;37;40mpython simple_md5_tool.py \033[1;32;40mpath/to/file.sql\n\t    \033[1;37;40mpython simple_md5_tool.py \033[1;32;40mpath/to/file.txt\n\n\033[1;37;40moptions (after file):\n\t -c, --count:\twill display a pretty visual of the number rising\n\t -rD:\t\twill remove duplicates from list'

# display help message if no args provided
if len(args) < 2:
	print(help_msg)
	exit()

try:
	count = 0

	if args['file'] == '-h' or args['file'] == 'help' or args['file'] == '--help':
		print(help_msg)
		exit()
	file_name = sys.argv[1]

	input_file = open(file_name)
	file_content = input_file.read()

	print("\n\033[1;36;40m[+] \033[1;37;40mFile loaded, attempting scrape...")

	if re.findall(r"([a-fA-F\d]{32})", file_content):
		hash_list = re.findall(r"([a-fA-F\d]{32})", file_content)

		if '-rD' in args.values() or '--rD' in args.values():
			print("\r\033[1;36;40m[+] \033[1;37;40mHashes Found, Removing Any Duplicates...", end='')

			hash_list = [*set(hash_list)]

			print("\r\033[1;36;40m[+] \033[1;37;40mHashes Found, Removing Any Duplicates...DONE\n", end='')
		
		print("\r\033[1;36;40m[+] \033[1;37;40mProcessing...")

		for hash in hash_list:
			hashes += hash + '\n'
			count += 1

			if '-c' in args.values() or '--count' in args.values():
				print('\r\033[1;35;40m[+] \033[1;33;40m' + str(count), end='')

		if '-c' in args.values() or '--count' in args.values():
			print('\r\033[1;35;40m[+] \033[1;33;40m' + str(count) + '\n', end='')

	print("\033[1;36;40m[+] \033[1;37;40mScrape Complete\n")


	if len(hashes) > 0:
		hashes = hashes[:len(hashes) - 1]

		if count < 11:
			print("\033[1;36;40m[+] \033[1;37;40mHashes Found and Saved:\n\n" + hashes)
		else:
			print("\033[1;32;40m[!] \033[1;37;40mFound and Saved \033[1;31;40m" + str(count) + " \033[1;37;40mHashes")

		if len(hashes) > 0:
			f = open("scarped_hashes_" + str(datetime.datetime.now()) + ".txt", "w")
			f.write(hashes)
			f.close()
	else:
		print("\033[1;31;40m[X] \033[1;37;40mNo Hashes Found\n")
	input_file.close()

except IOError:
	print('\n\033[1;31;40mERROR: \033[1;37;40mFile \033[1;31;40m' + args['file'] + ' \033[1;37;40mCould Not Be Found')
