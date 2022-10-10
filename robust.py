import requests
from duckduckgo_search import ddg
import tldextract
import numpy as np
import threading
import sys
import re
if len(sys.argv) != 3:
	print("useage: python3 robust.py <url> <status codes to match , seperated>")
	exit()
codes=sys.argv[2].split(",")
found=[]
def bust(href):
	try:
		r=requests.get(href)
		splitl=r.text.split("\n")
		splitl=list(set(splitl))
		for line in splitl:
			if "Disallow: " in line:
				lnsplt=line.replace("Disallow: ","").split("/")
				for entry in lnsplt:
					q=entry.split("?")
					entry=q[0].replace("*","")
					if not re.match(entry, "\s") and not tldextract.extract(href).domain.split(".")[0] in entry.lower() and len(entry) < 25 and not entry in found and not "#" in entry:
						r=requests.get(sys.argv[1]+"/"+entry, allow_redirects=False)
						if str(r.status_code) in codes:
							print("found: "+entry+" ["+str(r.status_code)+"]")
							found.append(entry)
	except:
		pass


def split(a,n):
	return(np.array_split(a, n))

with open("banner.txt","r") as banner:
	print(banner.read())

keywords = "filetype:TXT +inurl:\"robots.txt\""
results = ddg(keywords, max_results=250)
results=(href for href in (res["href"] for res in results))
results=[*results]
results=split(results,5)

for chunk in results:
	threads=[]
	for href in chunk:
		t=threading.Thread(target=bust, args=([href]))
		threads.append(t)
		t.start()
	for t in threads:
		t.join()




print(*splt)
