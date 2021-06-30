#!/usr/bin/python3
print("content-type: text/html")
print()


import cgi
import subprocess
cmd = cgi.FieldStorage()
cont = cmd.getvalue("d")

output=subprocess.getoutput("sudo kubectl delete deployment " +cont)

print("Command Executed: " +output)
