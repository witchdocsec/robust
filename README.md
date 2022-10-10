# robust
directory and file enumeration tool. if your wordlist didn't find anything this is your best bet. robust is built on dirgenerate and works by dorking for robots.txt files and parsing the dissalow entries then checking for them on the target site. as such it requires no wordlist

# useage
python3 robust.py <ur> <status codes to match , seperated>
