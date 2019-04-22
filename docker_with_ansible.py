#!/usr/bin/python
import os
import cgi
import commands

print "Content-Type: text/html"
print "" #left blank to bypass the remaing headers.

#getting html data
mypage_data=cgi.FieldStorage() #FieldStorage is optin in cgi
print "Task will be done"


name=mypage_data.getvalue('cont_name')
image=mypage_data.getvalue('cont_image')

print "<br/>"
print name
print "<br/>"
print image
print "<br/>"
print "<pre>" #pre tag is used to get output in same format
print "</pre>"

m=commands.getoutput("ansible-playbook launch_cont.yml -e name="+str(name)+"-e image="+str(image)+"")
s=commands.getoutput("date")
print s
print m
