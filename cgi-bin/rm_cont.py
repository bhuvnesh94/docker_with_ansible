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
print "<pre>"
print "<br/>"
print name
print "<br/>"
print image
print "<br/>"
print "</pre>"


x=commands.getoutput("sudo echo  name: "+str(name)+"   > vars.yml ")

print x
print "</br>"

z=os.system("sudo ansible-playbook rm_cont.yml")
print z
print "</br>"
