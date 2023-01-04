# Simple-MD5-Scraper
Just a simple python script that takes any readable file type and scrapes md5 hashes out using regex.

# usage:
python simple_md5_tool.py path/to/file.sql

-h --help and empty args will show the above example. Will print out hashes if 10 or less, otherwise will just save them to a file and tell you the count.
-c will add a visual of the number rising (purely visual, actually slows it down)
-rD will remove any duplicate hashes
