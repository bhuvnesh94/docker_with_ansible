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


x=commands.getoutput("sudo echo  name: "+str(name)+"   > vars.yml ")
y=commands.getoutput("sudo echo  image: "+str(image)+"   >> vars.yml ")

print x
print "</br>"
print y
print "</br>"

print "<pre>"
print commands.getoutput("sudo ansible-playbook launch_cont.yml")
print "</pre>"

