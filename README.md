# robust
directory and file enumeration tool. if your wordlist didn't find anything this is your best bet. robust is built on dirgenerate and works by dorking for robots.txt files and parsing the dissalow entries then checking for them on the target site. as such it requires no wordlist

# useage
robust.py [-h] [--url URL] [--codes CODES [CODES ...]] [-nosplit NOSPLIT]  
--url=url to scan  
--codes=status codes to match  
-nosplit (optional flag to look for paths as they appear in robosts.txt instead of dir by dir)

![image](https://user-images.githubusercontent.com/107813117/194931560-c04eb6bc-cf06-4787-8dbf-302cc3a3cb45.png)
