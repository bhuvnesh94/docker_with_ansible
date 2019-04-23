#!/usr/bin/python2
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
print "<br/>"

m=commands.getoutput("sudo ansible-playbook launch_cont.yml ")
#p=os.system("sudo  ansible-playbook test.yml")
print "<br/>"
s=commands.getoutput("date")
print s
print "<br/>"
print m
