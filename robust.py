import requests
from duckduckgo_search import ddg
import tldextract
import numpy as np
import threading
import argparse
import re

def parser():
	parser = argparse.ArgumentParser(description="robust args")
	parser.add_argument("--url")
	parser.add_argument("--codes",nargs="+")
	parser.add_argument("-nosplit")
	args = parser.parse_args()
	runrobust(args)

def runrobust(args):
	found=[]
	def bust(href):
		try:
			r=requests.get(href)
			splitl=r.text.split("\n")
			splitl=list(set(splitl))
			for line in splitl:
				if "Disallow: " in line:
					if args.nosplit:
						lnsplt=line
					else:
						lnsplt=line.replace("Disallow: ","").split("/")
					for entry in lnsplt:
						entry=entry.split("?")[0].replace("*","")
						entry=entry.split("&")[0]
						if not re.match(entry, "\s") and not tldextract.extract(href).domain.split(".")[0] in entry.lower() and len(entry) < 25 and not entry in found and not "#" in entry:
							r=requests.get(args.url+"/"+entry, allow_redirects=False)
							if str(r.status_code) in args.codes:
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

parser()
