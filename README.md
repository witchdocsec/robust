# robust
directory and file enumeration tool. if your wordlist didn't find anything this is your best bet. robust is built on dirgenerate and works by dorking for robots.txt files and parsing the dissalow entries then checking for them on the target site. as such it requires no wordlist

# useage
python3 robust.py [-h] [--url URL] [--codes CODES [CODES ...]] [-cookie COOKIE [COOKIE ...]] [-uagent UAGENT [UAGENT ...]] [-nosplit NOSPLIT]
--url=url to scan  
--codes=status codes to match  
-cookie (optional flag to pass cookie for authenticated fuzzing)  
-uagent (optional flag for user-agent)  
-nosplit (optional flag to look for paths as they appear in robosts.txt instead of dir by dir)

# example
python3 robust.py --url https://example.com --codes 200 403 --cookie role=user; id=1356 --uagent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0" -nosplit

![image](https://user-images.githubusercontent.com/107813117/202379537-de8add16-4bb0-47dd-b454-42cfd89eed02.png)
