#!/usr/bin/python3

import cgi
print("content-type: text/html")
print()

form = cgi.FieldStorage()
inp1 = form.getvalue("inp1")
import subprocess as sp
print("<html>")
print("<body>")
print(inp1)
print(form)
print(sp.getoutput(inp1))
print("</body>")
print("</html>")

