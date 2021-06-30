#!/usr/bin/python3

import cgi
import subprocess


print("content-type: text/html")
print()


output = subprocess.getoutput(" sudo kubectl get deployment")

print(output)
