#!/usr/bin/python2
import os
import cgi
import commands

print "Content-Type: text/html"
print "" #left blank to bypass the remaing headers.

#getting html data
mypage_data=cgi.FieldStorage() #FieldStorage is optin in cgi

print "Task will be done"
print "</br>"
name=mypage_data.getvalue('cont_name')

print commands.getoutput("sudo echo  name: "+str(name)+"   > vars.yml ") 
print "</br>"
print "<pre>" #pre tag is used to get output in same format
print commands.getoutput("sudo ansible-playbook stop_cont.yml")
print "</pre>"

print "</br>"
print "test"
print "</br>"

