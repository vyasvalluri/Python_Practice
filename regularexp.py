#!/usr/bin/env python3

import re

def all_matches_find(text, pattern):
	print(pattern)
	reobj = re.compile(pattern)
	for m in reobj.finditer(text):
		print(str(m.start())+" - "+str(m.end())+":"+text[m.start(): m.end()])

#all_matches_find("xyxyyxyyyyyxxxxyxyxxyy","xy*") # start with x and 0 or more y's
all_matches_find("xyxyyxyyyyyxxxxyxyxxyy","xy?") # start with x and 0 or 1 y's