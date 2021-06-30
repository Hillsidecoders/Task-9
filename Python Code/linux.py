#!/usr/bin/python3
print("content-type: text/html:")
print()

import cgi
import subprocess

f=cgi.FieldStorage()
cmd=f.getvalue("x") 
res=subprocess.getoutput("sudo "+cmd)
print(res)
