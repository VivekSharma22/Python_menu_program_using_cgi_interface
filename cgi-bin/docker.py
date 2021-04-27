#! /usr/bin/python3

import cgi
print("content-type: text/html")
print()

form=cgi.FieldStorage()
cmd=form.getvalue("inp")
inp1=form.getvalue("inp1")
if (inp1!=None):
    img=form.getvalue("img")
    imgdoc=form.getvalue("imgdoc")
    name=form.getvalue("name")

import subprocess as sp
if(cmd!=None):
    print(sp.getoutput(cmd))
elif (inp1=='10'):
    print(img,name)
    c="sudo docker pull {}".format(img)
    print(sp.getoutput(c))
elif (inp1=='11'):
    print("launch",imgdoc,name)
    c="sudo docker run -d  --name {} {}".format(name,imgdoc)
    print(sp.getoutput(c))
elif (inp1=='12'):
    print("stop ",name)
    c="sudo docker stop {}".format(name)
    print(sp.getoutput(c))
