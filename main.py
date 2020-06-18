#!/usr/local/bin/python3
import subprocess
import optparse
import re
print("hello world")

output = subprocess.check_output(["ls","-ltr"])
print(str(output))
result = re.findall(r'\w\w-\w',  str(output))
if result:
    print(result)
else:
    print("no result")